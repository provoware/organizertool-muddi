import asyncio
import subprocess
from typing import Tuple
import sys


async def check_dependencies() -> Tuple[str, str]:
    """Return the output of ``pip check``.

    This runs ``python -m pip check`` in a separate thread and
    captures stdout and stderr.
    """

    def run_check() -> Tuple[str, str]:
        proc = subprocess.run(
            ["python", "-m", "pip", "check"],
            capture_output=True,
            text=True,
        )
        return proc.stdout, proc.stderr

    return await asyncio.to_thread(run_check)


if __name__ == "__main__":
    out, err = asyncio.run(check_dependencies())
    if out:
        print(out)
    if err:
        print(err, file=sys.stderr)
