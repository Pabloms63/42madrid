PYTHON	= python3
MAP		?= maps/example.txt
MYPY_FLAGS	= --warn-return-any --warn-unused-ignores \
		  --ignore-missing-imports --disallow-untyped-defs \
		  --check-untyped-defs

.PHONY: install run visual gui debug clean lint lint-strict

install:
	$(PYTHON) -m pip install flake8 mypy pygame

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

visual:
	$(PYTHON) main.py --visual $(MAP)

gui:
	$(PYTHON) main.py --gui $(MAP)
