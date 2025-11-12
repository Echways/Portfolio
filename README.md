# Portfolio

Небольшой Django-сайт-портфолио: главная страница с достижениями, лента новостей, проекты и детальные страницы для каждого материала.  
Админка позволяет удобно добавлять новости, проекты и достижения без правки кода.

## Стек

- **Python** 3.10
- **Django** 4.0.x
- **SQLite**
- **Pillow** — работа с изображениями
- HTML/CSS/JS, статические ресурсы в `static/`

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone git@github.com:Echways/Portfolio.git
cd Portfolio
```

### 2. Создание виртуального окружения

```bash
python3 -m venv venv
source venv/bin/activate      # Linux/macOS
# или
venv\Scripts\activate         # Windows
```

### 3. Установка зависимостей

```bash
pip install pipenv
pipenv install
pipenv install "django==4.0.4"
pipenv install pillow
pipenv shell
```

### 4. Миграции базы данных

```bash
python manage.py migrate
```

### 5. Создание суперпользователя (для входа в /admin)

```bash
python manage.py createsuperuser
```

### 6. Запуск дев-сервера

```bash
python manage.py runserver
```

## Работа с контентом

Все данные (новости, проекты, достижения) управляются через Django Admin.

**Модели:**

- `News`
  - `title` — заголовок новости
  - `description` — текст новости
  - `image` — изображение (`static/media/img/news/…`)
- `Projects`
  - `title` — заголовок проекта
  - `description` — описание проекта
  - `image` — изображение (`static/media/img/projects/…`)
- `Achievments`
  - `text` — строка с описанием достижения

