# Use bash as the shell
SHELL := /bin/bash

# Variables
PYTHON = python3
POETRY = poetry
PYTEST = $(POETRY) run pytest
FLAKE8 = $(POETRY) run flake8

.PHONY: install run test lint clean setup docs check all

# Install dependencies
install:
	$(POETRY) install

# Run the application
run:
	$(POETRY) run aicodereviewer

# Run tests
test:
	$(PYTEST) tests/

# Run linter
lint:
	$(FLAKE8) aicodereviewer/ tests/

# Clean up pyc files and __pycache__ directories
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Set up the project (install dependencies and create necessary directories)
setup: install
	mkdir -p logs

# Generate documentation (placeholder, replace with actual documentation generator)
docs:
	@echo "Generating documentation..."
	# Add command to generate documentation here

# Run all checks (tests and linting)
check: test lint

# Add new dependencies
add-dep:
	@read -p "Enter the package name: " package; \
	$(POETRY) add $$package

# Add new development dependencies
add-dev-dep:
	@read -p "Enter the development package name: " package; \
	$(POETRY) add --dev $$package

# Update dependencies
update:
	$(POETRY) update

# Show dependency tree
show-deps:
	$(POETRY) show --tree

# Create a new virtual environment
create-venv:
	$(POETRY) env use python3

# Activate the virtual environment (note: this needs to be run with 'source' command)
activate-venv:
	@echo "To activate the virtual environment, run: source $$($(POETRY) env info --path)/bin/activate"

# Export dependencies to requirements.txt
export-requirements:
	$(POETRY) export -f requirements.txt --output requirements.txt

# Default target
all: setup check
