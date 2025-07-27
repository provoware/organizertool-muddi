from __future__ import annotations

from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


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
    """Placeholder for searching words in filenames."""

    @classmethod
    def create(cls) -> "FileNameSearchModule":
        return cls.create_dummy("Dateinamen-Suche")


class TextSearchModule(BaseModule):
    """Placeholder for searching text inside files."""

    @classmethod
    def create(cls) -> "TextSearchModule":
        return cls.create_dummy("Textsuche")


class FileTypeSearchModule(BaseModule):
    """Placeholder for finding specific file types."""

    @classmethod
    def create(cls) -> "FileTypeSearchModule":
        return cls.create_dummy("Dateitypen-Suche")


class MediaConvertModule(BaseModule):
    """Placeholder for media conversion."""

    @classmethod
    def create(cls) -> "MediaConvertModule":
        return cls.create_dummy("Mediendateien konvertieren")


class AliasInfoModule(BaseModule):
    """Placeholder for showing alias and shortcut information."""

    @classmethod
    def create(cls) -> "AliasInfoModule":
        return cls.create_dummy("Alias- und Tastenkombi-Info")

