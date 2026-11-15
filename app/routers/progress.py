from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Candidate, RecruitmentProgress

router = APIRouter()


@router.get("/candidate/{candidate_id}/progress")
def get_candidate_progress(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    # Find candidate
    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    # Find recruitment progress
    progress = db.query(RecruitmentProgress).filter(
        RecruitmentProgress.candidate_id == candidate_id
    ).first()

    # Create initial progress if it doesn't exist
    if not progress:

        progress = RecruitmentProgress(
            candidate_id=candidate_id
        )

        db.add(progress)
        db.commit()
        db.refresh(progress)

    return {
        "candidate_id": candidate_id,
        "candidate_name": candidate.name,
        "current_stage": progress.current_stage,
        "ats_status": progress.ats_status,
        "aptitude_status": progress.aptitude_status,
        "technical_status": progress.technical_status,
        "communication_status": progress.communication_status,
        "hr_status": progress.hr_status,
        "selection_status": progress.selection_status,
        "offer_status": progress.offer_status,
        "onboarding_status": progress.onboarding_status
    }