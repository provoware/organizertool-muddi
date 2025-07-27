"""Utilities for safe deletion via the system trash."""

from __future__ import annotations

import os
from send2trash import send2trash


def safe_remove(path: str) -> None:
    """Move ``path`` to the system trash instead of deleting it permanently."""

    if not os.path.exists(path):
        raise FileNotFoundError(path)
    send2trash(path)


__all__ = ["safe_remove"]
