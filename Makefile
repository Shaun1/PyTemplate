requirements:
	pip install -r requirements.txt

install:
	pipenv install
	pipenv shell

lint:
	pylint my_package; true

test: lint
	pytest
