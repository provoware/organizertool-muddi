import asyncio
from typing import Any, Awaitable, Callable, TypeVar, Optional

T = TypeVar("T")


async def run_with_retry(
    func: Callable[..., Awaitable[T]],
    *args: Any,
    retries: int = 3,
    delay: float = 0.1,
    on_error: Optional[Callable[[Exception, int], None]] = None,
    should_abort: Optional[Callable[[], bool]] = None,
) -> T:
    """Run ``func`` and retry on failure.

    Parameters
    ----------
    func:
        Asynchronous function to execute.
    retries:
        Maximum number of attempts.
    delay:
        Seconds to wait between retries.
    on_error:
        Optional callback receiving the exception and attempt number.
    should_abort:
        Optional callback returning ``True`` to cancel the operation.
    """

    for attempt in range(1, retries + 1):
        if should_abort and should_abort():
            raise asyncio.CancelledError()
        try:
            return await func(*args)
        except Exception as exc:  # pragma: no cover - generically handles errors
            if on_error:
                on_error(exc, attempt)
            if attempt >= retries:
                raise
            await asyncio.sleep(delay)
    # should not reach here
    raise RuntimeError("unreachable")
