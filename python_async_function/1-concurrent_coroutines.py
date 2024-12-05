#!/usr/bin/env python3
"""previous python file that you’ve written and write an async routine called wait_n"""

import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawns wait_random n times with a specified max_delay
    and returns the list of delays in ascending order.
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return sorted(delays)
