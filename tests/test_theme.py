from organizertool.ui.theme import (
    get_current_theme,
    set_current_theme,
    get_current_font_size,
    set_current_font_size,
    THEMES,
)
from organizertool.core.settings import load_settings
from organizertool.core.constants import DEFAULT_FONT_SIZE


def test_get_current_theme_default(monkeypatch):
    monkeypatch.delenv("ORGANIZER_THEME", raising=False)
    assert get_current_theme().startswith(THEMES["dark"])


def test_get_current_theme_custom(monkeypatch):
    monkeypatch.setenv("ORGANIZER_THEME", "light")
    assert get_current_theme().startswith(THEMES["light"])


def test_set_current_theme(tmp_path, monkeypatch):
    settings_file = tmp_path / "cfg.json"
    monkeypatch.setenv("ORGANIZER_SETTINGS", str(settings_file))
    monkeypatch.delenv("ORGANIZER_THEME", raising=False)

    set_current_theme("blue")
    assert load_settings()["theme"] == "blue"
    assert get_current_theme().startswith(THEMES["blue"])


def test_get_current_font_size_default(monkeypatch):
    monkeypatch.delenv("ORGANIZER_FONT_SIZE", raising=False)
    assert get_current_font_size() == DEFAULT_FONT_SIZE


def test_set_current_font_size(tmp_path, monkeypatch):
    settings_file = tmp_path / "cfg.json"
    monkeypatch.setenv("ORGANIZER_SETTINGS", str(settings_file))
    monkeypatch.delenv("ORGANIZER_FONT_SIZE", raising=False)

    set_current_font_size(15)
    assert load_settings()["font_size"] == 15
    assert "font-size: 15pt" in get_current_theme()
