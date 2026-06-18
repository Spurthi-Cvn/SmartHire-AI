from fastapi import APIRouter
from app.schemas import AptitudeAnswers

router = APIRouter()


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
            "options": [
                "EC2",
                "RDS",
                "S3",
                "IAM"
            ]
        },
        {
            "id": 3,
            "question": "Which tool is used for Continuous Integration and Continuous Deployment?",
            "options": [
                "Docker",
                "Jenkins",
                "Git",
                "Linux"
            ]
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
            "options": [
                "CloudWatch",
                "IAM",
                "Route53",
                "Lambda"
            ]
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
            "options": [
                "pwd",
                "mkdir",
                "ls",
                "cd"
            ]
        }
    ]

    return {
        "test_name": "AWS DevOps Aptitude Round",
        "questions": questions
    }


@router.post("/aptitude/submit")
def submit_aptitude(test: AptitudeAnswers):

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

    score = 0

    for question_id, answer in test.answers.items():

        if correct_answers.get(question_id) == answer:
            score += 1

    percentage = round(
        (score / len(correct_answers)) * 100,
        2
    )

    status = "Passed" if percentage >= 60 else "Failed"

    return {
        "score": score,
        "percentage": percentage,
        "status": status
    }