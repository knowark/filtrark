
clean:
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf ./.cache .mypy_cache ./schema/.mypy_cache .coverage+

test:
	pytest

PROJECT = filtrark
COVFILE ?= .coverage

mypy:
	mypy $(PROJECT)

coverage: 
	export COVERAGE_FILE=$(COVFILE); pytest -x --cov=$(PROJECT) tests/ \
	--cov-branch --cov-report term-missing -s -o cache_dir=/tmp/.pytest_cache

PART ?= patch

version:
	bump2version $(PART) pyproject.toml $(PROJECT)/__init__.py --tag --commit
