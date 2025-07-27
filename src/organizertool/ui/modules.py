from __future__ import annotations

from dataclasses import dataclass
import asyncio
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from ..services import (
    search_filenames,
    search_text,
    list_filetypes,
    categorize_files,
    load_categories,
)


data_view = QLabel


@dataclass
class BaseModule:
    """Simple container for Module information."""

    name: str
    widget: QWidget

    @classmethod
    def create_dummy(cls, name: str) -> "BaseModule":
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Modul {name} in Arbeit"))
        widget.setLayout(layout)
        return cls(name=name, widget=widget)


class FileNameSearchModule(BaseModule):
    """Show files that contain a word in their Namen."""

    @classmethod
    def create(cls, directory: str = ".", word: str = "test") -> "FileNameSearchModule":
        matches = asyncio.run(search_filenames(directory, word))
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Treffer f\u00fcr '{word}':"))
        for path in matches:
            layout.addWidget(QLabel(path))
        if not matches:
            layout.addWidget(QLabel("Keine Treffer"))
        widget.setLayout(layout)
        return cls(name="Dateinamen-Suche", widget=widget)


class TextSearchModule(BaseModule):
    """Search for a word in textdateien."""

    @classmethod
    def create(cls, directory: str = ".", word: str = "example") -> "TextSearchModule":
        results = asyncio.run(search_text(directory, word))
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Fundstellen f\u00fcr '{word}':"))
        for path, lines in results.items():
            layout.addWidget(QLabel(f"{path}: Zeilen {', '.join(map(str, lines))}"))
        if not results:
            layout.addWidget(QLabel("Keine Treffer"))
        widget.setLayout(layout)
        return cls(name="Textsuche", widget=widget)


class FileTypeSearchModule(BaseModule):
    """Listet Dateien nach Endungen."""

    @classmethod
    def create(cls, directory: str = ".", extensions: list[str] | None = None) -> "FileTypeSearchModule":
        if extensions is None:
            extensions = [".py"]
        matches = asyncio.run(list_filetypes(directory, extensions))
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Dateien mit {', '.join(extensions)}:"))
        for path in matches:
            layout.addWidget(QLabel(path))
        if not matches:
            layout.addWidget(QLabel("Keine Treffer"))
        widget.setLayout(layout)
        return cls(name="Dateitypen-Suche", widget=widget)


class CategoryModule(BaseModule):
    """Zeigt Dateien nach vordefinierten Kategorien."""

    @classmethod
    def create(cls, directory: str = ".") -> "CategoryModule":
        categories = asyncio.run(categorize_files(directory, categories=load_categories()))
        widget = QWidget()
        layout = QVBoxLayout()
        for cat, files in categories.items():
            layout.addWidget(QLabel(f"Kategorie {cat}:"))
            for f in files:
                layout.addWidget(QLabel(f"  {f}"))
            if not files:
                layout.addWidget(QLabel("  Keine Treffer"))
        widget.setLayout(layout)
        return cls(name="Dateikategorien", widget=widget)


class MediaConvertModule(BaseModule):
    """Placeholder for media conversion."""

    @classmethod
    def create(cls) -> "MediaConvertModule":
        return cls.create_dummy("Mediendateien konvertieren")


class AliasInfoModule(BaseModule):
    """Display useful shell aliases and keyboard shortcuts."""

    ALIASES = {
        "ll": "ls -la  # zeigt Dateien mit Details",
        "gs": "git status  # aktuellen Git-Zustand anzeigen",
    }

    SHORTCUTS = {
        "Ctrl+C": "bricht laufenden Prozess ab",
        "Ctrl+Shift+T": "öffnet neues Terminalfenster",
    }

    @classmethod
    def create(cls) -> "AliasInfoModule":
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Aliase (kurze Befehle):"))
        for name, desc in cls.ALIASES.items():
            layout.addWidget(QLabel(f"{name}: {desc}"))

        layout.addWidget(QLabel("Tastenkombinationen:"))
        for combo, desc in cls.SHORTCUTS.items():
            layout.addWidget(QLabel(f"{combo}: {desc}"))

        widget.setLayout(layout)
        return cls(name="Alias- und Tastenkombis", widget=widget)


__all__ = [
    "BaseModule",
    "FileNameSearchModule",
    "TextSearchModule",
    "FileTypeSearchModule",
    "CategoryModule",
    "MediaConvertModule",
    "AliasInfoModule",
]
