import os
from pathlib import Path
from typing import Iterable, List


def _resolve_base_dir(base_dir: Path | None = None) -> Path:
    if base_dir is not None:
        return base_dir
    return Path(__file__).resolve().parents[2]


def load_env(base_dir: Path | None = None, filename: str = ".env") -> Path:
    resolved_base_dir = _resolve_base_dir(base_dir)
    env_path = resolved_base_dir / filename
    if not env_path.exists():
        return env_path
    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
    return env_path


def get_str(name: str, default: str | None = None) -> str | None:
    return os.environ.get(name, default)


def get_bool(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.lower() in {"1", "true", "yes", "on"}


def get_int(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def get_list(name: str, default: Iterable[str] | None = None, separator: str = ",") -> List[str]:
    raw = os.environ.get(name)
    if raw is None:
        return list(default or [])
    return [item.strip() for item in raw.split(separator) if item.strip()]
