from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
import shutil
import os
import json

from app.database import get_db
from app.models import Candidate, Resume

from app.services.resume_parser import extract_text_from_pdf
from app.services.skill_extractor import extract_skills


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
# UPLOAD RESUME
# =========================

@router.post("/upload-resume")
def upload_resume(
    candidate_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        return {
            "message": "Candidate not found"
        }


    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


    resume_text = extract_text_from_pdf(file_path)

    skills = extract_skills(resume_text)


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


    resume = Resume(

        candidate_id=candidate_id,

        filename=file.filename,

        resume_text=resume_text,

        skills=json.dumps(skills),

        match_percentage=str(match_percentage)

    )


    db.add(resume)

    db.commit()

    db.refresh(resume)


    return {

        "message": "Resume Uploaded Successfully",

        "resume_id": resume.id,

        "candidate_id": candidate_id,

        "filename": file.filename,

        "skills": skills,

        "match_percentage": match_percentage

    }


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
    except:
        skills = []


    return {

        "resume_uploaded": True,

        "resume_id": resume.id,

        "candidate_id": resume.candidate_id,

        "filename": resume.filename,

        "skills": skills,

        "match_percentage": resume.match_percentage

    }