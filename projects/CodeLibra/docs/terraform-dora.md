# First, let's create a new module for DORA metrics

# File: modules/dora_metrics/main.tf
resource "aws_cloudwatch_log_group" "dora_metrics" {
  name = "/dora-metrics/${var.environment}"
  retention_in_days = 90
}

resource "aws_cloudwatch_dashboard" "dora_dashboard" {
  dashboard_name = "DORA-Metrics-${var.environment}"
  dashboard_body = jsonencode({
    widgets = [
      {
        type = "metric"
        x    = 0
        y    = 0
        width = 12
        height = 6
        properties = {
          metrics = [
            ["DORA", "deployment_frequency", "Environment", "${var.environment}"],
            ["DORA", "lead_time_for_changes", "Environment", "${var.environment}"],
            ["DORA", "time_to_restore_service", "Environment", "${var.environment}"],
            ["DORA", "change_failure_rate", "Environment", "${var.environment}"]
          ]
          view = "timeSeries"
          stacked = false
          region = var.region
          title = "DORA Metrics"
        }
      }
    ]
  })
}

# File: modules/dora_metrics/variables.tf
variable "environment" {
  description = "The environment (lcl, dev, qat, prd)"
  type        = string
}

variable "region" {
  description = "The AWS region"
  type        = string
}

# File: modules/dora_metrics/outputs.tf
output "log_group_name" {
  description = "The name of the CloudWatch Log Group for DORA metrics"
  value       = aws_cloudwatch_log_group.dora_metrics.name
}

# Now, let's update our Lambda module to include permissions for logging DORA metrics

# File: modules/lambda/main.tf
# Add this to the existing Lambda role
resource "aws_iam_role_policy_attachment" "lambda_cloudwatch_logs" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

# Add a custom policy for putting metrics
resource "aws_iam_role_policy" "lambda_put_metrics" {
  name = "lambda_put_metrics"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "cloudwatch:PutMetricData",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

# Update the Lambda function to include environment variables for DORA metrics
resource "aws_lambda_function" "code_librarian_lambda" {
  # ... existing configuration ...

  environment {
    variables = {
      DORA_METRICS_NAMESPACE = "DORA"
      ENVIRONMENT            = var.environment
      # ... other environment variables ...
    }
  }
}

# Now, let's update our main configuration to include the DORA metrics module

# File: environments/lcl/us-east-1/main.tf
module "dora_metrics" {
  source = "../../../modules/dora_metrics"
  environment = var.environment
  region      = var.region
}

# Update other modules to pass the DORA metrics log group name
module "lambda" {
  # ... existing configuration ...
  dora_log_group_name = module.dora_metrics.log_group_name
}

# Finally, let's add some Python code to log DORA metrics from our Lambda functions

# This would go in your Lambda function code, not in Terraform
import boto3
import os
from datetime import datetime

cloudwatch = boto3.client('cloudwatch')

def log_dora_metric(metric_name, value):
    cloudwatch.put_metric_data(
        Namespace=os.environ['DORA_METRICS_NAMESPACE'],
        MetricData=[
            {
                'MetricName': metric_name,
                'Dimensions': [
                    {
                        'Name': 'Environment',
                        'Value': os.environ['ENVIRONMENT']
                    },
                ],
                'Value': value,
                'Unit': 'None'
            },
        ]
    )

# Example usage in your Lambda function
def lambda_handler(event, context):
    # ... existing code ...

    # Log deployment frequency (you'd typically do this in your CI/CD pipeline)
    log_dora_metric('deployment_frequency', 1)

    # Log lead time for changes (you'd calculate this based on your development process)
    lead_time = calculate_lead_time()  # You need to implement this
    log_dora_metric('lead_time_for_changes', lead_time)

    # Log time to restore service (you'd log this when an incident is resolved)
    time_to_restore = calculate_time_to_restore()  # You need to implement this
    log_dora_metric('time_to_restore_service', time_to_restore)

    # Log change failure rate (you'd log this when a deployment fails)
    if deployment_failed:
        log_dora_metric('change_failure_rate', 1)
    else:
        log_dora_metric('change_failure_rate', 0)

    # ... rest of your Lambda function ...
