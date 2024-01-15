#!/usr/bin/env python3
"""task_wait_n module"""


from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of delays in ascending order"""
    delays: List[float] = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
