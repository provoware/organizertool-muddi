"""Organizer Tool main package."""

__version__ = "1.0.2"

from .services.hooks import run_with_retry
from .services.trash import safe_remove


def run_app() -> None:
    """Start the GUI application."""

    from .ui.main import run_app as _run_app

    _run_app()


def create_main_window():
    """Return the main window class for embedding."""

    from .ui.main import MainWindow

    return MainWindow()


__all__ = ["run_app", "create_main_window", "__version__", "run_with_retry", "safe_remove"]
