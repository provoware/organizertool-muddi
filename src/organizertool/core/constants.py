"""Shared constants and environment variable names."""

from pathlib import Path

# Environment variable names
ENV_SETTINGS = "ORGANIZER_SETTINGS"
"""Name of the variable to override the Pfad(Path) zur Einstellungsdatei."""

ENV_THEME = "ORGANIZER_THEME"
"""Name of the variable zur Wahl des Themes (Farbschema)."""

ENV_FONT_SIZE = "ORGANIZER_FONT_SIZE"
"""Name der Variablen für die Schriftgröße in Punkten."""

ENV_CATEGORIES = "ORGANIZER_CATEGORIES"
"""Name of the Variable, die auf eine JSON-Datei mit Dateikategorien zeigt."""

# Default locations and values
SETTINGS_PATH = Path.home() / ".organizertool" / "settings.json"
"""Standardpfad für gespeicherte Einstellungen."""

DEFAULT_THEME = "dark"
"""Theme, das genutzt wird, falls nichts anderes gesetzt ist."""

DEFAULT_FONT_SIZE = 12
"""Standard-Schriftgröße in Punkten."""

FILE_CATEGORIES = {
    "text": [".txt", ".md", ".rst"],
    "video": [".mp4", ".avi", ".mkv"],
    "image": [".jpg", ".png", ".gif"],
}
"""Vordefinierte Dateikategorien."""

__all__ = [
    "ENV_SETTINGS",
    "ENV_THEME",
    "ENV_FONT_SIZE",
    "ENV_CATEGORIES",
    "SETTINGS_PATH",
    "DEFAULT_THEME",
    "DEFAULT_FONT_SIZE",
    "FILE_CATEGORIES",
]
