# Organizer Tool Muddi

Dieses Projekt soll ein modular aufgebautes Werkzeug für Linux bereitstellen. Es enthält eine grafische Hauptoberfläche mit Header und einklappbarer Sidebar.
Den aktuellen Fortschritt findest du in der Datei `STATUS.md`.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Für Entwickler empfiehlt sich die Installation zusätzlicher Werkzeuge:

```bash
pip install pytest flake8 pytest-asyncio
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
Die Formatierung übernimmst du mit `black` ("Formatter" = automatisches Formatieren des Codes):

```bash
black src/organizertool tests
```

Die Typen checkst du mit `mypy` ("Type Checker" = Programm, das auf passende Datentypen achtet):

```bash
mypy src/organizertool tests
```
Mit `make check` fuehrst du Tests und Lint in einem Schritt aus:

```bash
make check
```

Installierte Pakete kannst du überprüfen ("Dependency Check" = Kontrolle der Abhängigkeiten):

```bash
make deps
```

## Kommandozeile (CLI)

Mit einem einfachen Kommando kannst du die grafische Oberfläche oder Suchbefehle
starten. "CLI" steht für *Command Line Interface* (Befehlszeile).

GUI öffnen:

```bash
python -m organizertool gui
```

Dateien nach Namen durchsuchen:

```bash
python -m organizertool search-name ORDNER suchwort
```

Text in Dateien finden:

```bash
python -m organizertool search-text ORDNER suchwort
```

Dateien nach Endung auflisten:

```bash
python -m organizertool list-types ORDNER .py .txt
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

### Eigene Kategorien definieren

Lege eine Datei `categories.json` an und fülle sie so:

```json
{
  "dokumente": [".pdf", ".docx"],
  "python": [".py"]
}
```

Setze dann die Umgebungsvariable ("Environment Variable" = Systemeinstellung)
`ORGANIZER_CATEGORIES` auf den Pfad dieser Datei, zum Beispiel:

```bash
export ORGANIZER_CATEGORIES=/pfad/zur/categories.json
```

Starte danach die GUI erneut, um deine Kategorien zu sehen.

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
- `black` formatiert den Code automatisch ("Formatter" = Formatierungswerkzeug).
- `mypy` kontrolliert die Typangaben ("Type Checker" = Programm für Datentypen).
- `python -m organizertool.ui.main` startet die grafische Oberfläche.
- Mit `python -m pip install -U -r requirements.txt` aktualisierst du alle Pakete (Pakete = Bibliotheken).
- `make deps` überprüft installierte Pakete ("Dependency Check" = Kontrolle der Abhängigkeiten).
- Die Farben der Oberfläche stellst du über die Umgebungsvariable `ORGANIZER_THEME` ein. Vier Themes (Farbvorlagen) sind vorhanden: `dark`, `light`, `blue` und `contrast`.
Beispiel:
```bash
export ORGANIZER_THEME=light
```
- Du kannst das Theme auch direkt in der GUI über ein Auswahlfeld ändern. Die
  Auswahl wird in `~/.organizertool/settings.json` gespeichert ("Settings-Datei" = Ablage für Einstellungen).
- Mit der Variablen `ORGANIZER_SETTINGS` kannst du den Ort dieser Datei ändern.
- Die Sidebar blendest du durch Klick auf "Hauptübersicht" ein oder aus.
- Bei schmalem Fenster versteckt sich die Sidebar automatisch.
- Starte das Modul "Alias- und Tastenkombis", um nützliche Kurzbefehle zu sehen.
- Mit `cd ordnername` wechselst du den Ordner ("Directory").
- `mkdir neuer_ordner` legt einen neuen Ordner an ("make directory").
- Drücke `F11`, um die GUI im Vollbild zu sehen ("Fullscreen").
- Mit `history` siehst du vergangene Befehle ("history" = Befehlsverlauf).
- Neue Datei anlegen: `touch meine_datei.txt` ("touch" legt eine leere Datei an).
- Inhalt einer Datei anzeigen: `cat meine_datei.txt` ("cat" zeigt Textdateien an).
- Eine Datei löschen: `rm -i meine_datei.txt` ("rm" l\u00f6scht Dateien, `-i` fragt sicherheitshalber nach).
- Sicher löschen über den Papierkorb:
  ```bash
  python -c "from organizertool import safe_remove; safe_remove('meine_datei.txt')"
  ```
  Dabei wird die Datei in den System-Papierkorb verschoben ("Trash" = Ablage für gelöschte Daten).
- Datei kopieren: `cp quelle ziel` ("cp" = Kopieren einer Datei).
- Datei verschieben oder umbenennen: `mv quelle ziel` ("mv" = Move/Rename).
- Mit `ls -la` siehst du Details zu Dateien ("-la" zeigt versteckte Dateien und Berechtigungen).
- Installierte Pakete mit Versionen speicherst du in `requirements.txt`:
-  ```bash
-  pip freeze > requirements.txt
-  ```
-  Ein Paket für die Veröffentlichung baust du mit:
-  ```bash
-  python -m pip install build
-  python -m build
-  ```
- Anleitung für Mitwirkende findest du in [CONTRIBUTING.md](CONTRIBUTING.md).
- Aktuelle Version anzeigen ("Version" = Programmstand):
  ```bash
  python -c "import organizertool; print(organizertool.__version__)"
  ```
- Änderungen nachschlagen: `cat CHANGELOG.md` ("Changelog" = Liste aller Neuerungen).
- Bei Fehlermeldungen wiederholt die Funktion `run_with_retry` einen Vorgang automatisch ("Retry" = erneuter Versuch).
- Beispiel zum Abbrechen eines Vorgangs:
  ```python
  import asyncio
  from organizertool import run_with_retry

  async def meine_aufgabe():
      raise RuntimeError("kaputt")

  await run_with_retry(meine_aufgabe, retries=3)
  ```
- Unten zeigt eine Statusleiste kurze Hinweise an ("Statusbar" = Leiste am Fensterrand).

