from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import CommunicationAnswers
from app.database import get_db
from app.models import Candidate, RecruitmentProgress

router = APIRouter()


# =====================================
# GET COMMUNICATION QUESTIONS
# =====================================

@router.get("/communication")
def communication_test():

    questions = [
        {
            "id": 1,
            "question": "Choose the correct sentence.",
            "options": [
                "She go to office daily.",
                "She goes to office daily.",
                "She going to office daily.",
                "She gone to office daily."
            ]
        },
        {
            "id": 2,
            "question": "What is the synonym of 'Reliable'?",
            "options": [
                "Trustworthy",
                "Weak",
                "Slow",
                "Lazy"
            ]
        },
        {
            "id": 3,
            "question": "Choose the correct email greeting.",
            "options": [
                "Hey Dude",
                "Dear Hiring Manager",
                "Yo",
                "What's Up"
            ]
        }
    ]

    return {
        "test_name": "Communication Round",
        "total_questions": len(questions),
        "questions": questions
    }


# =====================================
# SUBMIT COMMUNICATION ASSESSMENT
# =====================================

@router.post("/communication/submit")
def submit_communication(
    test: CommunicationAnswers,
    db: Session = Depends(get_db)
):

    # Step 1: Validate candidate

    candidate = db.query(Candidate).filter(
        Candidate.id == test.candidate_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    # Step 2: Validate answers

    correct_answers = {
        "1": "She goes to office daily.",
        "2": "Trustworthy",
        "3": "Dear Hiring Manager"
    }

    valid_options = {
        "1": [
            "She go to office daily.",
            "She goes to office daily.",
            "She going to office daily.",
            "She gone to office daily."
        ],
        "2": [
            "Trustworthy",
            "Weak",
            "Slow",
            "Lazy"
        ],
        "3": [
            "Hey Dude",
            "Dear Hiring Manager",
            "Yo",
            "What's Up"
        ]
    }

    if set(test.answers.keys()) != set(correct_answers.keys()):
        raise HTTPException(
            status_code=400,
            detail="Please answer all 3 questions."
        )

    for question_id, answer in test.answers.items():

        if answer not in valid_options[question_id]:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid answer for question {question_id}."
            )

    # Step 3: Calculate score

    score = 0

    for question_id, answer in test.answers.items():

        if correct_answers[question_id] == answer:
            score += 1

    total_questions = len(correct_answers)

    percentage = round(
        (score / total_questions) * 100,
        2
    )

    status = "Passed" if percentage >= 60 else "Failed"

    # Step 4: Find recruitment progress

    progress = db.query(RecruitmentProgress).filter(
        RecruitmentProgress.candidate_id == test.candidate_id
    ).first()

    if not progress:
        raise HTTPException(
            status_code=404,
            detail="Recruitment progress not found."
        )

    # Step 5: Update recruitment progress

    progress.communication_status = status

    if status == "Passed":

        progress.current_stage = "hr"
        progress.hr_status = "Pending"

    else:

        progress.current_stage = "communication"
        progress.hr_status = "Locked"

    # Step 6: Save to PostgreSQL

    try:

        db.commit()
        db.refresh(progress)

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to save communication result."
        )

    # Step 7: Return result

    return {
        "message": "Communication Assessment Completed",
        "candidate_id": candidate.id,
        "candidate_name": candidate.name,
        "score": score,
        "total_questions": total_questions,
        "percentage": percentage,
        "status": status,
        "next_stage": (
            "hr" if status == "Passed"
            else "Not eligible"
        )
    }