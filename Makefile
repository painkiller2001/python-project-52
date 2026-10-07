PORT ?= 8000

install:
	uv sync

collectstatic:
	uv run manage.py collectstatic --noinput

migrate:
	uv run manage.py migrate

lint:
	uv run ruff check .

build:
	./build.sh

setup: install collectstatic migrate

render-start:
	gunicorn task_manager.wsgi
