from organizertool.core.settings import load_settings, save_settings


def test_load_save_settings(tmp_path, monkeypatch):
    settings_file = tmp_path / "cfg.json"
    monkeypatch.setenv("ORGANIZER_SETTINGS", str(settings_file))

    data = {"theme": "light"}
    save_settings(data)
    assert settings_file.exists()

    loaded = load_settings()
    assert loaded == data
