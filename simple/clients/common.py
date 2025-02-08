
import asyncio
import logging
import time
from functools import wraps
from collections import deque

import aiohttp


logger = logging.getLogger("simple")


class RateLimiter:
    def __init__(self, max_requests=1, time_window=1):
        self.max_requests = max_requests
        self.time_window = time_window
        self.request_times = deque()

    async def maybe_sleep(self):
        while len(self.request_times) >= self.max_requests:
            oldest_time = self.request_times[0]
            time_delta = time.monotonic() - oldest_time

            if time_delta >= self.time_window:
                self.request_times.popleft()
            else:
                await asyncio.sleep(self.time_window - time_delta)

    def add_request_time(self):
        self.request_times.append(time.monotonic())


def retrying(method):
    @wraps(method)
    async def wrapper(*args, **kwargs):
        retry, max_retries = 0, 5
        while retry <= max_retries:
            try:
                return await method(*args, **kwargs)
            except (aiohttp.ClientError, TimeoutError) as error:
                retry += 1
                if retry == max_retries:
                    logging.error(
                        'Fail retry max_retries=%d error="%s"',
                        max_retries, error
                    )
                    raise

                base_delay, max_delay = 1, 60
                delay = min(base_delay * (2 ** (retry - 1)), max_delay)
                logger.warning(
                    'Retry retry=%d max_retries=%d delay=%.2f error="%s"',
                    retry, max_retries, delay, error
                )
                await asyncio.sleep(delay)

    return wrapper
