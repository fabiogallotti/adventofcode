.DEFAULT_GOAL := help
SHELL = bash


.PHONY: help
help: ## show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install: ## install dependencies
	poetry install --with dev
	poetry run pre-commit install

.PHONY: black
black: ## apply code formatting
	poetry run black src tests

.PHONY: black-check
black-check: ## apply code formatting
	poetry run black --check src tests

.PHONY: ruff
ruff: ## enforce code style
	poetry run ruff check src tests

.PHONY: lint
lint: black ruff

.PHONY: test
test: ## run all tests
	poetry run pytest -vv -s

.PHONY: run-docker
run-docker:
	sh docker/run.sh
