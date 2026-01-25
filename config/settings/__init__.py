from pathlib import Path

from config.core.env import load_env


BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_env(BASE_DIR)
