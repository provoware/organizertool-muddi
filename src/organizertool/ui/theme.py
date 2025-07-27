"""Simple themes for the GUI."""

from __future__ import annotations

import os

from ..core.settings import load_settings, save_settings

THEMES: dict[str, str] = {
    "dark": """
        QMainWindow { background-color: #1e1e1e; color: #eeeeee; }
        QToolBar { background-color: #3c3c3c; color: #ffffff; }
        QLabel { color: #eeeeee; }
    """,
    "light": """
        QMainWindow { background-color: #ffffff; color: #000000; }
        QToolBar { background-color: #dddddd; color: #000000; }
        QLabel { color: #000000; }
    """,
    "blue": """
        QMainWindow { background-color: #002b36; color: #93a1a1; }
        QToolBar { background-color: #073642; color: #cb4b16; }
        QLabel { color: #93a1a1; }
    """,
    "contrast": """
        QMainWindow { background-color: #000000; color: #ffffff; }
        QToolBar { background-color: #444444; color: #ffffff; }
        QLabel { color: #ffffff; }
    """,
}

DEFAULT_THEME = "dark"


def get_current_theme_name() -> str:
    """Return the active theme name."""

    env = os.getenv("ORGANIZER_THEME")
    if env:
        return env.lower()
    settings = load_settings()
    return str(settings.get("theme", DEFAULT_THEME)).lower()


def get_current_theme() -> str:
    """Return stylesheet for the active theme."""

    return THEMES.get(get_current_theme_name(), THEMES[DEFAULT_THEME])


def set_current_theme(name: str) -> None:
    """Persist the chosen theme name."""

    data = load_settings()
    data["theme"] = name
    save_settings(data)
