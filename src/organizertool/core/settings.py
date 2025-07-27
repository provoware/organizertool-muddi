import json
import os
from pathlib import Path
from typing import Any, Dict


def get_settings_path() -> Path:
    """Return path to the settings file.

    The environment variable ``ORGANIZER_SETTINGS`` can override the default
    location ``~/.organizertool/settings.json``.
    """
    env = os.getenv("ORGANIZER_SETTINGS")
    if env:
        return Path(env)
    return Path.home() / ".organizertool" / "settings.json"


def load_settings() -> Dict[str, Any]:
    """Load settings from disk or return an empty dict."""
    path = get_settings_path()
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_settings(data: Dict[str, Any]) -> None:
    """Persist settings to disk."""
    path = get_settings_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
