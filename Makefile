.PHONY: lint test check fmt fmt-check typecheck deps

lint:
	flake8 src/organizertool tests

test:
	PYTHONPATH=src pytest -q

fmt:
	black src/organizertool tests

fmt-check:
	black --check src/organizertool tests

typecheck:
	mypy src/organizertool tests

check: fmt-check lint test typecheck
	
deps:
	python -m pip check
