from organizertool.ui.theme import (
    get_current_theme,
    set_current_theme,
    THEMES,
)
from organizertool.core.settings import load_settings


def test_get_current_theme_default(monkeypatch):
    monkeypatch.delenv("ORGANIZER_THEME", raising=False)
    assert get_current_theme() == THEMES["dark"]


def test_get_current_theme_custom(monkeypatch):
    monkeypatch.setenv("ORGANIZER_THEME", "light")
    assert get_current_theme() == THEMES["light"]


def test_set_current_theme(tmp_path, monkeypatch):
    settings_file = tmp_path / "cfg.json"
    monkeypatch.setenv("ORGANIZER_SETTINGS", str(settings_file))
    monkeypatch.delenv("ORGANIZER_THEME", raising=False)

    set_current_theme("blue")
    assert load_settings()["theme"] == "blue"
    assert get_current_theme() == THEMES["blue"]
