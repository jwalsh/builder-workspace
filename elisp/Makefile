# Makefile for AWS AI Practice

.PHONY: all migrate test

all: migrate test

migrate: ## Migrate code
	emacs --batch -l aws-ai-practice-run-migrations.el

test: ## Run tests
	emacs --batch -l ert -l aws-ai-practice-tests.el -f ert-run-tests-batch-and-exit

clean: ## Clean up generated files
	rm -f ~/.emacs.d/aws-ai-practice.db

help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
