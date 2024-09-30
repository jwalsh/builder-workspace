#!/bin/bash

# SmartContractAnalyzer Project Setup Script

set -e

# Function to create a directory if it doesn't exist
create_directory() {
    if [ ! -d "$1" ]; then
        mkdir -p "$1"
        echo "Created directory: $1"
    else
        echo "Directory already exists: $1"
    fi
}

# Function to create a file with content if it doesn't exist or is empty
create_file_with_content() {
    if [ ! -f "$1" ] || [ ! -s "$1" ]; then
        cat << EOF > "$1"
$2
EOF
        echo "Created/Updated file: $1"
    else
        echo "File already exists and is not empty: $1"
    fi
}

# Create project root directory
#create_directory "SmartContractAnalyzer"
# cd SmartContractAnalyzer

# Create directories for each service
for service in frontend api-gateway smart-contract-parser analysis-engine legal-compliance vulnerability-scanner report-generator; do
    create_directory "$service"
done

# Create common directories
for dir in docs config scripts tests; do
    create_directory "$dir"
done

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    git init
    echo "Initialized git repository"
else
    echo "Git repository already initialized"
fi

# Create README.md
create_file_with_content "README.md" "# SmartContractAnalyzer

A tool that automatically analyzes and audits smart contracts for legal compliance and potential vulnerabilities.

## Project Structure

