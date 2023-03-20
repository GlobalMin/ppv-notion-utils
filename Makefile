VENV = .venv
VENV_PIP = $(VENV)/bin/pip



.PHONY: clean
clean: ## clean build artifacts
	@echo "🚀 Cleaning up build artifacts and cache files"
	@rm -rf dist
	@find . -type d -iname *.egginfo -exec rm -r {} +
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@rm -rf .coverage
	@find . -type d -iname __pycache__ -exec rm -r {} +


.PHONY: clean-docs
clean: 
	@echo "🚀 Cleaning up docs build artifacts"
	@rm -rf _build	
	@echo "🚀 Cleaning up docs cache files"
	@cd docs && rm -rf _build

.PHONY: install
install:

	@echo "🚀 Creating virtual environment in project root"
	@python -m virtualenv .venv

	@echo "🚀 Installing dependencies"
	@.venv/bin/pip install -r requirements.txt
	@.venv/bin/pip install -r requirements_dev.txt
	@.venv/bin/pip install -e .

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


# horizental line break 50% of terminal width
LINE = $(shell printf '=%.0s' {1..90})


.PHONY: build-docs
build-docs:
	clear
	@echo "$(LINE)"
	@echo "🚀 Building docs..."
	@echo "\n"
	@echo "Removing old build artifacts..."
	@rm -rf _build
	@echo "Done."
	@echo "\n"
	@echo "Pulling latest doc updates from main branch..."
	@git checkout origin/main -- docs
	@echo "Done."
	@echo "\n"
	@echo "Building docs to _build directory in root directory..."
	@sphinx-build -b html -E docs _build/html -q
	@echo "Done."
	@echo "\n"
	@echo "Opening in browser..."
	@open _build/html/index.html
	@echo "$(LINE)"
