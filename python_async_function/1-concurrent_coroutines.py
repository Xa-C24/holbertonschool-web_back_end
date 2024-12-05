#!/usr/bin/env python3
"""Async routine called wait_n"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with a specified max_delay
    and returns the list of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    # Insère chaque délai dans une liste triée au fur et à mesure
    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insère le délai dans la liste triée
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)

    return delays
