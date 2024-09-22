# Terraform Repository Structure for Code Librarian

Here's the proposed directory structure for your Terraform repository:

```
code-librarian-infra/
├── environments/
│   ├── lcl/
│   │   ├── us-east-1/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   └── terraform.tfvars
│   │   └── us-west-2/
│   │       ├── main.tf
│   │       ├── variables.tf
│   │       └── terraform.tfvars
│   ├── dev/
│   │   ├── us-east-1/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   └── terraform.tfvars
│   │   └── us-west-2/
│   │       ├── main.tf
│   │       ├── variables.tf
│   │       └── terraform.tfvars
│   ├── qat/
│   │   ├── us-east-1/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   └── terraform.tfvars
│   │   └── us-west-2/
│   │       ├── main.tf
│   │       ├── variables.tf
│   │       └── terraform.tfvars
│   └── prd/
│       ├── us-east-1/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   └── terraform.tfvars
│       └── us-west-2/
│           ├── main.tf
│           ├── variables.tf
│           └── terraform.tfvars
├── modules/
│   ├── api_gateway/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── lambda/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── dynamodb/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── sns/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── sqs/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── opensearch/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── .gitignore
├── README.md
└── versions.tf
```

Now, let's look at the content of some key files:

1. `environments/lcl/us-east-1/main.tf`:

```hcl
provider "aws" {
  region = "us-east-1"
}

module "api_gateway" {
  source = "../../../modules/api_gateway"
  # Add necessary variables
}

module "lambda" {
  source = "../../../modules/lambda"
  # Add necessary variables
}

# Add other modules as needed

terraform {
  backend "s3" {
    bucket = "code-librarian-tfstate-lcl-us-east-1"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }
}
```

2. `environments/lcl/us-east-1/variables.tf`:

```hcl
variable "environment" {
  description = "The environment (lcl, dev, qat, prd)"
  default     = "lcl"
}

variable "region" {
  description = "The AWS region"
  default     = "us-east-1"
}

# Add other variables as needed
```

3. `environments/lcl/us-east-1/terraform.tfvars`:

```hcl
environment = "lcl"
region      = "us-east-1"
# Add other variable values specific to lcl and us-east-1
```

4. `modules/api_gateway/main.tf`:

```hcl
resource "aws_api_gateway_rest_api" "code_librarian_api" {
  name        = "code-librarian-api-${var.environment}"
  description = "Code Librarian API for ${var.environment}"
}

# Add other API Gateway resources and methods
```

5. `modules/api_gateway/variables.tf`:

```hcl
variable "environment" {
  description = "The environment (lcl, dev, qat, prd)"
}

# Add other variables as needed
```

6. `modules/api_gateway/outputs.tf`:

```hcl
output "api_gateway_id" {
  description = "The ID of the API Gateway"
  value       = aws_api_gateway_rest_api.code_librarian_api.id
}

# Add other outputs as needed
```

7. `versions.tf` (in the root directory):

```hcl
terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}
```

8. `.gitignore`:

```
# Local .terraform directories
**/.terraform/*

# .tfstate files
*.tfstate
*.tfstate.*

# Crash log files
crash.log
crash.*.log

# Exclude all .tfvars files, which are likely to contain sensitive data
*.tfvars
*.tfvars.json

# Ignore override files as they are usually used to override resources locally and so
# are not checked in
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# Ignore CLI configuration files
.terraformrc
terraform.rc
```

This structure allows you to:

1. Maintain separate configurations for each environment and region.
2. Reuse modules across environments and regions.
3. Keep sensitive information out of version control (using .gitignore).
4. Use remote state storage with S3 backends for each environment/region combination.

To use this structure:

1. Navigate to the specific environment and region directory (e.g., `environments/dev/us-east-1/`).
2. Run `terraform init` to initialize the Terraform working directory.
3. Run `terraform plan` to see the execution plan.
4. Run `terraform apply` to apply the changes.

Remember to replace placeholder values and add actual resource configurations as needed for your Code Librarian project.
