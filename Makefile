requirements:
	pip install -r requirements.txt

install:
	python setup.py install

docs:
	mkdocs build --clean

test:
	nosetests -v

docker-build:
	docker build -t my_container .

docker-run:
	docker run --rm -ti -P my_container /bin/bash