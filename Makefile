.PHONY: test

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt
lint:
	flake8 hello_world test
test:
	PYTHONPATH=. py.test --verbose -s
run:
	PYTHONPATH=. FLASK_APP=hello_world flask run

docker_build:
	docker build -t hello-world-printer .

USERNAME=anetaw
TAG=$(USERNAME)/hello-world-printer

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD};	\
	docker tag hello-world-printer $(TAG); \
	docker push $(TAG); \
	docker logout;

test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=.


test_xunit:
	PYTHONPATH=. py.test --verbose -s --cov=. --cov-report xml
	PYTHONPATH=. py.test -s --cov=. --cov-report xml --junit-xml=test_results.xml
