from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import CandidateCreate, CandidateLogin, CandidateUpdate
from app.models import Candidate
from app.database import get_db

from app.services.email_service import send_application_email

router = APIRouter()


# =========================
# CANDIDATE REGISTRATION
# =========================

@router.post("/register")
def register(
    candidate: CandidateCreate,
    db: Session = Depends(get_db)
):

    # 1. Check duplicate email

    existing_candidate = db.query(Candidate).filter(
        Candidate.email == candidate.email
    ).first()

    if existing_candidate:
        raise HTTPException(
            status_code=409,
            detail="Email already registered. Please login."
        )

    # 2. Create candidate

    new_candidate = Candidate(
        name=candidate.name,
        email=candidate.email,
        phone=candidate.phone,
        password=candidate.password
    )

    # 3. Save candidate in PostgreSQL

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    # 4. Send application confirmation email

    email_result = send_application_email(
        recipient_email=new_candidate.email,
        candidate_name=new_candidate.name
    )

    # 5. Return registration response

    return {
        "message": "Candidate Registered Successfully",
        "candidate_id": new_candidate.id,
        "email_status": (
            "Email Sent Successfully"
            if email_result["success"]
            else "Registration successful, but email could not be sent"
        ),
        "email_message": email_result.get("message")
    }


# =========================
# CANDIDATE LOGIN
# =========================

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


# =========================
# GET CANDIDATE
# =========================

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


# =========================
# UPDATE CANDIDATE
# =========================

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


# =========================
# DELETE CANDIDATE
# =========================

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