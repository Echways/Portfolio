# Portfolio

Сайт‑портфолио: главная страница с командой и достижениями, лента новостей, проекты и детальные страницы для каждого материала. Контент управляется через админку.

## Стек

- Python 3.10+
- Django 5.x
- PostgreSQL
- Pillow
- HTML/CSS/JS, статика в `static/`, медиа в `media/`

## Быстрый старт

### 1. Клонирование

```bash
git clone git@github.com:Echways/Portfolio.git
cd Portfolio
```

### 2. Окружение и зависимости

Вариант через pipenv:

```bash
pip install pipenv
pipenv install --dev
pipenv shell
```

Вариант через venv:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install "Django>=5,<6" "pillow>=10" "psycopg[binary]"
```

### 3. PostgreSQL

Одна команда поднимает базу в Docker:

```bash
make db-up
```

### 4. Настройки окружения

```bash
cp .env.example .env
```

Минимально важные переменные для Postgres:

```env
DJANGO_DB_ENGINE=postgres
DJANGO_DB_NAME=portfolio
DJANGO_DB_USER=postgres
DJANGO_DB_PASSWORD=postgres
DJANGO_DB_HOST=127.0.0.1
DJANGO_DB_PORT=5444
```

### 5. Миграции и запуск

```bash
python manage.py migrate
python manage.py runserver
```

## Makefile команды

```bash
make run
make test
make check
make migrate
make db-up
make db-down
make db-logs
```

## Pre-commit

```bash
pipenv run pre-commit install
pipenv run pre-commit run --all-files
```

## Основные URL

- Сайт: `http://127.0.0.1:8000/`
- Админка: `http://127.0.0.1:8000/admin/`
- Healthcheck: `http://127.0.0.1:8000/health/`
- API root: `http://127.0.0.1:8000/api/`
- API schema: `http://127.0.0.1:8000/api/schema/`
- API docs: `http://127.0.0.1:8000/api/docs/`

## API v1

Поддерживает пагинацию: `?page=1&page_size=6`

- `GET /api/v1/news/`
- `GET /api/v1/news/<slug>/`
- `GET /api/v1/projects/`
- `GET /api/v1/projects/<slug>/`
- `GET /api/v1/team/`
- `GET /api/v1/achievements/`

## Настройки (dev/prod)

- Dev по умолчанию: `config.settings.dev`
- Prod: `config.settings.prod`

Пример запуска prod:

```bash
DJANGO_SETTINGS_MODULE=config.settings.prod python manage.py runserver
```

## Структура проекта

- `config/` — системный слой (settings, urls, core, api)
- `info/` — доменная логика (models, selectors, views, templates, tests)
- `templates/` — системные шаблоны (`404.html`, `500.html`, `api_docs.html`)
- `static/` — статика
- `media/` — загруженные файлы
