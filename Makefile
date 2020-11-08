format:
	black . && isort .
lint:
	flake8 .
precommit: format lint
	@echo Fix above errors, if present, before commiting.
run:
	python manage.py runserver
