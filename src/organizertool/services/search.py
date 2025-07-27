import asyncio
import os
from typing import List, Dict


async def search_filenames(directory: str, word: str, recursive: bool = True) -> List[str]:
    """Search for filenames containing the word."""

    def scan() -> List[str]:
        matches: List[str] = []
        for root, dirs, files in os.walk(directory):
            for name in files:
                if word.lower() in name.lower():
                    matches.append(os.path.join(root, name))
            if not recursive:
                break
        return matches

    return await asyncio.to_thread(scan)


async def search_text(directory: str, word: str, recursive: bool = True) -> Dict[str, List[int]]:
    """Search for word occurrences inside text files."""

    def scan() -> Dict[str, List[int]]:
        results: Dict[str, List[int]] = {}
        for root, dirs, files in os.walk(directory):
            for fname in files:
                path = os.path.join(root, fname)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                    for idx, line in enumerate(lines, 1):
                        if word.lower() in line.lower():
                            results.setdefault(path, []).append(idx)
                except Exception:
                    continue
            if not recursive:
                break
        return results

    return await asyncio.to_thread(scan)


async def list_filetypes(directory: str, extensions: List[str], recursive: bool = True) -> List[str]:
    """List files with given extensions."""

    def scan() -> List[str]:
        results: List[str] = []
        ext_set = {e.lower() for e in extensions}
        for root, dirs, files in os.walk(directory):
            for fname in files:
                if any(fname.lower().endswith(e) for e in ext_set):
                    results.append(os.path.join(root, fname))
            if not recursive:
                break
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
        for root, dirs, files in os.walk(directory):
            for fname in files:
                for cat, exts in FILE_CATEGORIES.items():
                    if any(fname.lower().endswith(e) for e in exts):
                        results[cat].append(os.path.join(root, fname))
            if not recursive:
                break
        return results

    return await asyncio.to_thread(scan)
