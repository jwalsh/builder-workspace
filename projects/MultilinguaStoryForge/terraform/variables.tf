# variables.tf
variable "environment" {
  description = "Deployment environment (lcl, dev, prd)"
  type        = string
}

variable "primary_region" {
  description = "Primary AWS region"
  type        = string
  default     = "us-east-1"
}

variable "secondary_region" {
  description = "Secondary AWS region (for prd environment)"
  type        = string
  default     = "us-west-2"
}
