.PHONY: test run

run:
	@python src/main.py

test:
	@python -m unittest discover -v test
