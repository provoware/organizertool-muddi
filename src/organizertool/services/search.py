import asyncio
import os
from typing import Dict, Iterable, List


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


async def categorize_files(directory: str, recursive: bool = True) -> Dict[str, List[str]]:
    """Return files grouped by predefined categories."""

    def scan() -> Dict[str, List[str]]:
        results: Dict[str, List[str]] = {cat: [] for cat in FILE_CATEGORIES}
        for path in iter_files(directory, recursive):
            for cat, exts in FILE_CATEGORIES.items():
                if any(path.lower().endswith(e) for e in exts):
                    results[cat].append(path)
        return results

    return await asyncio.to_thread(scan)
