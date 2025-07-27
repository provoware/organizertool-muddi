"""Utility functions around file handling."""

from __future__ import annotations

import os
from typing import Iterable


def iter_files(directory: str, recursive: bool = True) -> Iterable[str]:
    """Yield all file paths unter (unter = inside) ``directory``."""

    for root, dirs, files in os.walk(directory):
        for fname in files:
            yield os.path.join(root, fname)
        if not recursive:
            break


__all__ = ["iter_files"]
