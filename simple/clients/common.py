
import re
import asyncio
import logging
import time
import random
import traceback
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


def error_trace(error):
    filename, trace = None, []
    for entry in traceback.extract_tb(error.__traceback__):
        match = re.search(r"clients/(e2b|gigachat|openrouter|yandexgpt)\.py", entry.filename)
        if match:
            filename = match.group(1)
            trace.append(entry.name)
    return "%s:%s" % (filename, "/".join(trace))


def retrying(method):
    @wraps(method)
    async def wrapper(*args, **kwargs):
        retry = 0
        while True:
            try:
                return await method(*args, **kwargs)
            except (aiohttp.ClientError, TimeoutError) as error:
                retry += 1
                base_delay, max_delay, jitter = 1, 120, random.random()
                delay = min(base_delay * (2 ** (retry - 1) + jitter), max_delay)
                logger.warning(
                    'retry=%d delay=%.1f trace="%s" error="%s"',
                    retry, delay,
                    error_trace(error),
                    str(error) or error.__class__.__name__
                )
                await asyncio.sleep(delay)

    return wrapper
