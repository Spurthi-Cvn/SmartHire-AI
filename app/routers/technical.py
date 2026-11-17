from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import TechnicalAnswers
from app.database import get_db
from app.models import Candidate, RecruitmentProgress

router = APIRouter()


# =====================================
# GET TECHNICAL INTERVIEW QUESTIONS
# =====================================

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
        "total_questions": len(questions),
        "questions": questions
    }


# =====================================
# SUBMIT TECHNICAL INTERVIEW
# =====================================

@router.post("/technical/submit")
def submit_technical(
    test: TechnicalAnswers,
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
            detail="Please answer all 5 technical questions."
        )

    # Step 3: Calculate score
    # Current scoring: 20 marks for each submitted answer.

    score = len(test.answers) * 20

    status = "Passed" if score >= 60 else "Failed"

    # Step 4: Find recruitment progress

    progress = db.query(RecruitmentProgress).filter(
        RecruitmentProgress.candidate_id == test.candidate_id
    ).first()

    if not progress:

        progress = RecruitmentProgress(
            candidate_id=test.candidate_id
        )

        db.add(progress)

    # Step 5: Update recruitment progress

    progress.technical_status = status

    if status == "Passed":

        progress.current_stage = "communication"
        progress.communication_status = "Pending"

    else:

        progress.current_stage = "technical"
        progress.communication_status = "Locked"

    # Step 6: Save to PostgreSQL

    try:
        db.commit()
        db.refresh(progress)

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Unable to save technical interview result."
        )

    # Step 7: Return result

    return {
        "message": "Technical Interview Completed",
        "candidate_id": candidate.id,
        "candidate_name": candidate.name,
        "technical_score": score,
        "total_marks": 100,
        "status": status,
        "next_stage": (
            "communication" if status == "Passed"
            else "Not eligible"
        )
    }