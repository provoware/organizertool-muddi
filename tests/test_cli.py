import subprocess
import sys
from organizertool import __version__


def test_cli_version():
    result = subprocess.run(
        [sys.executable, "-m", "organizertool", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert __version__ in result.stdout


def test_cli_tips():
    result = subprocess.run(
        [sys.executable, "-m", "organizertool", "tips"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Systemaufr\xe4umung" in result.stdout
