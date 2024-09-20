provider "aws" {
  region = "us-west-2"
}

module "s3" {
  source = "../modules/s3"
}

module "lambda" {
  source = "../modules/lambda"
}

module "dynamodb" {
  source = "../modules/dynamodb"
}

module "api_gateway" {
  source = "../modules/api_gateway"
}

module "bedrock" {
  source = "../modules/bedrock"
}

module "opensearch" {
  source = "../modules/opensearch"
}
