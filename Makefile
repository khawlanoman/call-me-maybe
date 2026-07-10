
install:
	uv sync

run:
	uv run  python -m src
	
debug:
	uv python -m pdb 

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache

lint:
	-$(PYTHON) -m mypy . \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs
	$(PYTHON) -m flake8 .