from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session

import shutil
import os
import json

from app.database import get_db
from app.models import Candidate, Resume, RecruitmentProgress

from app.services.resume_parser import extract_text_from_pdf
from app.services.skill_extractor import extract_skills
from app.services.email_service import send_ats_result_email

from app.aws_s3 import upload_file_to_s3


router = APIRouter()


REQUIRED_SKILLS = [
    "AWS",
    "Docker",
    "Kubernetes",
    "Terraform",
    "Jenkins",
    "Git",
    "Python",
    "Linux"
]


# =====================================
# UPLOAD RESUME TO AWS S3
# =====================================

@router.post("/upload-resume")
def upload_resume(
    candidate_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = None

    try:

        # 1. VERIFY CANDIDATE

        candidate = db.query(Candidate).filter(
            Candidate.id == candidate_id
        ).first()

        if not candidate:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found"
            )


        # 2. VALIDATE FILE

        original_filename = os.path.basename(
            file.filename or "resume.pdf"
        )

        if not original_filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF resumes are allowed"
            )


        # 3. TEMPORARILY SAVE RESUME LOCALLY

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join(
            "uploads",
            f"candidate_{candidate_id}_{original_filename}"
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)


        # 4. EXTRACT RESUME TEXT

        resume_text = extract_text_from_pdf(file_path)


        # 5. EXTRACT SKILLS

        skills = extract_skills(resume_text)


        # 6. CALCULATE ATS MATCH PERCENTAGE

        matched_skills = [
            skill for skill in skills
            if skill in REQUIRED_SKILLS
        ]

        matched = len(matched_skills)

        total_required = len(REQUIRED_SKILLS)

        match_percentage = round(
            (matched / total_required) * 100,
            2
        )


        # 7. DETERMINE ATS RESULT

        ats_passed = match_percentage >= 70

        ats_status = (
            "Passed" if ats_passed else "Failed"
        )


        # 8. GENERATE S3 OBJECT KEY

        object_key = (
            f"resumes/candidate_{candidate_id}/"
            f"{original_filename}"
        )


        # 9. UPLOAD RESUME TO AMAZON S3

        upload_success = upload_file_to_s3(
            file_path,
            object_key
        )

        if not upload_success:
            raise HTTPException(
                status_code=500,
                detail="Resume upload to AWS S3 failed"
            )


        # 10. SAVE RESUME DETAILS IN POSTGRESQL

        resume = Resume(
            candidate_id=candidate_id,
            filename=original_filename,
            resume_text=resume_text,
            skills=json.dumps(skills),
            match_percentage=str(match_percentage)
        )

        db.add(resume)


        # 11. GET RECRUITMENT PROGRESS

        progress = db.query(RecruitmentProgress).filter(
            RecruitmentProgress.candidate_id == candidate_id
        ).first()


        # CREATE PROGRESS RECORD IF NOT AVAILABLE

        if not progress:

            progress = RecruitmentProgress(
                candidate_id=candidate_id
            )

            db.add(progress)


        # 12. UPDATE RECRUITMENT PROGRESS

        progress.ats_status = ats_status

        if ats_passed:

            progress.current_stage = "aptitude"

            progress.aptitude_status = "Pending"

        else:

            progress.current_stage = "ats"

            progress.aptitude_status = "Locked"


        # 13. SAVE CHANGES IN DATABASE

        db.commit()

        db.refresh(resume)

        db.refresh(progress)


        # 14. SEND ATS RESULT EMAIL

        try:

            email_result = send_ats_result_email(
                recipient_email=candidate.email,
                candidate_name=candidate.name,
                match_percentage=match_percentage
            )

        except Exception as error:

            print("ATS email sending failed:", error)

            email_result = {
                "success": False,
                "message": str(error)
            }


        # 15. RETURN RESPONSE

        return {

            "message": "Resume Uploaded Successfully",

            "storage": "Amazon S3",

            "bucket": "smarthire-ai-resumes-2026",

            "s3_key": object_key,

            "resume_id": resume.id,

            "candidate_id": candidate_id,

            "filename": original_filename,

            "skills": skills,

            "matched_skills": matched_skills,

            "match_percentage": match_percentage,

            "ats_status": ats_status,

            "next_stage": (
                "aptitude" if ats_passed else "Not eligible"
            ),

            "email_sent": email_result.get(
                "success", False
            ),

            "email_message": email_result.get(
                "message",
                "Email processing completed"
            )

        }


    except HTTPException:

        db.rollback()
        raise


    except Exception as error:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Resume processing failed: {str(error)}"
        )


    finally:

        # REMOVE TEMPORARY LOCAL FILE

        if file_path and os.path.exists(file_path):

            os.remove(file_path)


# =====================================
# GET CANDIDATE RESUME
# =====================================

@router.get("/resume/{candidate_id}")
def get_resume(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    resume = db.query(Resume).filter(
        Resume.candidate_id == candidate_id
    ).order_by(
        Resume.id.desc()
    ).first()


    if not resume:

        return {
            "resume_uploaded": False
        }


    try:

        skills = json.loads(resume.skills)

    except (TypeError, json.JSONDecodeError):

        skills = []


    object_key = (
        f"resumes/candidate_{candidate_id}/"
        f"{resume.filename}"
    )


    return {

        "resume_uploaded": True,

        "resume_id": resume.id,

        "candidate_id": resume.candidate_id,

        "filename": resume.filename,

        "storage": "Amazon S3",

        "s3_key": object_key,

        "skills": skills,

        "match_percentage": resume.match_percentage

    }