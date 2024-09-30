# SmartContractAnalyzer Makefile

CYAN := \033[0;36m
NC := \033[0m # No Color

.PHONY: help setup install build test run deploy clean

help: ## Display this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(CYAN)%-30s$(NC) %s\n", $$1, $$2}'

setup: ## Set up the project structure and documentation
	@echo "Setting up project structure..."
	@./setup_project.sh

install: ## Install dependencies for all services
	@echo "Installing dependencies..."
	@for service in frontend api-gateway smart-contract-parser analysis-engine legal-compliance vulnerability-scanner report-generator; do \
		cd $$service && npm install && cd ..; \
	done

build: ## Build all services
	@echo "Building services..."
	@for service in frontend api-gateway smart-contract-parser analysis-engine legal-compliance vulnerability-scanner report-generator; do \
		cd $$service && npm run build && cd ..; \
	done

test: ## Run tests for all services
	@echo "Running tests..."
	@for service in frontend api-gateway smart-contract-parser analysis-engine legal-compliance vulnerability-scanner report-generator; do \
		cd $$service && npm test && cd ..; \
	done

run: ## Run the project using Docker Compose
	@echo "Running services using Docker Compose..."
	@docker-compose up --build

deploy: ## Deploy the project to Minikube
	@echo "Deploying to Minikube..."
	@./scripts/setup_minikube.sh

clean: ## Remove build artifacts, Docker images, and delete Minikube cluster
	@echo "Cleaning up..."
	@for service in frontend api-gateway smart-contract-parser analysis-engine legal-compliance vulnerability-scanner report-generator; do \
		cd $$service && rm -rf node_modules dist && cd ..; \
	done
	@docker-compose down --rmi all --volumes --remove-orphans
	@minikube delete

.DEFAULT_GOAL := help
