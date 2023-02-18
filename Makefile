.SILENT:

up:
	docker-compose stop
	docker-compose up

build:
	docker-compose stop
	docker-compose build

migrate:
	docker-compose stop
	docker-compose run --rm cards manage.py migrate

createsuperuser:
	docker-compose stop
	docker-compose run --rm cards manage.py createsuperuser

makemigrations:
	docker-compose stop
	docker-compose run --rm cards manage.py makemigrations ${app}