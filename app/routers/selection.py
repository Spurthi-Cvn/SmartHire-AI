from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models import Candidate, RecruitmentProgress

router = APIRouter()


class SelectionDecision(BaseModel):
    candidate_id: int
    decision: str


@router.get("/selection/{candidate_id}")
def final_selection(candidate_id: int, db: Session = Depends(get_db)):

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    progress = db.query(RecruitmentProgress).filter(
        RecruitmentProgress.candidate_id == candidate_id
    ).first()

    if not progress:
        raise HTTPException(status_code=404, detail="Recruitment progress not found")

    return {
        "candidate_id": candidate.id,
        "candidate_name": candidate.name,
        "hr_status": progress.hr_status,
        "selection_status": progress.selection_status,
        "next_stage": "Offer Letter Generation"
        if progress.selection_status == "Selected"
        else "Awaiting Selection Decision"
    }


@router.post("/selection/submit")
def submit_selection(
    decision: SelectionDecision,
    db: Session = Depends(get_db)
):

    candidate = db.query(Candidate).filter(
        Candidate.id == decision.candidate_id
    ).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    progress = db.query(RecruitmentProgress).filter(
        RecruitmentProgress.candidate_id == decision.candidate_id
    ).first()

    if not progress:
        raise HTTPException(status_code=404, detail="Recruitment progress not found")

    if progress.hr_status != "Passed":
        raise HTTPException(
            status_code=400,
            detail="Candidate must pass the HR interview first"
        )

    result = decision.decision.strip().capitalize()

    if result not in ["Selected", "Rejected"]:
        raise HTTPException(
            status_code=400,
            detail="Decision must be Selected or Rejected"
        )

    progress.selection_status = result

    if result == "Selected":
        progress.current_stage = "offer"
        progress.offer_status = "Pending"
    else:
        progress.current_stage = "selection"
        progress.offer_status = "Locked"

    try:
        db.commit()
        db.refresh(progress)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Unable to save selection decision"
        )

    return {
        "message": "Final Selection Completed",
        "candidate_id": candidate.id,
        "candidate_name": candidate.name,
        "selection_status": result,
        "next_stage": "offer" if result == "Selected" else "Not eligible"
    }