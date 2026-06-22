from fastapi import APIRouter
from reportlab.pdfgen import canvas
from fastapi.responses import FileResponse
router = APIRouter()


@router.get("/offer-letter")
def generate_offer_letter():

    file_name = "offer_letter.pdf"

    pdf = canvas.Canvas(file_name)
    
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(120, 800, "ASHHH TECHNOLOGIES PVT. LTD.")

    pdf.setFont("Helvetica", 11)
    pdf.drawString(170, 780, "Innovating Cloud. Empowering Careers.")

    pdf.line(50, 770, 550, 770)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(220, 735, "OFFER LETTER")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(50, 700, "Reference No: AT/HR/2026/1001")
    pdf.drawString(380, 700, "Date: 22 June 2026")

    pdf.drawString(50, 660, "To,")
    pdf.drawString(50, 640, "Ms. Spurthi Chavan")

    pdf.drawString(
        50,
        600,
        "Subject: Offer of Employment - AWS DevOps Engineer"
    )

    pdf.drawString(50, 560, "Dear Spurthi Chavan,")

    pdf.drawString(
        50,
        530,
        "We are delighted to offer you the position of"
    )

    pdf.drawString(
        50,
        510,
        "AWS DevOps Engineer at Ashhh Technologies Pvt. Ltd."
    )

    pdf.drawString(
        50,
        480,
        "Based on your successful completion of our recruitment"
    )

    pdf.drawString(
        50,
        460,
        "process, we are pleased to welcome you to our team."
    )

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(50, 410, "Employment Details")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(70, 380, "Employee Name : Spurthi Chavan")
    pdf.drawString(70, 360, "Designation   : AWS DevOps Engineer")
    pdf.drawString(70, 340, "Department    : Cloud & DevOps")
    pdf.drawString(70, 320, "Work Location : Bengaluru, Karnataka")
    pdf.drawString(70, 300, "Joining Date  : 01 August 2026")
    pdf.drawString(70, 280, "Annual CTC    : Rs. 4,50,000")

    pdf.drawString(
        50,
        230,
        "This offer is subject to successful document verification"
    )

    pdf.drawString(
        50,
        210,
        "and completion of onboarding formalities."
    )

    pdf.drawString(
        50,
        180,
        "We look forward to your valuable contribution and wish"
    )

    pdf.drawString(
        50,
        160,
        "you a successful career with Ashhh Technologies."
    )

    pdf.drawString(50, 110, "Yours Sincerely,")

    pdf.drawString(50, 80, "Ananya Rao")
    pdf.drawString(50, 60, "Director - Human Resources")
    pdf.drawString(50, 40, "Ashhh Technologies Pvt. Ltd.")
    
    from fastapi.responses import FileResponse
    
    pdf.save()

    return FileResponse(
        path=file_name,
        filename="offer_letter.pdf",
        media_type="application/pdf"
    )