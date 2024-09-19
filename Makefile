# Makefile for coordinator project

PYTHON = poetry run python
COORDINATOR = $(PYTHON) -m coordinator

# ANSI color codes
CYAN := \033[36m
RESET := \033[0m

# Default target
.DEFAULT_GOAL := help

help: ## Display help information
	@echo "Available commands:"
	@awk 'BEGIN {FS = ":.*##"; printf "\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  $(CYAN)%-15s$(RESET) %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

setup: ## Set up the project environment
	poetry install
	poetry run pre-commit install

test: ## Run tests
	$(PYTHON) -m pytest tests/

lint: ## Run linter
	poetry run flake8 coordinator/

format: ## Format code
	poetry run black coordinator/
	poetry run isort coordinator/

pre-commit: ## Run pre-commit checks
	poetry run pre-commit run --all-files

repl: ## Start Python REPL with coordinator module
	poetry run ipython -i -c "import coordinator; print('Coordinator module loaded. Use coordinator.main() to run the main function.')"

coordinator-files: ## Get Coordinator files for LLM review
	files-to-prompt coordinator | tee coordinator_files.txt

test-coordinator: ## Run test coordinator with a sample project
	$(COORDINATOR) --name TestProject --description "This is a test project" --force

test-coordinator-all: test-coordinator ## Run all coordinator tests
	$(COORDINATOR) --list
	$(COORDINATOR) --name TestProject --use-llm claude
	$(COORDINATOR) --check-health

list: # List Coordinator tasks
	$(COORDINATOR) --list

list-tasks: ## List all tasks
	sqlite3 tasks.db "SELECT id, project_id, title, status, assigned_to, task_type, rfc_state FROM tasks;" | tee tasks_output.txt

.PHONY: help setup test lint format pre-commit repl test-coordinator test-coordinator-all
