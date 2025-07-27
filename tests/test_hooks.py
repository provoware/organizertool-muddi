import asyncio
import pytest

from organizertool.services.hooks import run_with_retry


@pytest.mark.asyncio
async def test_run_with_retry_success():
    counter = {"n": 0}

    async def sometimes_fail() -> str:
        counter["n"] += 1
        if counter["n"] < 2:
            raise RuntimeError("fail")
        return "ok"

    result = await run_with_retry(sometimes_fail, retries=2)
    assert result == "ok"


@pytest.mark.asyncio
async def test_run_with_retry_abort():
    async def task() -> str:
        return "value"

    def should_abort() -> bool:
        return True

    with pytest.raises(asyncio.CancelledError):
        await run_with_retry(task, should_abort=should_abort)
