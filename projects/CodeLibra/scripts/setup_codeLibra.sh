#!/bin/bash

# CodeLibra Project Setup Script

# Check if we are already in the CodeLibra directory
if [ "${PWD##*/}" != "CodeLibra" ]; then
  # Create the CodeLibra directory if it doesn't exist, then cd into it
  if [ ! -d "CodeLibra" ]; then
    echo "Creating CodeLibra directory..."
    mkdir CodeLibra
  fi
  cd CodeLibra || exit
else
  echo "Already in CodeLibra directory."
fi

# Set up code structure
mkdir -p src/{api,lambda,frontend}
touch src/api/app.py
touch src/lambda/{analyzer,rag_query}.py
touch src/frontend/{index.html,app.js,styles.css}

# Set up infrastructure as code
mkdir -p infra/{terraform,cdk}
touch infra/terraform/{main.tf,variables.tf,outputs.tf}
touch infra/cdk/{app.py,stack.py}

# Set up monitoring and observability
mkdir -p monitoring
touch monitoring/{cloudwatch_dashboard.json,prometheus_config.yml}

# Set up documentation
mkdir -p docs
touch docs/{README.md,architecture.md,api_spec.md}

# Set up RFCs
mkdir -p rfcs
touch rfcs/{001-monitoring-observability.md,002-escalation-recovery-failover.md,003-rag-knowledge-bases-bedrock.md}

# Set up tests
mkdir -p tests/{unit,integration}
touch tests/unit/{test_api.py,test_lambda.py}
touch tests/integration/test_rag.py

# Set up CI/CD
touch .github/workflows/ci_cd.yml

# Set up configuration files
touch {.gitignore,.env.example,requirements.txt,package.json}

# Set up Makefile for common commands
touch Makefile

echo "CodeLibra project structure has been set up!"
