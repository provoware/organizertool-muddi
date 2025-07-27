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

