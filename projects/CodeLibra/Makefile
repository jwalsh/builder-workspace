# Makefile for Code Librarian Monorepo

# Variables
PYTHON := python3
PIP := $(PYTHON) -m pip
NPM := npm
AWS_CLI := aws
SAM_CLI := sam

# Directories
API_HANDLER_DIR := src/api_handler
CODE_ANALYZER_DIR := src/code_analyzer
COMMIT_HANDLER_DIR := src/commit_handler
GRAPHQL_DIR := src/graphql
FRONTEND_DIR := src/frontend

# AWS SAM template
SAM_TEMPLATE := template.yaml

# Phony targets
.PHONY: all clean install test lint build deploy

# Default target
all: install test lint build

# Clean build artifacts
clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	rm -rf .aws-sam
	rm -rf $(FRONTEND_DIR)/build

# Install dependencies
install:
	$(PIP) install -r requirements.txt
	cd $(FRONTEND_DIR) && $(NPM) install

# Run tests
test:
	$(PYTHON) -m pytest tests/
	cd $(FRONTEND_DIR) && $(NPM) test

# Lint code
lint:
	$(PYTHON) -m flake8 src/ tests/
	cd $(FRONTEND_DIR) && $(NPM) run lint

# Build the project
build:
	$(SAM_CLI) build -t $(SAM_TEMPLATE)
	cd $(FRONTEND_DIR) && $(NPM) run build

# Deploy the project
deploy:
	$(SAM_CLI) deploy --guided

# API Handler specific targets
.PHONY: api-handler-test api-handler-lint

api-handler-test:
	$(PYTHON) -m pytest tests/api_handler/

api-handler-lint:
	$(PYTHON) -m flake8 $(API_HANDLER_DIR)/

# Code Analyzer specific targets
.PHONY: code-analyzer-test code-analyzer-lint

code-analyzer-test:
	$(PYTHON) -m pytest tests/code_analyzer/

code-analyzer-lint:
	$(PYTHON) -m flake8 $(CODE_ANALYZER_DIR)/

# Commit Handler specific targets
.PHONY: commit-handler-test commit-handler-lint

commit-handler-test:
	$(PYTHON) -m pytest tests/commit_handler/

commit-handler-lint:
	$(PYTHON) -m flake8 $(COMMIT_HANDLER_DIR)/

# GraphQL specific targets
.PHONY: graphql-test graphql-lint

graphql-test:
	$(PYTHON) -m pytest tests/graphql/

graphql-lint:
	$(PYTHON) -m flake8 $(GRAPHQL_DIR)/

# Frontend specific targets
.PHONY: frontend-test frontend-lint frontend-build

frontend-test:
	cd $(FRONTEND_DIR) && $(NPM) test

frontend-lint:
	cd $(FRONTEND_DIR) && $(NPM) run lint

frontend-build:
	cd $(FRONTEND_DIR) && $(NPM) run build

# Local development
.PHONY: run-local

run-local:
	$(SAM_CLI) local start-api
	cd $(FRONTEND_DIR) && $(NPM) start
