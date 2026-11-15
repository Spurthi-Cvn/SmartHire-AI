from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json

from app.schemas import AptitudeAnswers
from app.models import Candidate, AptitudeResult
from app.database import get_db
from app.services.email_service import send_aptitude_result_email

router = APIRouter()


# =====================================
# GET APTITUDE QUESTIONS
# =====================================

@router.get("/aptitude")
def aptitude_test():

    questions = [
        {
            "id": 1,
            "question": "What is AWS EC2 used for?",
            "options": [
                "Compute Service",
                "Database Service",
                "Storage Service",
                "Networking Service"
            ]
        },
        {
            "id": 2,
            "question": "Which AWS service is used for object storage?",
            "options": ["EC2", "RDS", "S3", "IAM"]
        },
        {
            "id": 3,
            "question": "Which tool is used for Continuous Integration and Continuous Deployment?",
            "options": ["Docker", "Jenkins", "Git", "Linux"]
        },
        {
            "id": 4,
            "question": "What is Docker mainly used for?",
            "options": [
                "Containerization",
                "Monitoring",
                "Networking",
                "Database Management"
            ]
        },
        {
            "id": 5,
            "question": "Which Kubernetes object is used to manage Pods?",
            "options": [
                "Deployment",
                "Volume",
                "ConfigMap",
                "Secret"
            ]
        },
        {
            "id": 6,
            "question": "Which command is used to initialize Terraform?",
            "options": [
                "terraform apply",
                "terraform init",
                "terraform plan",
                "terraform destroy"
            ]
        },
        {
            "id": 7,
            "question": "Which Git command is used to upload local changes to GitHub?",
            "options": [
                "git clone",
                "git pull",
                "git push",
                "git status"
            ]
        },
        {
            "id": 8,
            "question": "Which AWS service is used for monitoring resources?",
            "options": ["CloudWatch", "IAM", "Route53", "Lambda"]
        },
        {
            "id": 9,
            "question": "What does IAM stand for in AWS?",
            "options": [
                "Identity and Access Management",
                "Internet Access Manager",
                "Internal Application Monitor",
                "Infrastructure Access Module"
            ]
        },
        {
            "id": 10,
            "question": "Which Linux command is used to list files and directories?",
            "options": ["pwd", "mkdir", "ls", "cd"]
        }
    ]

    return {
        "test_name": "AWS DevOps Aptitude Round",
        "total_questions": len(questions),
        "passing_percentage": 60,
        "questions": questions
    }


# =====================================
# SUBMIT APTITUDE TEST
# =====================================

@router.post("/aptitude/submit")
def submit_aptitude(
    test: AptitudeAnswers,
    db: Session = Depends(get_db)
):

    # Step 1: Validate candidate

    candidate = db.query(Candidate).filter(
        Candidate.id == test.candidate_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )
        # Validate submitted answers

    expected_question_ids = {
        str(i) for i in range(1, 11)
    }

    submitted_question_ids = set(test.answers.keys())

    if submitted_question_ids != expected_question_ids:
        raise HTTPException(
            status_code=400,
            detail="Please answer all 10 questions."
        )

    valid_options = {
        "1": ["Compute Service", "Database Service", "Storage Service", "Networking Service"],
        "2": ["EC2", "RDS", "S3", "IAM"],
        "3": ["Docker", "Jenkins", "Git", "Linux"],
        "4": ["Containerization", "Monitoring", "Networking", "Database Management"],
        "5": ["Deployment", "Volume", "ConfigMap", "Secret"],
        "6": ["terraform apply", "terraform init", "terraform plan", "terraform destroy"],
        "7": ["git clone", "git pull", "git push", "git status"],
        "8": ["CloudWatch", "IAM", "Route53", "Lambda"],
        "9": ["Identity and Access Management", "Internet Access Manager", "Internal Application Monitor", "Infrastructure Access Module"],
        "10": ["pwd", "mkdir", "ls", "cd"]
    }

    for question_id, answer in test.answers.items():
        if answer not in valid_options[question_id]:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid answer for question {question_id}."
            )

    # Step 2: Correct answers

    correct_answers = {
        "1": "Compute Service",
        "2": "S3",
        "3": "Jenkins",
        "4": "Containerization",
        "5": "Deployment",
        "6": "terraform init",
        "7": "git push",
        "8": "CloudWatch",
        "9": "Identity and Access Management",
        "10": "ls"
    }

    # Step 3: Calculate score

    score = 0

    for question_id, answer in test.answers.items():

        if correct_answers.get(question_id) == answer:
            score += 1

    total_questions = len(correct_answers)

    percentage = round(
        (score / total_questions) * 100,
        2
    )

    status = "Passed" if percentage >= 60 else "Failed"

    # Step 4: Save result in PostgreSQL

    result = AptitudeResult(
        candidate_id=candidate.id,
        score=score,
        percentage=str(percentage),
        status=status,
        answers=json.dumps(test.answers)
    )

    db.add(result)
    db.commit()
    db.refresh(result)

        # Step 5: Send aptitude result email

    try:
        email_result = send_aptitude_result_email(
            recipient_email=candidate.email,
            candidate_name=candidate.name,
            score=score,
            total_questions=total_questions,
            percentage=percentage,
            status=status
        )

    except Exception as error:
        print("Aptitude email error:", error)

        email_result = {
            "success": False,
            "message": str(error)
        }

    # Step 6: Return result

    return {
        "message": "Aptitude Assessment Completed",
        "assessment_id": result.id,
        "candidate_id": candidate.id,
        "candidate_name": candidate.name,
        "score": score,
        "total_questions": total_questions,
        "percentage": percentage,
        "status": status,
        "email_sent": email_result.get("success", False),
        "email_message": email_result.get(
            "message",
            "Email sent successfully"
        )
    }