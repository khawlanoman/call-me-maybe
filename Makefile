
install:
# 	export UV_CACHE_DIR="$HOME/.cache/uv"
	uv add torch transformers

run:
	uv run python -m src.main
	
debug:
	uv run python -m pdb -m src.main

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