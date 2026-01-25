#!/usr/bin/env python
import os
import sys
from pathlib import Path

from config.core.env import load_env


def main():
    base_dir = Path(__file__).resolve().parent
    load_env(base_dir)

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        os.environ.get("DJANGO_SETTINGS_MODULE", "config.settings.dev"),
    )
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
