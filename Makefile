# catch all other commands
.DEFAULT:
	./manage.py $@

run: runserver

format:
	black . && isort .

lint:
	flake8 .

precommit: format lint
