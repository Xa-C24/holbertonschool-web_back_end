#!/usr/bin/env python3
"""Measure the runtime of wait_n"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns the average runtime per coroutine.
    """
    start_time = time.time()  # Enregistre le temps de début
    asyncio.run(wait_n(n, max_delay))  # Exécute la coroutine wait_n
    end_time = time.time()  # Enregistre le temps de fin

    total_time = end_time - start_time  # Calcule le temps total
    return total_time / n  # Retourne le temps moyen par tâche
