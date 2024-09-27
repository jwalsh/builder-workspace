
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

clean-test-project: ## Remove TestProject and add JSON files
	rm -rf projects/TestProject
	git add projects/*/*.json
	@echo "TestProject removed and JSON files added to git."

test-coordinator-all: test-coordinator ## Run all coordinator tests
	$(COORDINATOR) --list
	$(COORDINATOR) --name TestProject --use-llm claude
	$(COORDINATOR) --check-health

list: # List Coordinator tasks
	$(COORDINATOR) --list

list-tasks: ## List all tasks
	sqlite3 tasks.db "SELECT id, project_id, title, status, assigned_to, task_type, rfc_state FROM tasks;" | tee tasks_output.txt

tangle: ## Get txt files for all projects
	poetry run emacs -Q --batch -l org --eval '(org-babel-tangle-file "projects/README.org")'

tangle-all: ## Tangle code blocks from org files
	@echo "Tangling code blocks..."
	@for file in $(ORG_FILES); do \
		emacs --batch --eval "(progn \
			(require 'org) \
			(org-babel-tangle-file \"$$file\"))"; \
	done
	@echo "Tangling complete."

generate-diagrams: ## Generate diagrams from org files
	@echo "Generating diagrams..."
	@for file in $(MERMAID_ORG_FILES); do \
		emacs --batch --eval "(progn \
			(require 'org) \
			(find-file \"$$file\") \
			(org-babel-execute-buffer) \
			(save-buffer) \
			(kill-buffer))"; \
	done
	@echo "Diagram generation complete."

install-emacs-packages: ## Install required Emacs packages
	@echo "Installing Emacs packages..."
	@emacs --batch --eval "(progn \
		(require 'package) \
		(add-to-list 'package-archives '(\"melpa\" . \"https://melpa.org/packages/\") t) \
		(package-initialize) \
		(package-refresh-contents) \
		(package-install 'org) \
		(package-install 'htmlize))"


run-analyzer: ## Run the analyzer on the projects
	$(PYTHON) -m analyzer --action categorize --filename projects/README.org
	$(PYTHON) -m analyzer --action analyze --filename projects/README.org

.PHONY: help setup test lint format pre-commit repl test-coordinator test-coordinator-all

.PHONY: migrate

# Define the directory where migration scripts are located
MIGRATIONS_DIR := migrations

# Find all Python files in the migrations directory and sort them
MIGRATION_SCRIPTS := $(sort $(wildcard $(MIGRATIONS_DIR)/*.py))

migrate:
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


generate-docs: ## Generate documentation for the project
	@echo "Generating documentation..."
	poetry add sphinx
	poetry run sphinx-quickstart -q -p "Coordinator" -a "Jason Walsh" -v "0.1" -l "en" --ext-autodoc --makefile docs
	poetry run sphinx-apidoc -o docs/source coordinator
	@echo "import os" >> docs/source/conf.py
	@echo "import sys" >> docs/source/conf.py
	@echo "sys.path.insert(0, os.path.abspath('../..'))" >> docs/source/conf.py
	cd docs && poetry run make html
	@echo "Documentation generated in the 'docs/_build/html' directory."
