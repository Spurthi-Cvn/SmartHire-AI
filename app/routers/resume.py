from fastapi import APIRouter, UploadFile, File
import shutil

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


@router.post("/upload-resume")
def upload_resume(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)

    skills = extract_skills(resume_text)

    matched = len(skills)

    total_required = len(REQUIRED_SKILLS)

    match_percentage = round(
        (matched / total_required) * 100,
        2
    )

    return {
        "message": "Resume Uploaded Successfully",
        "skills": skills,
        "match_percentage": match_percentage
    }