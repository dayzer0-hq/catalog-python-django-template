# catalog-python-django-template

A minimal, runnable **Python + Django** starter for DayZer0 catalog briefs. It is a
generic starting point shared by every Python + Django brief: a Django project with
[Django REST Framework](https://www.django-rest-framework.org/) installed and a single
health route. Build your brief's feature on top of it — add an app, your models and your
endpoints.

## Stack

- Python 3.11+
- Django 4.2 (LTS) + Django REST Framework (pinned in `requirements.txt`)

## Layout

- `config/` — the Django project (settings, URLs, WSGI/ASGI)
- `health/` — an app exposing `GET /health`
- `manage.py` — Django's management entry point

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Then confirm the health route:

```bash
curl http://127.0.0.1:8000/health
# {"status": "ok"}
```

`python manage.py check` should report no issues.
