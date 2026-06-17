from fastapi import APIRouter

router = APIRouter()

@router.get("/job/aws-devops")
def aws_devops_job():

    return {
        "role": "AWS DevOps Engineer",
        "required_skills": [
            "AWS",
            "Docker",
            "Kubernetes",
            "Terraform",
            "Jenkins",
            "Git",
            "Linux"
        ]
    }