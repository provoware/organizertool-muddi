"""Simple themes for the GUI."""

from __future__ import annotations

import os

from ..core.settings import load_settings, save_settings
from ..core.constants import (
    ENV_THEME,
    ENV_FONT_SIZE,
    DEFAULT_THEME,
    DEFAULT_FONT_SIZE,
)

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


def get_current_theme_name() -> str:
    """Return the active theme name."""

    env = os.getenv(ENV_THEME)
    if env:
        return env.lower()
    settings = load_settings()
    return str(settings.get("theme", DEFAULT_THEME)).lower()


def get_current_theme() -> str:
    """Return stylesheet for the active theme including font size."""

    theme = THEMES.get(get_current_theme_name(), THEMES[DEFAULT_THEME])
    size = get_current_font_size()
    return theme + f"\nQWidget {{ font-size: {size}pt; }}"


def set_current_theme(name: str) -> None:
    """Persist the chosen theme name."""

    data = load_settings()
    data["theme"] = name
    save_settings(data)


def get_current_font_size() -> int:
    """Return the active font size in points."""

    env = os.getenv(ENV_FONT_SIZE)
    if env:
        try:
            return int(env)
        except ValueError:
            pass
    settings = load_settings()
    size = settings.get("font_size", DEFAULT_FONT_SIZE)
    try:
        return int(size)
    except (TypeError, ValueError):
        return DEFAULT_FONT_SIZE


def set_current_font_size(size: int) -> None:
    """Persist the font size."""

    data = load_settings()
    data["font_size"] = int(size)
    save_settings(data)
