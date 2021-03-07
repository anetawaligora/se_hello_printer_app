deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt
lint:
	flake8 hello_world test
.PHONY: test
test:
	PYTHONPATH=. py.test --verbose -s
run:
	PYTHONPATH=. FLASK_APP=hello_world flask run
test_smoke:
	curl --fail 127.0.0.1:5000
