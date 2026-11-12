import os
import boto3

from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
AWS_PROFILE = os.getenv("AWS_PROFILE", "smarthire-dev")
SES_SENDER_EMAIL = os.getenv("SES_SENDER_EMAIL")


def send_application_email(
    recipient_email: str,
    candidate_name: str
):

    session = boto3.Session(
        profile_name=AWS_PROFILE,
        region_name=AWS_REGION
    )

    ses = session.client("ses")

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