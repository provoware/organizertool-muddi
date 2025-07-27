# Organizer Tool Muddi

Dieses Projekt soll ein modular aufgebautes Werkzeug für Linux bereitstellen. Es enthält eine grafische Hauptoberfläche mit Header und einklappbarer Sidebar.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Für Entwickler empfiehlt sich die Installation zusätzlicher Werkzeuge:

```bash
pip install pytest flake8
```

## Starten

```bash
python -m organizertool.ui.main
```

Tests führst du so aus ("Test" = automatische Überprüfung):

```bash
pytest
```

Den Stil des Codes prüfst du mit `flake8` ("Linter" = Programm, das auf Fehler hinweist):

```bash
flake8 src/organizertool
```

Um einzelne Module im Python-Interpreter zu testen, kannst du Folgendes eingeben:

```bash
python
>>> from organizertool.ui.modules import FileNameSearchModule
>>> mod = FileNameSearchModule.create('.', 'demo')
```

## Projektstruktur

- `src/organizertool/ui/main.py`: Basis-GUI mit Header und Sidebar
- `src/organizertool/ui/modules.py`: Enthält Module wie Dateisuche
- `src/organizertool/services/search.py`: Asynchrone (nebenläufige) Suchfunktionen
- `TODO-AGENTS.md`: Offene Aufgaben für die Weiterentwicklung
- `todo.txt`: Einfache Aufgabenliste für Benutzer
- `erledigt.txt`: Bereits erledigte Punkte

## Geplante Module

Einige einfache Module sind bereits enthalten, z.B. die Suche nach Dateinamen
und Text. Zukünftig sollen folgende Funktionen ausgebaut werden:

- Dateinamen nach Begriffen durchsuchen
- Text in Dateien finden
- Bestimmte Dateitypen auflisten (optional rekursiv)
- Dateien nach Kategorien wie Text oder Video sortieren
- Mediendateien konvertieren
- Informationen zu Aliasen und Tastenkombinationen anzeigen

## Hinweise für Laien

- "GUI" steht für *Graphical User Interface* (grafische Benutzeroberfläche)
- "Modul" bedeutet eine Programmeinheit, die eine bestimmte Aufgabe erfüllt
- "Interpreter" ist ein Programm, das Befehle direkt ausführt (hier: `python`)
- "Asynchron" bedeutet, dass Aufgaben gleichzeitig laufen können (nebenläufig)

Weitere Vorschläge findest du in `todo.txt`.

## Weitere Laienvorschläge

- Nach der Installation kannst du mit `deactivate` die virtuelle Umgebung verlassen.
- Mit `git pull` aktualisierst du den Code ("Repository" = Projektablage).
- Falls ein Begriff unklar ist, schau in die Klammern: Ein *Module* ist z.B. ein kleines Teilprogramm.
- Mit `python -m pip list` siehst du alle installierten Pakete (Pakete = Bibliotheken).
- Zum Beenden des Programms drückst du `Ctrl+C` (Strg+C, beendet den laufenden Prozess).
- Mit `ls` listest du Dateien im aktuellen Ordner auf (Ordner = Directory).
- `pwd` zeigt dir den aktuellen Pfad (Pfad = Directory-Name) an.
- Um nach einem anderen Begriff zu suchen, passe die Parameter in den Modulen an, z.B. `FileNameSearchModule.create('.', 'mein_wort')`.
- Mit `pytest` führst du automatische Tests aus ("Tests" prüfen Funktionen).
- `flake8` prüft die Code-Qualität und weist auf Formatierungsfehler hin ("Linter").
