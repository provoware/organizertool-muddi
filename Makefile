.PHONY: lint test check

lint:
	flake8 src/organizertool tests

test:
	PYTHONPATH=src pytest -q

check: lint test

