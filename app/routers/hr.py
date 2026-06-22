from fastapi import APIRouter

router = APIRouter()


@router.get("/hr")
def hr_interview():

    questions = [
        {
            "id": 1,
            "question": "Tell me about yourself."
        },
        {
            "id": 2,
            "question": "Why do you want to join our company?"
        },
        {
            "id": 3,
            "question": "What are your strengths?"
        },
        {
            "id": 4,
            "question": "Where do you see yourself in 5 years?"
        },
        {
            "id": 5,
            "question": "Are you willing to relocate?"
        }
    ]

    return {
        "round": "HR Interview",
        "questions": questions
    }
    
from fastapi import APIRouter
from app.schemas import HRAnswers

router = APIRouter()

@router.get("/hr")
def hr_interview():
    return {
        "round": "HR Interview",
        "questions": [
            {"id": 1, "question": "Tell me about yourself"},
            {"id": 2, "question": "Why should we hire you?"},
            {"id": 3, "question": "What are your strengths?"},
            {"id": 4, "question": "Are you willing to relocate?"},
            {"id": 5, "question": "Where do you see yourself in 5 years?"}
        ]
    }


@router.post("/hr/submit")
def submit_hr(test: HRAnswers):

    score = len(test.answers) * 20

    status = (
        "Selected"
        if score >= 60
        else "Rejected"
    )

    return {
        "hr_score": score,
        "status": status
    }