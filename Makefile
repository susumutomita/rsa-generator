.PHONY: install
install:
	pip install -r requirements.txt && pre-commit install && npm install

.PHONY: lint
lint:
	black . --check
	yamllint -c .yamllint .
	flake8 .

.PHONY: format
format:
	black .

.PHONY: before_commit
before_commit: test format lint
