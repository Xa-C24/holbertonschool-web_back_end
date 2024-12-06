#!/usr/bin/env python3
"""Execute task_wait_random n times and return sorted list of delays."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times with max_delay and returns
    the list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Liste de tâches
    delays = []

    for task in asyncio.as_completed(tasks):  # Gérer les tâches au fur et à mesure
        delay = await task
        delays.append(delay)

    return sorted(delays)  # Retourne les délais triés
