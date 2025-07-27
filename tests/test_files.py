import pytest

from organizertool.core.files import iter_files


def test_iter_files_nonexistent(tmp_path):
    missing = tmp_path / "not_here"
    with pytest.raises(FileNotFoundError):
        list(iter_files(str(missing)))
