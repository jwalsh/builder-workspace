#!/bin/bash

# Set your AWS profile and region
export AWS_PROFILE=your_aws_profile
export AWS_REGION=us-west-2

# S3 bucket name where PDFs are uploaded
S3_BUCKET="aif-c01-input"

# DynamoDB table name where insights are stored (if applicable)
DYNAMODB_TABLE="aif-c01-insights"

# Function to check if a PDF exists in S3
check_pdf_in_s3() {
    local pdf_name="$1"
    if aws s3 ls "s3://$S3_BUCKET/$pdf_name" &>/dev/null; then
        echo "✅ PDF $pdf_name exists in S3"
    else
        echo "❌ PDF $pdf_name does not exist in S3"
    fi
}

# Function to check if insights exist for a PDF
check_insights() {
    local pdf_name="$1"
    # Assuming insights are stored with the PDF name as the primary key
    if aws dynamodb get-item \
        --table-name "$DYNAMODB_TABLE" \
        --key "{\"pdf_name\": {\"S\": \"$pdf_name\"}}" \
        --query "Item" \
        --output text &>/dev/null; then
        echo "✅ Insights exist for $pdf_name"
    else
        echo "❌ No insights found for $pdf_name"
    fi
}

# Main validation logic
echo "Starting validation..."

# List of PDFs to check (you can expand this list)
pdfs=(
    "DTX0365.pdf"
    "PTX0014_0.pdf"
    "Demonstrative_A.pdf"
    # Add more PDFs as needed
)

for pdf in "${pdfs[@]}"; do
    echo "Checking $pdf..."
    check_pdf_in_s3 "$pdf"
    check_insights "$pdf"
    echo "---"
done

# Check Comprehend job status (if applicable)
comprehend_job_id="your-comprehend-job-id"
comprehend_status=$(aws comprehend describe-document-classification-job --job-id "$comprehend_job_id" --query "DocumentClassificationJobProperties.JobStatus" --output text)
echo "Comprehend job status: $comprehend_status"

# Check Bedrock model deployment status (if applicable)
bedrock_model_id="your-bedrock-model-id"
bedrock_status=$(aws bedrock-runtime describe-model --model-id "$bedrock_model_id" --query "ModelStatus" --output text)
echo "Bedrock model status: $bedrock_status"

echo "Validation complete."