- \`frontend/\`: React with Next.js frontend application
- \`api-gateway/\`: NestJS API Gateway service
- \`smart-contract-parser/\`: Smart Contract Parser service
- \`analysis-engine/\`: Analysis Engine service
- \`legal-compliance/\`: Legal Compliance service
- \`vulnerability-scanner/\`: Vulnerability Scanner service
- \`report-generator/\`: Report Generator service
- \`docs/\`: Project documentation
- \`config/\`: Configuration files
- \`scripts/\`: Utility scripts
- \`tests/\`: End-to-end and integration tests

## Getting Started

1. Clone the repository
2. Install dependencies for each service
3. Set up the development environment
4. Run the services

For detailed instructions, see the [Development Guide](docs/development-guide.md).

## Documentation

- [System Architecture](docs/system-architecture.md)
- [API Documentation](docs/api-documentation.md)
- [Deployment Guide](docs/deployment-guide.md)

## License

[MIT License](LICENSE)"

# Create basic documentation files
for doc in system-architecture api-documentation deployment-guide development-guide; do
    create_file_with_content "docs/$doc.md" "# $doc\n\nTODO: Add content for $doc"
done

# Create docker-compose.yml for local development
create_file_with_content "docker-compose.yml" "version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - \"3000:3000\"

  api-gateway:
    build: ./api-gateway
    ports:
      - \"4000:4000\"

  smart-contract-parser:
    build: ./smart-contract-parser
    ports:
      - \"4001:4001\"

  analysis-engine:
    build: ./analysis-engine
    ports:
      - \"4002:4002\"

  legal-compliance:
    build: ./legal-compliance
    ports:
      - \"4003:4003\"

  vulnerability-scanner:
    build: ./vulnerability-scanner
    ports:
      - \"4004:4004\"

  report-generator:
    build: ./report-generator
    ports:
      - \"4005:4005\"

  postgres:
    image: postgres:13
    environment:
      POSTGRES_DB: smartcontractanalyzer
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - \"5672:5672\"
      - \"15672:15672\"

volumes:
  postgres_data:"

# Create .gitignore
create_file_with_content ".gitignore" "# Dependencies
node_modules/

# Build outputs
dist/
build/

# Environment variables
.env
.env.local

# IDE files
.vscode/
.idea/

# Logs
*.log

# OS files
.DS_Store
Thumbs.db

# Test coverage
coverage/

# Temporary files
*.tmp
*.swp"

# Create Dockerfile template
create_file_with_content "Dockerfile.template" "FROM node:14-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci --only=production

COPY . .

RUN npm run build

CMD [\"npm\", \"start\"]"

# Create basic package.json for each service
for service in frontend api-gateway smart-contract-parser analysis-engine legal-compliance vulnerability-scanner report-generator; do
    create_directory "$service/src"
    cp Dockerfile.template "$service/Dockerfile"
    create_file_with_content "$service/package.json" "{
  \"name\": \"@smartcontractanalyzer/$service\",
  \"version\": \"1.0.0\",
  \"description\": \"$service for SmartContractAnalyzer\",
  \"main\": \"dist/index.js\",
  \"scripts\": {
    \"build\": \"tsc\",
    \"start\": \"node dist/index.js\",
    \"dev\": \"ts-node-dev src/index.ts\",
    \"test\": \"jest\"
  },
  \"dependencies\": {},
  \"devDependencies\": {
    \"@types/node\": \"^14.14.31\",
    \"typescript\": \"^4.2.2\",
    \"ts-node-dev\": \"^1.1.6\",
    \"jest\": \"^26.6.3\",
    \"@types/jest\": \"^26.0.20\"
  }
}"
done

# Create basic TypeScript configuration
create_file_with_content "tsconfig.json" "{
  \"compilerOptions\": {
    \"target\": \"es2019\",
    \"module\": \"commonjs\",
    \"strict\": true,
    \"esModuleInterop\": true,
    \"skipLibCheck\": true,
    \"forceConsistentCasingInFileNames\": true,
    \"outDir\": \"./dist\",
    \"rootDir\": \"./src\"
  },
  \"include\": [\"src/**/*\"],
  \"exclude\": [\"node_modules\", \"**/*.spec.ts\"]
}"

# Copy TypeScript configuration to each service
for service in api-gateway smart-contract-parser analysis-engine legal-compliance vulnerability-scanner report-generator; do
    cp tsconfig.json "$service/"
done

# Create Next.js configuration for frontend
create_file_with_content "frontend/next.config.js" "module.exports = {
  reactStrictMode: true,
}"

# Create simple REST API example for api-gateway
create_directory "api-gateway/src/controllers"
create_file_with_content "api-gateway/src/controllers/health.controller.ts" "import { Controller, Get } from '@nestjs/common';

@Controller('health')
export class HealthController {
  @Get()
  getHealth(): string {
    return 'OK';
  }
}"

# Create basic GitHub Actions workflow for CI
create_directory ".github/workflows"
create_file_with_content ".github/workflows/ci.yml" "name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [14.x]

    steps:
    - uses: actions/checkout@v2
    - name: Use Node.js \${{ matrix.node-version }}
      uses: actions/setup-node@v2
      with:
        node-version: \${{ matrix.node-version }}
    - run: npm ci
    - run: npm run build --if-present
    - run: npm test"

# Create basic Kubernetes deployment files
create_directory "k8s"
for service in frontend api-gateway smart-contract-parser analysis-engine legal-compliance vulnerability-scanner report-generator; do
    create_file_with_content "k8s/$service-deployment.yaml" "apiVersion: apps/v1
kind: Deployment
metadata:
  name: $service
spec:
  replicas: 1
  selector:
    matchLabels:
      app: $service
  template:
    metadata:
      labels:
        app: $service
    spec:
      containers:
      - name: $service
        image: smartcontractanalyzer/$service:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: $service
spec:
  selector:
    app: $service
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80"
done

# Create Minikube setup script
create_file_with_content "scripts/setup_minikube.sh" "#!/bin/bash

# Start Minikube
minikube start

# Enable ingress addon
minikube addons enable ingress

# Set up local Docker environment to use Minikube's Docker daemon
eval \$(minikube docker-env)

# Build Docker images for each service
for service in frontend api-gateway smart-contract-parser analysis-engine legal-compliance vulnerability-scanner report-generator; do
  docker build -t smartcontractanalyzer/\$service:latest ./\$service
done

# Apply Kubernetes configurations
kubectl apply -f k8s/

# Wait for deployments to be ready
kubectl wait --for=condition=available --timeout=300s deployment --all

# Get Minikube IP
minikube_ip=\$(minikube ip)

echo \"SmartContractAnalyzer is now running on Minikube!\"
echo \"Access the services using the Minikube IP: \$minikube_ip\""

chmod +x scripts/setup_minikube.sh

# Create diagrams directory and files
create_directory "docs/diagrams"
create_file_with_content "docs/diagrams/developer-workflow.mmd" "graph TD
    A[Clone Repository] --> B[Run 'make setup']
    B --> C[Run 'make install']
    C --> D[Run 'make build']
    D --> E[Run 'make test']
    E --> F{All tests pass?}
    F -->|Yes| G[Develop new feature]
    F -->|No| H[Fix failing tests]
    H --> E
    G --> I[Write tests for new feature]
    I --> J[Run 'make test']
    J --> K{All tests pass?}
    K -->|Yes| L[Run 'make run']
    K -->|No| M[Fix failing tests]
    M --> J
    L --> N[Manual testing]
    N --> O{Feature works as expected?}
    O -->|Yes| P[Commit changes]
    O -->|No| Q[Debug and fix issues]
    Q --> L
    P --> R[Push to repository]
    R --> S[Create pull request]
    S --> T[Code review]
    T --> U{Changes requested?}
    U -->|Yes| V[Make requested changes]
    V --> T
    U -->|No| W[Merge pull request]
    W --> X[Run 'make deploy']
    X --> Y[Monitor deployment]"

create_file_with_content "docs/diagrams/system-architecture.mmd" "graph TD
    A[User] --> B[Frontend Service]
    B --> C[API Gateway]
    C --> D[Smart Contract Parser Service]
    C --> E[Analysis Engine Service]
    C --> F[Legal Compliance Service]
    C --> G[Vulnerability Scanner Service]
    C --> H[Report Generator Service]
    D --> I[(Database Service)]
    E --> I
    F --> I
    G --> I
    H --> I
    D <--> J{Message Queue}
    E <--> J
    F <--> J
    G <--> J
    H <--> J
    
    subgraph \"Kubernetes Cluster\"
        B
        C
        D
        E
        F
        G
        H
        I
        J
    end
    
    K[CI/CD Pipeline] --> B
    K --> C
    K --> D
    K --> E
    K --> F
    K --> G
    K --> H
    
    L[Monitoring & Logging] --> B
    L --> C
    L --> D
    L --> E
    L --> F
    L --> G
    L --> H
    L --> I
    L --> J"

echo "Project structure and core documentation have been set up successfully."
echo "To set up Minikube and deploy the project, run: ./scripts/setup_minikube.sh"
