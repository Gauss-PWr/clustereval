black:
	black src tests

flake:
	flake8 src tests

lint: black flake

test:
	pytest -n auto -vv