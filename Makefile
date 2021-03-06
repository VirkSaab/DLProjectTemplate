# set the name of the virtual environment, project name, and python version
VENV := venv
PROJ_NAME := dlp
PYI := python3.9

.PHONY: help ce make_venv install clean make_docs update_docs test_base run_flask

help:	## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


ce:	## Display current environment information
	@echo "Current environment:"
	@echo "\t Python - $(shell which python)"
	@echo "\t Pip - $(shell which pip)"


make_venv:	## Create a virtual environment.
ifneq ($(wildcard ./${VENV}/bin/activate),)
	@echo "${VENV} folder already exists. Delete it first to make new one."
else
	@echo "creating virtual environment..."
	@$(PYI) -m venv $(VENV)
	@./$(VENV)/bin/pip install -U pip
	@./$(VENV)/bin/pip install ruamel.yaml
	@./$(VENV)/bin/pip install easydict
	@./$(VENV)/bin/pip install -r requirements.txt
	@echo "Installing ${PROJ_NAME} in dev mode..."
	@./$(VENV)/bin/pip install -e .
endif


install:	## Install the project in editable (or dev) mode.
	@echo "Installing ${PROJ_NAME} in dev mode..."
	@./$(VENV)/bin/pip install -e .


clean:	## Clean unused files.
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf docs/build
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@echo Done!


make_docs:	## create new documentation
ifneq ($(wildcard ./docs/.*),)
	@echo "docs folder already exists. Delete that first to make new one."
else
	@echo "Creating sphinx docs..."
	sphinx-quickstart docs
endif


update_docs: docs/Makefile ## Update documentation
	sphinx-apidoc -o docs/source ${PROJ_NAME} --force
	make -C docs html
	@git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all > CHANGELOG.md


test_base: # Test on first project setup
	pytest tests/test_config.py


run_flask: ${PROJ_NAME}/deploy  ## Start the flask app server
	FLASK_APP=${PROJ_NAME}/deploy/app flask run
