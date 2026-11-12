import boto3
from botocore.exceptions import ClientError

# AWS configuration
AWS_PROFILE = "smarthire-dev"
AWS_REGION = "ap-south-1"
BUCKET_NAME = "smarthire-ai-resumes-2026"

# Connect to AWS using the local CLI profile
session = boto3.Session(
    profile_name=AWS_PROFILE,
    region_name=AWS_REGION
)

# Create S3 client
s3_client = session.client("s3")


def test_s3_connection():
    try:
        response = s3_client.head_bucket(
            Bucket=BUCKET_NAME
        )

        print("Successfully connected to Amazon S3!")
        print(f"Bucket: {BUCKET_NAME}")

        return True

    except ClientError as error:
        print("S3 connection failed:")
        print(error)

        return False


if __name__ == "__main__":
    test_s3_connection()
def upload_file_to_s3(file_path, object_key):
    try:
        s3_client.upload_file(
            file_path,
            BUCKET_NAME,
            object_key
        )

        print("Resume uploaded successfully to S3!")

        return True

    except ClientError as error:
        print("S3 upload failed:", error)

        return False