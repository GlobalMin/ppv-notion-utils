


.PHONY: clean
clean: ## clean build artifacts
	@echo "🚀 Cleaning up build artifacts and cache files"
	@rm -rf dist
	@find . -type d -iname *.egginfo -exec rm -r {} +
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@rm -rf .coverage
	@find . -type d -iname __pycache__ -exec rm -r {} +


.PHONY: install
install:

	@echo "🚀 Creating virtual environment in project root"
	@python -m virtualenv .venv

	@echo "🚀 Installing dependencies"
	@.venv/bin/pip install -r requirements.txt
	@.venv/bin/pip install -r requirements-dev.txt
	@.venv/bin/pip install -e .




.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
