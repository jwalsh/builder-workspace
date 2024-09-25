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
	@awk 'BEGIN {FS = ":.*##"; printf "\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  $(CYAN)%-20s$(RESET) %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

setup: ## Set up the project environment
	poetry install
	poetry run pre-commit install

test: ## Run all tests
	$(PYTHON) -m pytest tests/

lint: ## Run linter
	poetry run flake8 coordinator/

format: ## Format code
	poetry run black coordinator/
	poetry run isort coordinator/

sort-imports: ## Sort imports in Python files
	poetry run isort coordinator/

.PHONY: sort-imports

pre-commit: ## Run pre-commit checks
	poetry run pre-commit run --all-files

repl: ## Start Python REPL with coordinator module
	poetry run ipython -i -c "import coordinator; print('Coordinator module loaded. Use coordinator.main() to run the main function.')"

coordinator-files: ## Get Coordinator files for LLM review
	files-to-prompt coordinator | tee coordinator_files.txt

test-coordinator: ## Run test coordinator with a sample project
	$(COORDINATOR) --name TestProject --description "This is a test project" --force

clean-test-project: ## Remove TestProject and add JSON files
	rm -rf projects/TestProject
	git add projects/*/*.json
	@echo "TestProject removed and JSON files added to git."

test-coordinator-all: test-coordinator ## Run all coordinator tests
	$(COORDINATOR) --list
	$(COORDINATOR) --name TestProject --use-llm claude
	$(COORDINATOR) --check-health

list: ## List Coordinator tasks
	$(COORDINATOR) --list

list-tasks: ## List all tasks
	sqlite3 tasks.db "SELECT id, project_id, title, status, assigned_to, task_type, rfc_state FROM tasks;" | tee tasks_output.txt

tangle: ## Get txt files for all projects
	poetry run emacs -Q --batch -l org --eval '(org-babel-tangle-file "projects/README.org")'

run-analyzer: ## Run the analyzer on the projects
	$(PYTHON) -m analyzer --action categorize --filename projects/README.org
	$(PYTHON) -m analyzer --action analyze --filename projects/README.org

# Define the directory where migration scripts are located
MIGRATIONS_DIR := migrations
# Find all Python files in the migrations directory and sort them
MIGRATION_SCRIPTS := $(sort $(wildcard $(MIGRATIONS_DIR)/*.py))

migrate: ## Run database migrations
	@echo "Running database migrations..."
	@for script in $(MIGRATION_SCRIPTS); do \
		echo "Applying migration: $$script"; \
		python $$script; \
		if [ $$? -ne 0 ]; then \
			echo "Error applying migration: $$script"; \
			exit 1; \
		fi; \
	done
	@echo "All migrations completed successfully."

test-all: ## Run all LLM provider tests
	pytest tests/test_llm_providers.py

test-claude: ## Test Claude provider
	pytest tests/test_llm_providers.py::test_claude_provider

test-openai: ## Test OpenAI provider
	pytest tests/test_llm_providers.py::test_openai_provider

test-azure-openai: ## Test Azure OpenAI provider
	pytest tests/test_llm_providers.py::test_azure_openai_provider

test-bedrock: ## Test Bedrock provider
	pytest tests/test_llm_providers.py::test_bedrock_provider

test-ollama: ## Test Ollama provider
	pytest tests/test_llm_providers.py::test_ollama_provider

test-standard-model: ## Test standard LLM model
	pytest tests/test_llm.py

.PHONY: help setup test lint format pre-commit repl test-coordinator test-coordinator-all
.PHONY: migrate test-all test-claude test-openai test-azure-openai test-bedrock test-ollama test-standard-model
