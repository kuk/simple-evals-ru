
import asyncio
import logging
import time
import random
from functools import wraps
from collections import deque

import aiohttp


logger = logging.getLogger("simple")


class RateLimiter:
    def __init__(self, max_requests=1, time_window=1):
        self.max_requests = max_requests
        self.time_window = time_window
        self.request_times = deque()

    async def wait(self):
        self.request_times.append(time.monotonic())

        while len(self.request_times) >= self.max_requests:
            oldest_time = self.request_times[0]
            time_delta = time.monotonic() - oldest_time

            if time_delta >= self.time_window:
                self.request_times.popleft()
            else:
                await asyncio.sleep(self.time_window - time_delta)


def retrying(method):
    @wraps(method)
    async def wrapper(*args, **kwargs):
        retry, max_retries = 0, 10
        while retry <= max_retries:
            try:
                return await method(*args, **kwargs)
            except (aiohttp.ClientError, TimeoutError) as error:
                retry += 1
                if retry == max_retries:
                    logging.error(
                        'Fail retry max_retries=%d cls=%s msg="%s"',
                        max_retries, error.__class__.__name__, str(error)
                    )
                    raise

                base_delay, max_delay, jitter = 1, 100, random.random()
                delay = min(base_delay * (2 ** (retry - 1) + jitter), max_delay)
                logger.warning(
                    'Retry retry=%d max_retries=%d delay=%.1f cls=%s msg="%s"',
                    retry, max_retries, delay, error.__class__.__name__, str(error)
                )
                await asyncio.sleep(delay)

    return wrapper
