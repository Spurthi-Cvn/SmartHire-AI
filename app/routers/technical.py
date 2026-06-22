from fastapi import APIRouter
from app.schemas import TechnicalAnswers

router = APIRouter()


@router.get("/technical")
def technical_interview():

    questions = [
        {
            "id": 1,
            "question": "What is Terraform used for?"
        },
        {
            "id": 2,
            "question": "Explain Docker Container."
        },
        {
            "id": 3,
            "question": "What is Kubernetes?"
        },
        {
            "id": 4,
            "question": "What is CI/CD?"
        },
        {
            "id": 5,
            "question": "Difference between EC2 and S3?"
        }
    ]

    return {
        "round": "Technical Interview",
        "questions": questions
    }
    
@router.post("/technical/submit")
def submit_technical(test: TechnicalAnswers):

    score = len(test.answers) * 20

    status = (
        "Selected For HR Round"
        if score >= 60
        else "Rejected"
    )

    return {
        "technical_score": score,
        "status": status
    }