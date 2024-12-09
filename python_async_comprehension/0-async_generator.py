#!/usr/bin/env python3
"""Creates a generator"""

import asyncio
import random


async def async_generator():
    """
      Coroutine that generates 10 random floating-point numbers asynchronously.

      At each iteration:
      - Waits asynchronously for 1 second.
      - Yields a random floating-point number between 0 and 10.

      Returns:
          An asynchronous generator yielding 10 random numbers (float).
      """
    for _ in range(10):  # Boucle 10fois
      await asyncio.sleep(1)  # Attend 1seconde
      yield random.uniform(0, 10)  # Génére un nombre aléatoire
