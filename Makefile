.DEFAULT_GOAL := help

PROJECT_SLUG  := pyproject

COLOR         :=\033[0;32m
NC            :=\033[0m


.PHONY: .uv  ## Check that uv is installed
.uv:
	@uv -V || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'


###### Development

.PHONY: install ## Install the package, dependencies, and pre-commit for local development
install: .uv
	uv sync --frozen --group all --all-extras
	pre-commit install --install-hooks

.PHONY: upgrade ## Updating all dependencies
upgrade: .uv
	uv lock --upgrade

.PHONY: format ## Auto-format source files
format: .uv
	uv run ruff check --fix .
	uv run ruff format .

.PHONY: lint ## Lint Python source files
lint: .uv
	uv run ruff check .
	uv run ruff format --check .

.PHONY: typecheck ## Perform type-checking
typecheck: .uv
	uv run mypy .

.PHONY: test ## Run all tests
test: .uv
	uv run pytest

.PHONY: benchmark ## Run all benchmarks
benchmark: .uv
	uv run pytest --benchmark-enable tests/benchmarks

.PHONY: all ## Run the standard set of checks
all: lint typecheck test testcov


###### Clean up

.PHONY: clean ## Clear local caches and build artifacts
clean:
	rm -rf dist
	rm -rf .cache
	rm -rf .hypothesis
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]'`


###### Additional commands

.PHONY: docs ## Open live documentation
docs:
	uv run pdoc \
		--docformat google \
		--math \
		src/$(PROJECT_SLUG)

ESCAPE := 
.PHONY: help ## Print this help
help:
	@grep -E \
		'^(.PHONY: .*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/\n##        $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' \
		| awk 'BEGIN {FS = ".PHONY: |## "}; {printf "\033[36m%-20s\033[0m %s\n", $$2, $$3}'
