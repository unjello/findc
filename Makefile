.PHONY: all upload build clean

all: upload
upload:
	python setup.py sdist bdist_wheel upload
build:
	python setup.py sdist bdist_wheel
clean:
	rm -rf build/ dist/ find_compiler.egg-info
