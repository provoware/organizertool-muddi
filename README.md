# Organizer Tool Muddi

Dieses Projekt soll ein modular aufgebautes Werkzeug für Linux bereitstellen. Es enthält eine grafische Hauptoberfläche mit Header und einklappbarer Sidebar.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Starten

```bash
python -m organizertool.gui
```

## Projektstruktur

- `src/organizertool/gui.py`: Basis-GUI mit Header und Sidebar
- `TODO-AGENTS.md`: Offene Aufgaben für die Weiterentwicklung
- `todo.txt`: Einfache Aufgabenliste für Benutzer
- `erledigt.txt`: Bereits erledigte Punkte

## Hinweise für Laien

- "GUI" steht für *Graphical User Interface* (grafische Benutzeroberfläche)
- "Modul" bedeutet eine Programmeinheit, die eine bestimmte Aufgabe erfüllt

Weitere Vorschläge findest du in `todo.txt`.
