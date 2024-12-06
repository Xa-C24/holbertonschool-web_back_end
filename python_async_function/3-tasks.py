#!/usr/bin/env python3
"""Return an asyncio.Task from wait_random"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task
    that executes wait_random with the given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
