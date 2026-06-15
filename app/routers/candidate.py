from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import CandidateCreate, CandidateLogin, CandidateUpdate
from app.models import Candidate
from app.database import get_db

router = APIRouter()


@router.post("/register")
def register(
    candidate: CandidateCreate,
    db: Session = Depends(get_db)
):

    new_candidate = Candidate(
        name=candidate.name,
        email=candidate.email,
        phone=candidate.phone,
        password=candidate.password
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    return {
        "message": "Candidate Registered Successfully",
        "candidate_id": new_candidate.id
    }


@router.post("/login")
def login(
    candidate: CandidateLogin,
    db: Session = Depends(get_db)
):

    user = db.query(Candidate).filter(
        Candidate.email == candidate.email
    ).first()

    if not user:
        return {"message": "User not found"}

    if user.password != candidate.password:
        return {"message": "Invalid password"}

    return {
        "message": "Login Successful",
        "candidate_id": user.id
    }


@router.get("/candidate/{candidate_id}")
def get_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        return {
            "message": "Candidate Not Found"
        }

    return {
        "id": candidate.id,
        "name": candidate.name,
        "email": candidate.email,
        "phone": candidate.phone
    }


@router.put("/candidate/{candidate_id}")
def update_candidate(
    candidate_id: int,
    updated_data: CandidateUpdate,
    db: Session = Depends(get_db)
):

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        return {
            "message": "Candidate not found"
        }

    candidate.name = updated_data.name
    candidate.email = updated_data.email
    candidate.phone = updated_data.phone

    db.commit()
    db.refresh(candidate)

    return {
        "message": "Candidate Updated Successfully"
    }
    
@router.delete("/candidate/{candidate_id}")
def delete_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        return {
            "message": "Candidate Not Found"
        }

    db.delete(candidate)
    db.commit()

    return {
        "message": "Candidate Deleted Successfully"
    }