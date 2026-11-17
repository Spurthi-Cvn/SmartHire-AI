from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import HRAnswers
from app.database import get_db
from app.models import Candidate, RecruitmentProgress

router = APIRouter()


# =====================================
# GET HR INTERVIEW QUESTIONS
# =====================================

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
        "total_questions": len(questions),
        "questions": questions
    }


# =====================================
# SUBMIT HR INTERVIEW
# =====================================

@router.post("/hr/submit")
def submit_hr(
    test: HRAnswers,
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

    if len(test.answers) != 5:
        raise HTTPException(
            status_code=400,
            detail="Please answer all 5 HR questions."
        )

    # Step 3: Calculate score
    # Current logic awards 20 marks per submitted answer.

    score = len(test.answers) * 20

    status = "Passed" if score >= 60 else "Failed"

    # Step 4: Find recruitment progress

    progress = db.query(RecruitmentProgress).filter(
        RecruitmentProgress.candidate_id == candidate.id
    ).first()

    if not progress:
        raise HTTPException(
            status_code=404,
            detail="Recruitment progress not found."
        )

    # Step 5: Update recruitment progress

    progress.hr_status = status

    if status == "Passed":

        progress.current_stage = "selection"
        progress.selection_status = "Pending"

    else:

        progress.current_stage = "hr"
        progress.selection_status = "Pending"

    # Step 6: Save to PostgreSQL

    try:

        db.commit()
        db.refresh(progress)

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to save HR interview result."
        )

    # Step 7: Return result

    return {
        "message": "HR Interview Completed",
        "candidate_id": candidate.id,
        "candidate_name": candidate.name,
        "hr_score": score,
        "total_marks": 100,
        "status": status,
        "next_stage": (
            "selection" if status == "Passed"
            else "Not eligible"
        )
    }