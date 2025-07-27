from organizertool.ui.theme import get_current_theme, THEMES


def test_get_current_theme_default(monkeypatch):
    monkeypatch.delenv("ORGANIZER_THEME", raising=False)
    assert get_current_theme() == THEMES["dark"]


def test_get_current_theme_custom(monkeypatch):
    monkeypatch.setenv("ORGANIZER_THEME", "light")
    assert get_current_theme() == THEMES["light"]
