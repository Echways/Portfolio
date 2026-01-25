PYTHON ?= python3
MANAGE := $(PYTHON) manage.py

.PHONY: run test check migrate makemigrations shell lint format db-up db-down db-logs db-wait

run:
	$(MANAGE) runserver

test:
	$(MANAGE) test

check:
	$(MANAGE) check

migrate:
	$(MANAGE) migrate --noinput

makemigrations:
	$(MANAGE) makemigrations

shell:
	$(MANAGE) shell

lint:
	ruff check .

format:
	black .
	isort .

db-up:
	docker compose up -d db
	$(MAKE) db-wait

db-down:
	docker compose down

db-logs:
	docker compose logs -f db

db-wait:
	docker compose ps db
