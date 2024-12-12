#!/usr/bin/env python3
""" module for runtime of executing async_comprehension four times in parallel """

import asyncio  # Gérer les coroutines.
import time     # Mesurer le temps d'exécution.
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
  """
    Measures the total runtime of executing async_comprehension
    four times in parallel.
    
    Returns:
        float: Total runtime in seconds.
    """

  start = time.perf_counter()  # Start the timer
  await asyncio.gather(
      async_comprehension(),
      async_comprehension(),
      async_comprehension(),
      async_comprehension()
  )
  end = time.perf_counter()  # End the timer
  return end - start  # Calculate and start
