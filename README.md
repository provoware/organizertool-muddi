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
python -m organizertool.ui.main
```

## Projektstruktur

- `src/organizertool/ui/main.py`: Basis-GUI mit Header und Sidebar
- `src/organizertool/ui/modules.py`: Platzhalter für künftige Module
- `TODO-AGENTS.md`: Offene Aufgaben für die Weiterentwicklung
- `todo.txt`: Einfache Aufgabenliste für Benutzer
- `erledigt.txt`: Bereits erledigte Punkte

## Geplante Module

- Dateinamen nach Begriffen durchsuchen
- Text in Dateien finden
- Bestimmte Dateitypen auflisten (optional rekursiv)
- Dateien nach Kategorien wie Text oder Video sortieren
- Mediendateien konvertieren
- Informationen zu Aliasen und Tastenkombinationen anzeigen

## Hinweise für Laien

- "GUI" steht für *Graphical User Interface* (grafische Benutzeroberfläche)
- "Modul" bedeutet eine Programmeinheit, die eine bestimmte Aufgabe erfüllt

Weitere Vorschläge findest du in `todo.txt`.

## Weitere Laienvorschläge

- Nach der Installation kannst du mit `deactivate` die virtuelle Umgebung verlassen.
- Mit `git pull` aktualisierst du den Code ("Repository" = Projektablage).
- Falls ein Begriff unklar ist, schau in die Klammern: Ein *Module* ist z.B. ein kleines Teilprogramm.
- Mit `python -m pip list` siehst du alle installierten Pakete (Pakete = Bibliotheken).
- Zum Beenden des Programms drückst du `Ctrl+C` (Strg+C, beendet den laufenden Prozess).
