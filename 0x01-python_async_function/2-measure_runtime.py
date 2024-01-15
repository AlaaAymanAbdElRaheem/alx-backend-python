#!/usr/bin/env python3
""" a measure_time function with integers n and max_delay
as arguments that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n"""


wait_n = __import__('1-concurrent_coroutines').wait_n


import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """returns total_time / n"""
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time / n
