#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer argument"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds (inclusive)
    and returns this delay.
    """
    delay = random.uniform(0, max_delay)  # Génère un délai aléatoire
    await asyncio.sleep(delay)  # Attend pendant ce délai
    return delay                # Retourne le délai
