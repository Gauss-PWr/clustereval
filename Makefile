black:
	black src tests

flake:
	flake8 src tests

isort:
	isort src tests

lint: black flake isort

test:
	pytest -n auto -vv
