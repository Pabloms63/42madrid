.PHONY: install run debug clean lint lint-strict test bench inspect check

install:
	uv sync

run:
	uv run python -m src

test:
	uv run python -m tests.test_grammar
	uv run python -m tests.test_real_data

bench:
	uv run python bench.py

inspect:
	uv run python debug.py

debug:
	uv run python -m pdb -m src

clean:
	rm -rf __pycache__ src/__pycache__ .mypy_cache .pytest_cache

lint:
	uv run flake8 .
	uv run mypy . --warn-return-any --warn-unused-ignores \
		--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run flake8 .
	uv run mypy . --strict

check: lint test