import os
import boto3

from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
AWS_PROFILE = os.getenv("AWS_PROFILE", "smarthire-dev")
SES_SENDER_EMAIL = os.getenv("SES_SENDER_EMAIL")


# =====================================
# CREATE SES CLIENT
# =====================================

def get_ses_client():

    session = boto3.Session(
        profile_name=AWS_PROFILE,
        region_name=AWS_REGION
    )

    return session.client("ses")


# =====================================
# APPLICATION RECEIVED EMAIL
# =====================================

def send_application_email(
    recipient_email: str,
    candidate_name: str
):

    ses = get_ses_client()

    subject = "Application Received - ASHHH Technologies"

    body_text = f"""
Hello {candidate_name},

Thank you for applying to ASHHH Technologies!

We have successfully received your job application.

Our recruitment team will review your resume.
You will receive further updates about your application.

Regards,
ASHHH Technologies
SmartHire AI Recruitment Team
"""

    try:

        response = ses.send_email(
            Source=SES_SENDER_EMAIL,
            Destination={
                "ToAddresses": [recipient_email]
            },
            Message={
                "Subject": {
                    "Data": subject,
                    "Charset": "UTF-8"
                },
                "Body": {
                    "Text": {
                        "Data": body_text,
                        "Charset": "UTF-8"
                    }
                }
            }
        )

        return {
            "success": True,
            "message_id": response["MessageId"]
        }

    except ClientError as error:

        print("SES Error:", error.response["Error"]["Message"])

        return {
            "success": False,
            "message": error.response["Error"]["Message"]
        }


# =====================================
# ATS RESULT EMAIL
# =====================================

def send_ats_result_email(
    recipient_email: str,
    candidate_name: str,
    match_percentage: float
):

    ses = get_ses_client()

    passing_percentage = 70

    if match_percentage >= passing_percentage:

        subject = "Congratulations! Resume Shortlisted - ASHHH Technologies"

        body_text = f"""
Hello {candidate_name},

Congratulations!

Your resume has successfully passed our ATS screening.

Your ATS Match Percentage: {match_percentage}%

Required Passing Percentage: {passing_percentage}%

You have been shortlisted for the next recruitment stage.

Further assessment details will be shared through email.

Regards,
ASHHH Technologies
SmartHire AI Recruitment Team
"""

        status = "Shortlisted"

    else:

        subject = "ATS Screening Update - ASHHH Technologies"

        body_text = f"""
Hello {candidate_name},

Thank you for applying to ASHHH Technologies.

Your ATS Match Percentage: {match_percentage}%

Required Passing Percentage: {passing_percentage}%

Unfortunately, your resume did not meet the required screening criteria.

We appreciate your interest.

Regards,
ASHHH Technologies
SmartHire AI Recruitment Team
"""

        status = "Not Shortlisted"

    try:

        response = ses.send_email(
            Source=SES_SENDER_EMAIL,

            Destination={
                "ToAddresses": [recipient_email]
            },

            Message={
                "Subject": {
                    "Data": subject,
                    "Charset": "UTF-8"
                },

                "Body": {
                    "Text": {
                        "Data": body_text,
                        "Charset": "UTF-8"
                    }
                }
            }
        )

        return {
            "success": True,
            "message_id": response["MessageId"],
            "ats_status": status
        }

    except ClientError as error:

        print("ATS Email Error:", error.response["Error"]["Message"])

        return {
            "success": False,
            "message": error.response["Error"]["Message"]
        }
def send_aptitude_result_email(
    recipient_email: str,
    candidate_name: str,
    score: int,
    total_questions: int,
    percentage: float,
    status: str
):

    ses = get_ses_client()

    subject = f"Aptitude Assessment Result - {status}"

    body_text = f"""
Hello {candidate_name},

Your aptitude assessment has been evaluated successfully.

Assessment: AWS DevOps Aptitude Round

Your Score: {score}/{total_questions}
Percentage: {percentage}%
Result: {status}

Thank you for participating.

Regards,
ASHHH Technologies
SmartHire AI Recruitment Team
"""

    try:
        response = ses.send_email(
            Source=SES_SENDER_EMAIL,
            Destination={
                "ToAddresses": [recipient_email]
            },
            Message={
                "Subject": {
                    "Data": subject,
                    "Charset": "UTF-8"
                },
                "Body": {
                    "Text": {
                        "Data": body_text,
                        "Charset": "UTF-8"
                    }
                }
            }
        )

        return {
            "success": True,
            "message_id": response["MessageId"]
        }

    except ClientError as error:
        print("Aptitude Email Error:", error)

        return {
            "success": False,
            "message": error.response["Error"]["Message"]
        }