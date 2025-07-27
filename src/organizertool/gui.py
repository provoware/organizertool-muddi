from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QDockWidget, QLabel, QToolBar, QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt


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

        # Central placeholder
        central = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(QLabel("Hier kommen Module hin"))
        central.setLayout(central_layout)
        self.setCentralWidget(central)

        # Right sidebar as dock widget
        sidebar = QDockWidget("Sidebar", self)
        sidebar.setAllowedAreas(Qt.RightDockWidgetArea)
        sidebar.setWidget(QLabel("Inhalt der Sidebar"))
        self.addDockWidget(Qt.RightDockWidgetArea, sidebar)
        sidebar.setVisible(False)

        # Toggle sidebar via header label click (simple example)
        toolbar.widgetForAction(toolbar.actions()[0]).mousePressEvent = lambda event: sidebar.setVisible(not sidebar.isVisible())


def run_app() -> None:
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    run_app()
