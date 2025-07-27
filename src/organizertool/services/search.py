import asyncio
import json
import os
from typing import Dict, Iterable, List, Optional


def iter_files(directory: str, recursive: bool = True) -> Iterable[str]:
    """Yield all file paths under ``directory``."""

    for root, dirs, files in os.walk(directory):
        for fname in files:
            yield os.path.join(root, fname)
        if not recursive:
            break


async def search_filenames(directory: str, word: str, recursive: bool = True) -> List[str]:
    """Search for filenames containing ``word``."""

    def scan() -> List[str]:
        matches: List[str] = []
        for path in iter_files(directory, recursive):
            if word.lower() in os.path.basename(path).lower():
                matches.append(path)
        return matches

    return await asyncio.to_thread(scan)


async def search_text(directory: str, word: str, recursive: bool = True) -> Dict[str, List[int]]:
    """Search inside text files for ``word`` occurrences."""

    def scan() -> Dict[str, List[int]]:
        results: Dict[str, List[int]] = {}
        for path in iter_files(directory, recursive):
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                for idx, line in enumerate(lines, 1):
                    if word.lower() in line.lower():
                        results.setdefault(path, []).append(idx)
            except Exception:
                continue
        return results

    return await asyncio.to_thread(scan)


async def list_filetypes(directory: str, extensions: List[str], recursive: bool = True) -> List[str]:
    """List files with the given extensions."""

    def scan() -> List[str]:
        results: List[str] = []
        ext_set = {e.lower() for e in extensions}
        for path in iter_files(directory, recursive):
            if any(path.lower().endswith(e) for e in ext_set):
                results.append(path)
        return results

    return await asyncio.to_thread(scan)


FILE_CATEGORIES: Dict[str, List[str]] = {
    "text": [".txt", ".md", ".rst"],
    "video": [".mp4", ".avi", ".mkv"],
    "image": [".jpg", ".png", ".gif"],
}


def load_categories() -> Dict[str, List[str]]:
    """Return categories from JSON file defined in ``ORGANIZER_CATEGORIES``.

    The environment variable should point to a JSON file with a mapping of
    category names to lists of file extensions. If the variable is not set,
    ``FILE_CATEGORIES`` is returned.
    """

    cfg_path = os.getenv("ORGANIZER_CATEGORIES")
    if not cfg_path:
        return FILE_CATEGORIES
    try:
        with open(cfg_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return {str(k): list(map(str, v)) for k, v in data.items()}
    except Exception:
        pass
    return FILE_CATEGORIES


async def categorize_files(
    directory: str,
    recursive: bool = True,
    categories: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, List[str]]:
    """Return files grouped by categories.

    If ``categories`` is ``None``, the categories are loaded via
    :func:`load_categories`.
    """

    cats = categories or load_categories()

    def scan() -> Dict[str, List[str]]:
        results: Dict[str, List[str]] = {cat: [] for cat in cats}
        for path in iter_files(directory, recursive):
            for cat, exts in cats.items():
                if any(path.lower().endswith(e) for e in exts):
                    results[cat].append(path)
        return results

    return await asyncio.to_thread(scan)
