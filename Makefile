VENV = .venv
VENV_PIP = $(VENV)/bin/pip

# draw horizontal line 50% of the terminal width
LINE = $(shell printf '%*s' "80" '' | tr ' ' -)


.PHONY: help
help:
	@echo $(LINE)
	@echo "Available commands:"
	@echo "  clean         to clean up build artifacts and cache files"
	@echo "  install       to install dependencies and create virtual environment"
	@echo "  install_dev   to install extra dependencies for rendering docs and testing"
	@echo "  wipe_all      to run normal cleaning and also remove venv/tox"
	@echo $(LINE)

.PHONY: clean
clean: 
	@echo "🚀 Cleaning up build artifacts and cache files like '__pycache__','.ipynb_checkpoints', etc."
	@rm -rf dist
	@find . -type d -iname *.egg-info -exec rm -r {} +
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@rm -rf .coverage
	@find . -type d -iname __pycache__ -exec rm -r {} +
	@find . -type d -iname .ipynb_checkpoints -exec rm -r {} +

.PHONY: install
install:
	@echo "🚀 Creating virtual environment in project root"
	@python -m virtualenv .venv
	@echo "🚀 Installing dependencies"
	@.venv/bin/pip install -r requirements.txt
	@.venv/bin/pip install -e .

.PHONY: install_dev
install_dev:
	@echo "🚀 Install extra dependencies for rendering docs and testing"
	@.venv/bin/pip install -r requirements_dev.txt


.PHONY: wipe_all
wipe_all:
	@echo "🚀 Run normal cleaning and also remove venv/tox"
	@make clean
	@rm -rf .venv
	@rm -rf .tox
