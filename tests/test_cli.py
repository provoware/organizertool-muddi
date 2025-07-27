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
