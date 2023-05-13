.DEFAULT_GOAL := help

PROJECT_SLUG  := py_project

COLOR         :=\033[0;32m
NC            :=\033[0m


###### Development

.PHONY: update-requirements
update-requirements: ## Update requirements.txt file
	@poetry export --output requirements.txt

.PHONY: doc
doc: ## Open package documentation
	@poetry run pdoc \
		--docformat google \
		--math \
		src/$(PROJECT_SLUG)

.PHONY: format
format: ## Format code
	@printf "\n${COLOR}=== Formatting code...${NC}\n"
	-poetry run pyupgrade --py310-plus $$(git ls-files '*.py')
	-poetry run ruff check --fix .
	poetry run isort .
	poetry run black .


.PHONY: test
test: test-lint test-unit test-safety ## Run all tests by decreasing priority

.PHONY: test-lint
test-lint: ## Run code linting tests
	@printf "\n${COLOR}=== Running code linting tests...${NC}\n"
	poetry run pyupgrade --py310-plus $$(git ls-files '*.py')
	poetry run isort .
	poetry run black .
	poetry run ruff check .
	poetry run flake8 .
	poetry run pylint $$(git ls-files '*.py')
	poetry run mypy .

.PHONY: test-unit
test-unit: ## Run unit tests
	@printf "\n${COLOR}=== Running unit tests...${NC}\n"
	@poetry run pytest

.PHONY: test-safety
test-safety: ## Run dependencies safety tests
	@printf "\n${COLOR}=== Running dependencies safety tests...${NC}\n"
	poetry check
	poetry run pip check
	poetry run safety check --full-report


###### Deployment


###### Clean up

.PHONY: clean
clean: ## Clean temporary files and directories
	@printf "\n${COLOR}=== Cleaning temporary files and directories...${NC}\n"
	@rm -rf dist
	@rm -rf .cache
	@rm -rf .hypothesis
	@-find . -regex "^.*\(__pycache__\|\.?coverage\(\|\..*\)\)" -exec rm -rf {} +


###### Additional commands

.PHONY: version
version: ## Print the current version
	@cat pyproject.toml | grep -o '\([0-9]\+\.\?\)\{3\}' | head -1

ESCAPE := 
.PHONY: help
help: ## Print this help
	@grep -E '^([a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/\n        $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-20s\033[0m %s\n", $$1, $$2}'
