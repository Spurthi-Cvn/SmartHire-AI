from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
import shutil
import os
import json

from app.database import get_db
from app.models import Candidate, Resume

from app.services.resume_parser import extract_text_from_pdf
from app.services.skill_extractor import extract_skills

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


# =========================
# UPLOAD RESUME TO AWS S3
# =========================

@router.post("/upload-resume")
def upload_resume(
    candidate_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    # 1. Verify candidate

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    # 2. Validate file

    original_filename = os.path.basename(
        file.filename or "resume.pdf"
    )

    if not original_filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF resumes are allowed"
        )

    # 3. Temporarily save resume locally

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        f"candidate_{candidate_id}_{original_filename}"
    )

    try:

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 4. Extract resume text

        resume_text = extract_text_from_pdf(file_path)

        # 5. Extract skills

        skills = extract_skills(resume_text)

        # 6. Calculate ATS match percentage

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

        # 7. Generate S3 object key

        object_key = (
            f"resumes/candidate_{candidate_id}/"
            f"{original_filename}"
        )

        # 8. Upload resume to Amazon S3

        upload_success = upload_file_to_s3(
            file_path,
            object_key
        )

        if not upload_success:
            raise HTTPException(
                status_code=500,
                detail="Resume upload to AWS S3 failed"
            )

        # 9. Save resume details in PostgreSQL

        resume = Resume(
            candidate_id=candidate_id,
            filename=original_filename,
            resume_text=resume_text,
            skills=json.dumps(skills),
            match_percentage=str(match_percentage)
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        # 10. Return response

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
            "match_percentage": match_percentage
        }

    except HTTPException:
        raise

    except Exception as error:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Resume processing failed: {str(error)}"
        )

    finally:

        # Remove temporary local file

        if os.path.exists(file_path):
            os.remove(file_path)


# =========================
# GET CANDIDATE RESUME
# =========================

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
    