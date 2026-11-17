from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models import Candidate, RecruitmentProgress

router = APIRouter()


class JoiningCompletion(BaseModel):
    candidate_id: int


@router.get("/joining/{candidate_id}")
def joining_status(candidate_id: int, db: Session = Depends(get_db)):

    # Check candidate
    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    # Check recruitment progress
    progress = db.query(RecruitmentProgress).filter(
        RecruitmentProgress.candidate_id == candidate_id
    ).first()

    if not progress:
        raise HTTPException(status_code=404, detail="Recruitment progress not found")

    # Check offer status
    if progress.offer_status != "Offered":
        raise HTTPException(
            status_code=400,
            detail="Offer letter has not been generated"
        )

    return {
        "employee_id": f"ASH{candidate.id:04d}",
        "candidate_id": candidate.id,
        "candidate_name": candidate.name,
        "designation": "AWS DevOps Engineer",
        "department": "Cloud & DevOps",
        "joining_date": "To be confirmed",
        "offer_status": progress.offer_status,
        "onboarding_status": progress.onboarding_status
    }


@router.post("/joining/complete")
def complete_joining(
    data: JoiningCompletion,
    db: Session = Depends(get_db)
):

    candidate = db.query(Candidate).filter(
        Candidate.id == data.candidate_id
    ).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    progress = db.query(RecruitmentProgress).filter(
        RecruitmentProgress.candidate_id == data.candidate_id
    ).first()

    if not progress:
        raise HTTPException(status_code=404, detail="Recruitment progress not found")

    if progress.offer_status != "Offered":
        raise HTTPException(
            status_code=400,
            detail="Candidate must receive an offer before onboarding"
        )

    progress.onboarding_status = "Completed"
    progress.current_stage = "completed"

    try:
        db.commit()
        db.refresh(progress)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Unable to update onboarding status"
        )

    return {
        "message": "Onboarding Completed Successfully",
        "employee_id": f"ASH{candidate.id:04d}",
        "candidate_id": candidate.id,
        "candidate_name": candidate.name,
        "onboarding_status": progress.onboarding_status,
        "recruitment_status": "Completed"
    }