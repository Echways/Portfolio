import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application

from config.core.env import load_env

base_dir = Path(__file__).resolve().parent.parent
load_env(base_dir)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.environ.get("DJANGO_SETTINGS_MODULE", "config.settings.dev"),
)

application = get_wsgi_application()
