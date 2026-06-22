from fastapi import APIRouter

router = APIRouter()


@router.get("/joining")
def joining_status():

    return {
        "employee_id": "ASH1001",
        "candidate_name": "Spurthi Chavan",
        "designation": "AWS DevOps Engineer",
        "department": "Cloud & DevOps",
        "joining_date": "01-Aug-2026",
        "status": "Joined Successfully"
    }