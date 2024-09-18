# main.tf
provider "aws" {
  region = var.primary_region
  alias  = "primary"
}

provider "aws" {
  region = var.secondary_region
  alias  = "secondary"
}

# Global resources
resource "aws_route53_zone" "global_zone" {
  provider = aws.primary
  name     = "example.com"
}

resource "aws_acm_certificate" "global_certificate" {
  provider          = aws.primary
  domain_name       = "example.com"
  validation_method = "DNS"
}

resource "aws_cloudfront_distribution" "global_cdn" {
  # ... CloudFront configuration ...
}

# Primary region resources
module "primary_region" {
  source    = "./modules/region"
  providers = {
    aws = aws.primary
  }
  environment      = var.environment
  region           = var.primary_region
  is_primary       = true
  route53_zone_id  = aws_route53_zone.global_zone.id
  certificate_arn  = aws_acm_certificate.global_certificate.arn
}

# Secondary region resources (only for prd environment)
module "secondary_region" {
  count     = var.environment == "prd" ? 1 : 0
  source    = "./modules/region"
  providers = {
    aws = aws.secondary
  }
  environment      = var.environment
  region           = var.secondary_region
  is_primary       = false
  route53_zone_id  = aws_route53_zone.global_zone.id
  certificate_arn  = aws_acm_certificate.global_certificate.arn
}

# modules/region/main.tf
resource "aws_api_gateway_rest_api" "api" {
  name        = "${var.environment}-${var.region}-api"
  description = "API for ${var.environment} in ${var.region}"
}

resource "aws_lambda_function" "text_analysis" {
  filename      = "text_analysis.zip"
  function_name = "${var.environment}-${var.region}-text-analysis"
  handler       = "index.handler"
  runtime       = "python3.8"
  role          = aws_iam_role.lambda_exec.arn
}

# Similar resources for translation, vocabulary, and story-generation Lambda functions

resource "aws_dynamodb_table" "global_table" {
  name             = "${var.environment}-${var.region}-global-table"
  billing_mode     = "PAY_PER_REQUEST"
  hash_key         = "id"
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  attribute {
    name = "id"
    type = "S"
  }

  replica {
    region_name = var.is_primary ? var.secondary_region : var.primary_region
  }
}

resource "aws_s3_bucket" "storage" {
  bucket = "${var.environment}-${var.region}-storage"
}

resource "aws_sqs_queue" "text_analysis_queue" {
  name = "${var.environment}-${var.region}-text-analysis-queue"
}

# Similar resources for translation, vocabulary, and story-generation SQS queues

resource "aws_cloudwatch_log_group" "api_logs" {
  name = "/aws/apigateway/${aws_api_gateway_rest_api.api.name}"
}

resource "aws_cloudwatch_metric_alarm" "api_errors" {
  alarm_name          = "${var.environment}-${var.region}-api-errors"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "1"
  metric_name         = "5XXError"
  namespace           = "AWS/ApiGateway"
  period              = "60"
  statistic           = "Sum"
  threshold           = "5"
  alarm_description   = "This metric monitors API Gateway 5XX errors"
  alarm_actions       = [aws_sns_topic.alerts.arn]
  dimensions = {
    ApiName = aws_api_gateway_rest_api.api.name
  }
}

resource "aws_cognito_user_pool" "pool" {
  name = "${var.environment}-${var.region}-user-pool"
}

resource "aws_cognito_identity_pool" "pool" {
  identity_pool_name               = "${var.environment}-${var.region}-identity-pool"
  allow_unauthenticated_identities = false
}
