# Makefile for testing ai_pro_cat.py actions

# Default target
.DEFAULT_GOAL := help

# Python interpreter
PYTHON = python3

# Script name
SCRIPT = ai_pro_cat.py

# Project file
PROJECT_FILE = PROJECTS.org

# Output files
OUTPUT_FILE = projects_for_training.csv
TRAIN_FILE = train_data.csv
TEST_FILE = test_data.csv

# Test split ratio
TEST_SPLIT = 0.2

# Max refresh and unknown values
MAX_REFRESH = 3
MAX_UNKNOWN = 5

# ANSI color codes
CYAN = \033[0;36m
NC = \033[0m

# Help target
help:
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "$(CYAN)%-30s$(NC) %s\n", $$1, $$2}'

categorize: ## Run the categorize action
	$(PYTHON) $(SCRIPT) --action categorize --filename $(PROJECT_FILE) --max-refresh $(MAX_REFRESH) --max-unknown $(MAX_UNKNOWN)

analyze: ## Run the analyze action
	$(PYTHON) $(SCRIPT) --action analyze --filename $(PROJECT_FILE)

categories: ## Show all categories
	$(PYTHON) $(SCRIPT) --action categories

export: ## Export projects to CSV
	$(PYTHON) $(SCRIPT) --action export --filename $(PROJECT_FILE) --output-file $(OUTPUT_FILE)

train-test: ## Split data for training and testing
	$(PYTHON) $(SCRIPT) --action train-test --filename $(PROJECT_FILE) --output-file $(OUTPUT_FILE) --train-file $(TRAIN_FILE) --test-file $(TEST_FILE) --test-split $(TEST_SPLIT)

deduplicate: ## Deduplicate projects
	$(PYTHON) $(SCRIPT) --action deduplicate --filename $(PROJECT_FILE)

check-arxiv: ## Check recent arXiv papers
	$(PYTHON) $(SCRIPT) --action check-arxiv --filename $(PROJECT_FILE)

test-all: ## Run all actions in sequence
test-all: categorize analyze categories export train-test deduplicate check-arxiv
	@echo "$(CYAN)All tests completed.$(NC)"

clean: ## Remove generated files
	rm -f $(OUTPUT_FILE) $(TRAIN_FILE) $(TEST_FILE)
	rm -f category_similarity_dendrogram.png project_similarity_clusters.png
	rm -f arxiv_cache.json

.PHONY: help categorize analyze categories export train-test deduplicate check-arxiv test-all clean
