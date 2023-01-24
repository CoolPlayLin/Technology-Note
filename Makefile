.PHONY: docs
init:
	python -m pip install --upgrade pip
	python -m pip install -r ./requirements.txt
build:
	python -m pip install build setuptools wheel
	python -m build