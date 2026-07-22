
install:
	uv sync

run:
	uv run python -m src
	
debug:
	uv run python -m pdb -m src

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf ./src/__pycache__
	rm -rf ./data/output

fclean: clean
	rm -rf data/output

lint:
	- python -m mypy ./src\
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs
	python -m flake8 ./src