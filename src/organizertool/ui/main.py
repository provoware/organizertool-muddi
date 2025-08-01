from __future__ import annotations

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QDockWidget,
    QMainWindow,
    QToolBar,
    QWidget,
    QVBoxLayout,
    QComboBox,
)
from PySide6.QtCore import Qt

from .theme import (
    get_current_theme,
    set_current_theme,
    THEMES,
    get_current_theme_name,
    get_current_font_size,
    set_current_font_size,
)

from .modules import (
    BaseModule,
    FileNameSearchModule,
    TextSearchModule,
    FileTypeSearchModule,
    CategoryModule,
    MediaConvertModule,
    AliasInfoModule,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Organizer Tool")
        self.resize(800, 600)

        # Apply theme from environment variable ORGANIZER_THEME
        # Available themes: dark, light, blue, contrast
        self.setStyleSheet(get_current_theme())

        # Header dashboard using a toolbar
        toolbar = QToolBar("Dashboard")
        toolbar.setMovable(False)
        self.addToolBar(Qt.TopToolBarArea, toolbar)  # type: ignore[attr-defined]
        toolbar.addWidget(QLabel("Hauptübersicht"))

        theme_box = QComboBox()
        for name in THEMES:
            theme_box.addItem(name)
        theme_box.setCurrentText(get_current_theme_name())
        theme_box.currentTextChanged.connect(self.change_theme)
        toolbar.addWidget(theme_box)

        font_box = QComboBox()
        for size in ["8", "10", "12", "14", "16", "18", "20"]:
            font_box.addItem(size)
        font_box.setCurrentText(str(get_current_font_size()))
        font_box.currentTextChanged.connect(self.change_font_size)
        toolbar.addWidget(font_box)

        # Central area lists all loaded modules
        central = QWidget()
        self.central_layout = QVBoxLayout()
        central.setLayout(self.central_layout)
        self.setCentralWidget(central)

        self.load_modules()

        # Right sidebar as dock widget (aufklappbar)
        self.sidebar = QDockWidget("Sidebar", self)
        self.sidebar.setAllowedAreas(Qt.RightDockWidgetArea)  # type: ignore[attr-defined]
        self.sidebar.setWidget(QLabel("Inhalt der Sidebar"))
        self.addDockWidget(Qt.RightDockWidgetArea, self.sidebar)  # type: ignore[attr-defined]
        self.sidebar.setVisible(False)

        # simple status bar for user feedback
        self.statusBar().showMessage("Bereit")

        # Toggle sidebar via header label click (simple example)
        action = toolbar.actions()[0]

        def _toggle(_: object) -> None:
            self.sidebar.setVisible(not self.sidebar.isVisible())

        toolbar.widgetForAction(action).mousePressEvent = _toggle  # type: ignore[assignment]

    def change_theme(self, name: str) -> None:
        """Apply and persist selected theme."""

        set_current_theme(name)
        self.setStyleSheet(get_current_theme())
        self.statusBar().showMessage(f"Theme gewechselt zu {name}", 2000)

    def change_font_size(self, size: str) -> None:
        """Adjust and persist the font size."""

        try:
            value = int(size)
        except ValueError:
            value = get_current_font_size()
        set_current_font_size(value)
        self.setStyleSheet(get_current_theme())
        self.statusBar().showMessage(f"Schriftgröße gesetzt auf {value}", 2000)

    def resizeEvent(self, event) -> None:  # type: ignore[override]
        """Auto-hide sidebar on small window widths."""
        if self.width() < 600:
            self.sidebar.setVisible(False)
        super().resizeEvent(event)

    def load_modules(self) -> None:
        """Create placeholder modules and show them."""
        modules = [
            BaseModule.create_dummy("Systemaufräumung"),
            BaseModule.create_dummy("Duplikatsuche"),
            FileNameSearchModule.create(),
            TextSearchModule.create(),
            FileTypeSearchModule.create(),
            CategoryModule.create(),
            MediaConvertModule.create(),
            AliasInfoModule.create(),
        ]
        for mod in modules:
            self.central_layout.addWidget(mod.widget)


def run_app() -> None:
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    run_app()
