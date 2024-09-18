# Makefile for testing ai_pro_cat.py actions

# Default target
.DEFAULT_GOAL := help

# Python interpreter
PYTHON = poetry run python3

# Script name
CATEGORIZE_SCRIPT = ai_pro_cat.py
COORDINATOR_SCRIPT = coordinator.py 

# Project file
PROJECTS_DIR = projects
PROJECTS_FILE = $(PROJECTS_DIR)/README.org

# Tasks databas
TASKS_DB = tasks.db 

# Output files
OUTPUT_DIR = output
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


setup: ## Force Poetry 
	poetry add click pydantic anthropic google-generativeai ollama orgparse matplotlib numpy scikit-learn scipy requests

categorize: ## Run the categorize action
	$(PYTHON) $(CATEGORIZE_SCRIPT) --action categorize --filename $(PROJECTS_FILE) --max-refresh $(MAX_REFRESH) --max-unknown $(MAX_UNKNOWN)

analyze: ## Run the analyze action
	$(PYTHON) $(CATEGORIZE_SCRIPT) --action analyze --filename $(PROJECTS_FILE)

categories: ## Show all categories
	$(PYTHON) $(CATEGORIZE_SCRIPT) --action categories

export: ## Export projects to CSV
	$(PYTHON) $(CATEGORIZE_SCRIPT) --action export --filename $(PROJECTS_FILE) --output-file $(OUTPUT_FILE)

train-test: ## Split data for training and testing
	$(PYTHON) $(CATEGORIZE_SCRIPT) --action train-test --filename $(PROJECTS_FILE) --output-file $(OUTPUT_FILE) --train-file $(TRAIN_FILE) --test-file $(TEST_FILE) --test-split $(TEST_SPLIT)

deduplicate: ## Deduplicate projects
	$(PYTHON) $(CATEGORIZE_SCRIPT) --action deduplicate --filename $(PROJECTS_FILE)

check-arxiv: ## Check recent arXiv papers
	$(PYTHON) $(CATEGORIZE_SCRIPT) --action check-arxiv --filename $(PROJECTS_FILE)

test-all: ## Run all actions in sequence
test-all: categorize analyze categories export train-test deduplicate check-arxiv
	@echo "$(CYAN)All tests completed.$(NC)"

ollama-test-generate:
	curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d "{\"model\": \"llama3:8b-instruct-q8_0\", \"prompt\": \"System Message: Provide a concise summary of the following text.\n\nText: Machine learning is a subset of artificial intelligence that focuses on building systems that learn from data. It involves algorithms and statistical models to perform specific tasks without explicit instructions, relying on patterns and inference instead.\", \"temperature\": 0.5}"

ollama-test-embeddings:
	curl -X POST http://localhost:11434/api/embeddings -H "Content-Type: application/json" -d "{\"model\": \"mxbai-embed-large\", \"prompt\": \"Llamas are members of the camelid family\"}"

MultilinguaStoryForge:
	python coordinator.py --name MultilinguaStoryForge


BuilderAgents:
	python coordinator.py --name BuilderAgents

AdFlow:
	python coordinator.py --name AdFlow --force

clean: ## Remove generated files
	rm -f $(OUTPUT_FILE) $(TRAIN_FILE) $(TEST_FILE)
	rm -f category_similarity_dendrogram.png project_similarity_clusters.png
	rm -f arxiv_cache.json

.PHONY: help categorize analyze categories export train-test deduplicate check-arxiv test-all clean
