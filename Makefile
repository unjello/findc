.PHONY: all upload build

all: upload
upload:
	python setup.py sdist bdist_wheel upload
build:
	python setup.py sdist bdist_wheel
