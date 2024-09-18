# RFC 002: Secrets Management

## Introduction

This RFC proposes a flexible approach to secrets management that works across different environments, including local development, Docker, Replit, and AWS.

## Secrets Management Approach

### Local Development and Docker

Create a `secrets.json` file:

```json
{
  "GOOGLE_AI_API_KEY": "your_google_ai_api_key_here",
  "ANTHROPIC_API_KEY": "your_anthropic_api_key_here",
  "GITHUB_TOKEN": "your_github_token_here",
  "OLLAMA_API_BASE_URL": "http://localhost:11434",
  "AWS_ACCESS_KEY_ID": "your_aws_access_key_id_here",
  "AWS_SECRET_ACCESS_KEY": "your_aws_secret_access_key_here",
  "OPENAI_API_KEY": "your_openai_api_key_here"
}
```

Mount this file in Docker Compose:

```yaml
volumes:
  - ./secrets.json:/app/secrets.json
```

### Other Environments (e.g., Replit, AWS)

For environments like Replit or AWS, we'll need to adapt our secrets management:

#### Replit
Use Replit's built-in Secrets management. Update our code to check for environment variables first:

```python
import os
import json

def load_secrets():
    if os.path.exists('secrets.json'):
        with open('secrets.json') as f:
            return json.load(f)
    else:
        return {
            "GOOGLE_AI_API_KEY": os.getenv("GOOGLE_AI_API_KEY"),
            "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
            "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN"),
            "OLLAMA_API_BASE_URL": os.getenv("OLLAMA_API_BASE_URL", "http://localhost:11434"),
            "AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID"),
            "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY"),
            "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
        }

secrets = load_secrets()
```

#### AWS
For AWS, we can use AWS Secrets Manager with a boto3 script:

```python
import boto3
import json
from botocore.exceptions import ClientError

def get_aws_secret(secret_name, region_name="us-west-2"):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e
    else:
        if 'SecretString' in get_secret_value_response:
            return json.loads(get_secret_value_response['SecretString'])

# Usage
aws_secrets = get_aws_secret("your_secret_name")
```

### .envrc for direnv (local development)

To support direnv for local development, create a `.envrc` file:

```bash
export GOOGLE_AI_API_KEY="your_google_ai_api_key_here"
export ANTHROPIC_API_KEY="your_anthropic_api_key_here"
export GITHUB_TOKEN="your_github_token_here"
export OLLAMA_API_BASE_URL="http://localhost:11434"
export AWS_ACCESS_KEY_ID="your_aws_access_key_id_here"
export AWS_SECRET_ACCESS_KEY="your_aws_secret_access_key_here"
export OPENAI_API_KEY="your_openai_api_key_here"
```

## Implementation

1. Create `secrets-example.json` and add `secrets.json` to `.gitignore`.
2. Update `project_manager.py` to use the `load_secrets()` function.
3. For AWS deployments, include `aws_secrets.py` and update `project_manager.py` to use it when in an AWS environment.
4. Create a `.envrc-example` file and add `.envrc` to `.gitignore`.
5. Implement a script to convert `secrets.json` to `.envrc` for local development with direnv.

## Next Steps

1. Implement the secrets management approach in the project.
2. Test the setup in various environments (local, Docker, Replit, AWS) to ensure compatibility.
3. Update documentation to reflect the secrets management approach.
4. Create a contributing guide that explains how to set up secrets for development.
