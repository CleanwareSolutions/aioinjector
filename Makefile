clean:
	find . -name '__pycache__' -exec rm -fr {} + && \
	find . -name *.pyc -exec rm -fr {} + && \
	rm .coverage .coverage.xml && \
	rm -rf ./.mypy_cache ./.pytest_cache

COVFILE ?= .coverage
PWD = $(shell pwd)

coverage:
	export COVERAGE_FILE=$(PWD)/$(COVFILE);pytest -x \
	--cov=$(PWD)/aioinjector $(PWD)/tests/ \
	--cov-report term-missing \
	--cov-report xml:$(PWD)/$(COVFILE).xml -s -vv \
	-o cache_dir=/tmp/pytest/cache

update:
	pip-review --auto
	pip freeze > requirements.txt