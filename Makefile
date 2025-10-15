.PHONY: run test clean create-dummy run-test-clean all

create-dummy:
	@echo "Creating dummy files..."
	python3 data/create_dummy_files.py

run: create-dummy
	python3 src/date_parser.py

test: create-dummy
	pytest tests/test_date_parser.py --maxfail=1 --disable-warnings

check-lint:
	@echo "Running linter..."
	flake8 .

check-all: test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	find data -mindepth 1 -type d -exec rm -rf {} +
	find data -mindepth 1 -type f ! -name "create_dummy_files.py" -exec rm -f {} +

run-test-clean:
	$(MAKE) run
	$(MAKE) test
	$(MAKE) clean

all: run check-all clean
