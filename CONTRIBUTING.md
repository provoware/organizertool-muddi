# Beitragende willkommen

Dieses Projekt soll leicht erweiterbar sein. Folge diesen Schritten, um eigene Verbesserungen einzureichen:

1. **Virtuelle Umgebung** ("virtual environment" = isolierte Python-Umgebung) erstellen und aktivieren:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install pytest flake8 pytest-asyncio mypy black
   ```
2. **Code formatieren**:
   ```bash
   make fmt
   ```
3. **Tests, Linter und Typprüfung** ("Lint" = Code-Prüfung, "Type Check" = Typenprüfung) zusammen starten:
   ```bash
   make check
   ```
4. **Abhängigkeiten prüfen** ("Dependency Check" = Paketkontrolle):
   ```bash
   make deps
   ```
5. Reiche Änderungen über einen Pull Request ein.

Weitere Hinweise stehen in der Datei `README.md`.
