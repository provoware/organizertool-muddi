from unittest import mock

from organizertool.services.trash import safe_remove


def test_safe_remove_calls_send2trash(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("x")
    with mock.patch("organizertool.services.trash.send2trash") as m:
        safe_remove(str(file))
        m.assert_called_once_with(str(file))


def test_safe_remove_missing(tmp_path):
    missing = tmp_path / "not_here"
    with mock.patch("organizertool.services.trash.send2trash") as m:
        try:
            safe_remove(str(missing))
        except FileNotFoundError:
            pass
        else:
            assert False, "Expected FileNotFoundError"
        m.assert_not_called()
