#!/usr/bin/env python3
"""defines a type-annotated function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """Multiplies a float by multiplier"""
        return n * multiplier
    return multiply
