from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models import Job, Candidate, JobApplication

router = APIRouter()


# =====================================
# GET ALL AVAILABLE JOBS
# =====================================

@router.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):

    jobs = db.query(Job).filter(
        Job.status == "Open"
    ).all()

    return {
        "total_jobs": len(jobs),
        "jobs": [
            {
                "id": job.id,
                "title": job.title,
                "department": job.department,
                "location": job.location,
                "employment_type": job.employment_type,
                "experience": job.experience,
                "description": job.description,
                "required_skills": job.required_skills,
                "salary_range": job.salary_range
            }
            for job in jobs
        ]
    }


# =====================================
# GET JOB DETAILS
# =====================================

@router.get("/jobs/{job_id}")
def get_job_details(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = db.query(Job).filter(
        Job.id == job_id,
        Job.status == "Open"
    ).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found or no longer available"
        )

    return {
        "id": job.id,
        "title": job.title,
        "department": job.department,
        "location": job.location,
        "employment_type": job.employment_type,
        "experience": job.experience,
        "description": job.description,
        "required_skills": job.required_skills,
        "salary_range": job.salary_range
    }


# =====================================
# ADD NEW JOB
# =====================================

@router.post("/jobs")
def create_job(
    title: str,
    department: str,
    location: str,
    employment_type: str,
    description: str,
    experience: str = "",
    required_skills: str = "",
    salary_range: str = "",
    db: Session = Depends(get_db)
):

    new_job = Job(
        title=title,
        department=department,
        location=location,
        employment_type=employment_type,
        experience=experience,
        description=description,
        required_skills=required_skills,
        salary_range=salary_range,
        status="Open"
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {
        "message": "Job created successfully",
        "job_id": new_job.id,
        "title": new_job.title
    }


# =====================================
# APPLY FOR A JOB
# =====================================

@router.post("/jobs/{job_id}/apply")
def apply_for_job(
    job_id: int,
    candidate_id: int,
    db: Session = Depends(get_db)
):

    # STEP 1: Check candidate

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found. Please register first."
        )

    # STEP 2: Check job availability

    job = db.query(Job).filter(
        Job.id == job_id,
        Job.status == "Open"
    ).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found or no longer available."
        )

    # STEP 3: Prevent duplicate applications

    existing_application = db.query(JobApplication).filter(
        JobApplication.candidate_id == candidate_id,
        JobApplication.job_id == job_id
    ).first()

    if existing_application:
        raise HTTPException(
            status_code=409,
            detail="You have already applied for this job."
        )

    # STEP 4: Create application

    new_application = JobApplication(
        candidate_id=candidate_id,
        job_id=job_id,
        application_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        application_status="Applied"
    )

    db.add(new_application)

    db.commit()

    db.refresh(new_application)

    # STEP 5: Return confirmation

    return {
        "message": "Job application submitted successfully!",
        "application_id": new_application.id,
        "candidate_id": candidate_id,
        "job_id": job.id,
        "job_title": job.title,
        "application_status": new_application.application_status,
        "application_date": new_application.application_date
    }
    
    # =====================================
# GET CANDIDATE'S APPLICATIONS
# =====================================

@router.get("/my-applications/{candidate_id}")
def get_my_applications(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    # STEP 1: Check candidate

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    # STEP 2: Fetch all candidate applications

    applications = (
        db.query(JobApplication, Job)
        .join(Job, JobApplication.job_id == Job.id)
        .filter(JobApplication.candidate_id == candidate_id)
        .order_by(JobApplication.id.desc())
        .all()
    )

    # STEP 3: Prepare response

    application_list = []

    for application, job in applications:

        application_list.append({
            "application_id": application.id,
            "job_id": job.id,
            "job_title": job.title,
            "department": job.department,
            "location": job.location,
            "employment_type": job.employment_type,
            "experience": job.experience,
            "salary_range": job.salary_range,
            "application_date": application.application_date,
            "application_status": application.application_status
        })

    return {
        "candidate_id": candidate_id,
        "candidate_name": candidate.name,
        "total_applications": len(application_list),
        "applications": application_list
    }