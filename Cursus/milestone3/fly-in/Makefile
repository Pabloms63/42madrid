.PHONY: install run debug clean lint lint-strict

# python3 -m venv .venv
# source .venv/bin/activate

PYTHON	= python3
MAP		?= maps/easy/01_linear_path.txt
MYPY_FLAGS	= --warn-return-any --warn-unused-ignores \
		  --ignore-missing-imports --disallow-untyped-defs \
		  --check-untyped-defs

install:
	$(PYTHON) -m pip install flake8 mypy

run:
	$(PYTHON) main.py $(MAP)

debug:
	$(PYTHON) -m pdb main.py $(MAP)

clean:
	rm -rf __pycache__ */__pycache__ .mypy_cache .pytest_cache

lint:
	$(PYTHON) -m flake8 . --exclude=.venv
	$(PYTHON) -m mypy . --exclude '^\.venv/' $(MYPY_FLAGS)

lint-strict:
	$(PYTHON) -m flake8 . --exclude=.venv
	$(PYTHON) -m mypy . --exclude '^\.venv/' --strict