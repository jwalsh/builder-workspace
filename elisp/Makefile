# Makefile for AWS AI Practice

.PHONY: all migrate test

EMACS = emacs
EMACSFLAGS = --batch -Q -L . --eval "(setq load-prefer-newer t)"

all: migrate test

migrate: ## Migrate code
	$(EMACS) $(EMACSFLAGS) -l aws-ai-practice-migrations.el -l aws-ai-practice-run-migrations.el \
		--eval "(aws-ai-practice-run-migrations-and-checks)"

test: ## Run tests
	$(EMACS) $(EMACSFLAGS) -l aws-ai-practice.el -l aws-ai-practice-migrations.el -l ert \
		-l aws-ai-practice-tests.el -f ert-run-tests-batch-and-exit

clean: ## Clean up generated files
	rm -f aws-ai-practice.db

help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
