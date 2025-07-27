import argparse
import asyncio
from typing import List
from pathlib import Path
import os
import sys

from . import __version__, run_app
from .services import search
from .core.settings import get_settings_path, save_settings
from .core.constants import ENV_CATEGORIES


def _search_names(args: argparse.Namespace) -> None:
    results = asyncio.run(
        search.search_filenames(
            args.directory,
            args.word,
            recursive=not args.no_recursive,
        )
    )
    for path in results:
        print(path)


def _show_tips(_: argparse.Namespace) -> None:
    """Print beginner tips from todo.txt."""

    root = Path(__file__).resolve().parents[2]
    todo = root / "todo.txt"
    try:
        text = todo.read_text(encoding="utf-8")
    except OSError:
        print("Tip-Datei nicht gefunden")
        return
    print(text)


def _diagnose(_: argparse.Namespace) -> None:
    """Simple environment check mit Selbstreparatur."""

    print("Starte Diagnose...")
    settings_path = get_settings_path()
    if settings_path.exists():
        print(f"Einstellungsdatei gefunden: {settings_path}")
    else:
        print(f"Einstellungsdatei fehlt, erstelle {settings_path}")
        save_settings({})
    cat_file = os.getenv(ENV_CATEGORIES)
    if cat_file:
        if os.path.exists(cat_file):
            print(f"Kategorien-Datei gefunden: {cat_file}")
        else:
            print(f"Achtung: Kategorien-Datei nicht gefunden: {cat_file}")
    else:
        print("Keine Kategorien-Datei gesetzt (ORGANIZER_CATEGORIES)")
    version = ".".join(map(str, sys.version_info[:3]))
    print(f"Python-Version: {version}")


def _search_text(args: argparse.Namespace) -> None:
    results = asyncio.run(
        search.search_text(
            args.directory,
            args.word,
            recursive=not args.no_recursive,
        )
    )
    for path, lines in results.items():
        line_list = ", ".join(map(str, lines))
        print(f"{path}: {line_list}")


def _list_types(args: argparse.Namespace) -> None:
    results = asyncio.run(
        search.list_filetypes(
            args.directory,
            args.extensions,
            recursive=not args.no_recursive,
        )
    )
    for path in results:
        print(path)


def main(argv: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Organizer Tool Kommandozeile")
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
        help="Version anzeigen",
    )
    sub = parser.add_subparsers(dest="cmd")

    gui_p = sub.add_parser("gui", help="Grafische Oberfläche starten")
    gui_p.set_defaults(func=lambda args: run_app())

    names_p = sub.add_parser("search-name", help="Nach Dateinamen suchen")
    names_p.add_argument("directory", help="Ordner, in dem gesucht wird")
    names_p.add_argument("word", help="Suchbegriff im Dateinamen")
    names_p.add_argument(
        "--no-recursive",
        action="store_true",
        help="nicht rekursiv suchen",
    )
    names_p.set_defaults(func=_search_names)

    text_p = sub.add_parser("search-text", help="In Dateien nach Text suchen")
    text_p.add_argument("directory", help="Ordner, in dem gesucht wird")
    text_p.add_argument("word", help="Suchbegriff im Text")
    text_p.add_argument(
        "--no-recursive",
        action="store_true",
        help="nicht rekursiv suchen",
    )
    text_p.set_defaults(func=_search_text)

    types_p = sub.add_parser("list-types", help="Dateien nach Endung auflisten")
    types_p.add_argument("directory", help="Ordner, in dem gesucht wird")
    types_p.add_argument("extensions", nargs="+", help="Dateiendungen")
    types_p.add_argument(
        "--no-recursive",
        action="store_true",
        help="nicht rekursiv suchen",
    )
    types_p.set_defaults(func=_list_types)

    tips_p = sub.add_parser("tips", help="Tipps für Einsteiger anzeigen")
    tips_p.set_defaults(func=_show_tips)

    diag_p = sub.add_parser("diagnose", help="Umgebung prüfen und reparieren")
    diag_p.set_defaults(func=_diagnose)

    args = parser.parse_args(argv)
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        print("Tipp: Mehr Hinweise mit 'python -m organizertool tips'")


if __name__ == "__main__":
    main()
