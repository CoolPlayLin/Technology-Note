.PHONY: docs
init:
	python -m pip install --upgrade pip
	python -m pip install -r ./requirements.txt
	python -m pip install build setuptools wheel
build:
	python -m build
ci:
	python -m pip install isort
	python -m isort . --diff >> Report.txt