# catch all other commands
.DEFAULT:
	./manage.py $@

run:
	./manage.py runserver

format:
	black . && isort .

lint:
	flake8 .

precommit: format lint
	@echo Fix above errors, if present, before commiting.