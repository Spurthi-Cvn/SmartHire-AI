from fastapi import APIRouter

router = APIRouter()

@router.get("/shortlist")
def shortlist_candidate():

    candidate_score = 80

    if candidate_score >= 70:
        status = "Shortlisted"
    else:
        status = "Rejected"

    return {
        "candidate_score": candidate_score,
        "status": status
    }