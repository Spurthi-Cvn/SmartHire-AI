import os
from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from reportlab.pdfgen import canvas

from app.database import get_db
from app.models import Candidate, RecruitmentProgress

router = APIRouter()


@router.get("/offer-letter/{candidate_id}")
def generate_offer_letter(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    # Step 1: Check candidate
    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    # Step 2: Check recruitment progress
    progress = db.query(RecruitmentProgress).filter(
        RecruitmentProgress.candidate_id == candidate_id
    ).first()

    if not progress:
        raise HTTPException(
            status_code=404,
            detail="Recruitment progress not found"
        )

    # Step 3: Check selection status
    if progress.selection_status != "Selected":
        raise HTTPException(
            status_code=400,
            detail="Candidate is not selected for the job"
        )

    # Step 4: Create offer letter folder
    os.makedirs("offers", exist_ok=True)

    file_name = f"offer_letter_{candidate_id}.pdf"
    file_path = os.path.join("offers", file_name)

    # Step 5: Generate PDF
    pdf = canvas.Canvas(file_path)

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(120, 800, "ASHHH TECHNOLOGIES PVT. LTD.")

    pdf.setFont("Helvetica", 11)
    pdf.drawString(170, 780, "Innovating Cloud. Empowering Careers.")

    pdf.line(50, 770, 550, 770)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(220, 735, "OFFER LETTER")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(50, 700, "Reference No: AT/HR/2026/1001")
    pdf.drawString(380, 700, f"Date: {date.today()}")

    pdf.drawString(50, 660, "To,")
    pdf.drawString(50, 640, f"Ms. {candidate.name}")

    pdf.drawString(
        50, 600,
        "Subject: Offer of Employment - AWS DevOps Engineer"
    )

    pdf.drawString(50, 560, f"Dear {candidate.name},")

    pdf.drawString(
        50, 530,
        "We are delighted to offer you the position of"
    )

    pdf.drawString(
        50, 510,
        "AWS DevOps Engineer at Ashhh Technologies Pvt. Ltd."
    )

    pdf.drawString(
        50, 480,
        "Based on your successful completion of our recruitment"
    )

    pdf.drawString(
        50, 460,
        "process, we are pleased to welcome you to our team."
    )

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, 410, "Employment Details")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(70, 380, f"Employee Name : {candidate.name}")
    pdf.drawString(70, 360, "Designation   : AWS DevOps Engineer")
    pdf.drawString(70, 340, "Department    : Cloud & DevOps")
    pdf.drawString(70, 320, "Work Location : Bengaluru, Karnataka")
    pdf.drawString(70, 300, "Joining Date  : To be confirmed")
    pdf.drawString(70, 280, "Annual CTC    : Rs. 4,50,000")

    pdf.drawString(
        50, 230,
        "This offer is subject to successful document verification"
    )

    pdf.drawString(
        50, 210,
        "and completion of onboarding formalities."
    )

    pdf.drawString(
        50, 180,
        "We look forward to your valuable contribution and wish"
    )

    pdf.drawString(
        50, 160,
        "you a successful career with Ashhh Technologies."
    )

    pdf.drawString(50, 110, "Yours Sincerely,")
    pdf.drawString(50, 80, "Ananya Rao")
    pdf.drawString(50, 60, "Director - Human Resources")
    pdf.drawString(50, 40, "Ashhh Technologies Pvt. Ltd.")

    pdf.save()

    # Step 6: Update recruitment progress
    progress.offer_status = "Offered"
    progress.onboarding_status = "Pending"
    progress.current_stage = "onboarding"

    try:
        db.commit()
        db.refresh(progress)
    except Exception:
        db.rollback()
        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=500,
            detail="Unable to update offer status"
        )

    # Step 7: Return PDF
    return FileResponse(
        path=file_path,
        filename=file_name,
        media_type="application/pdf"
    )