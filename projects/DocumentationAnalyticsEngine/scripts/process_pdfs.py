import os
import boto3
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
from botocore.exceptions import ClientError

# Load environment variables
load_dotenv()

# AWS Configuration
aws_profile = os.getenv('AWS_PROFILE')
aws_region = os.getenv('AWS_REGION')
s3_bucket_name = os.getenv('S3_BUCKET_NAME')
output_directory = os.getenv('OUTPUT_DIRECTORY')

# Initialize AWS clients
session = boto3.Session(profile_name=aws_profile, region_name=aws_region)
s3 = session.client('s3')
textract = session.client('textract')
comprehend = session.client('comprehend')

def upload_file_to_s3(file_path, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)
    try:
        s3.upload_file(file_path, s3_bucket_name, object_name)
    except ClientError as e:
        print(f"Error uploading {file_path} to S3: {e}")
        return False
    return True

def extract_text_from_pdf(s3_object_name):
    response = textract.start_document_text_detection(
        DocumentLocation={'S3Object': {'Bucket': s3_bucket_name, 'Name': s3_object_name}}
    )
    job_id = response['JobId']

    # Wait for the job to complete
    while True:
        response = textract.get_document_text_detection(JobId=job_id)
        status = response['JobStatus']
        if status in ['SUCCEEDED', 'FAILED']:
            break

    if status == 'SUCCEEDED':
        text = ""
        for item in response['Blocks']:
            if item['BlockType'] == 'LINE':
                text += item['Text'] + "\n"
        return text
    else:
        print(f"Textract job failed for {s3_object_name}")
        return None

def analyze_entities(text):
    response = comprehend.detect_entities(Text=text, LanguageCode='en')
    return response['Entities']

def process_file(file_path):
    file_name = os.path.basename(file_path)
    print(f"Processing {file_name}...")

    # Upload file to S3
    if not upload_file_to_s3(file_path):
        return

    # Extract text from PDF
    text = extract_text_from_pdf(file_name)
    if not text:
        return

    # Analyze entities
    entities = analyze_entities(text)

    # Save results
    output_file = os.path.join(output_directory, f"{file_name}_analysis.json")
    with open(output_file, 'w') as f:
        json.dump(entities, f, indent=2)

    print(f"Analysis complete for {file_name}")

def main():
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    pdf_files = [f for f in os.listdir('data/us-v-google-2023') if f.endswith('.pdf')]

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_file, os.path.join('data/us-v-google-2023', pdf)) for pdf in pdf_files]
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()
