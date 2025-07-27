from __future__ import annotations

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QDockWidget,
    QMainWindow,
    QToolBar,
    QWidget,
    QVBoxLayout,
)
from PySide6.QtCore import Qt

from .modules import (
    BaseModule,
    FileNameSearchModule,
    TextSearchModule,
    FileTypeSearchModule,
    MediaConvertModule,
    AliasInfoModule,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Organizer Tool")
        self.resize(800, 600)

        # Header dashboard using a toolbar
        toolbar = QToolBar("Dashboard")
        toolbar.setMovable(False)
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        toolbar.addWidget(QLabel("Hauptübersicht"))

        # Central area lists all loaded modules
        central = QWidget()
        self.central_layout = QVBoxLayout()
        central.setLayout(self.central_layout)
        self.setCentralWidget(central)

        self.load_modules()

        # Right sidebar as dock widget (aufklappbar)
        sidebar = QDockWidget("Sidebar", self)
        sidebar.setAllowedAreas(Qt.RightDockWidgetArea)
        sidebar.setWidget(QLabel("Inhalt der Sidebar"))
        self.addDockWidget(Qt.RightDockWidgetArea, sidebar)
        sidebar.setVisible(False)

        # Toggle sidebar via header label click (simple example)
        toolbar.widgetForAction(toolbar.actions()[0]).mousePressEvent = lambda event: sidebar.setVisible(not sidebar.isVisible())

    def load_modules(self) -> None:
        """Create placeholder modules and show them."""
        modules = [
            BaseModule.create_dummy("Systemaufräumung"),
            BaseModule.create_dummy("Duplikatsuche"),
            FileNameSearchModule.create(),
            TextSearchModule.create(),
            FileTypeSearchModule.create(),
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

