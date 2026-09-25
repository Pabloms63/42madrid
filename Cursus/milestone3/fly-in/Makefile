.PHONY: install run debug clean lint lint-strict

##source .venv/bin/activate

lint:
	python3 -m flake8 . --exclude=.venv
	python3 -m mypy fly_in \
		--exclude='^\.venv/' \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs