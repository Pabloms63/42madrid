
PYTHON = python3
MAIN = a_maze_ing.py
CONFIG = config.txt


install:
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install -e .

run:
	-$(PYTHON) $(MAIN) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

build:
	$(PYTHON) -m build

clean:
	rm -rf __pycache__ .mypy_cache dist/ src/*.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

.PHONY: install run debug clean lint build