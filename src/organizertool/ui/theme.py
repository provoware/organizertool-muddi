"""Simple themes for the GUI."""

from __future__ import annotations

import os

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


def get_current_theme() -> str:
    """Return stylesheet for theme from ORGANIZER_THEME variable."""

    name = os.getenv("ORGANIZER_THEME", DEFAULT_THEME).lower()
    return THEMES.get(name, THEMES[DEFAULT_THEME])
