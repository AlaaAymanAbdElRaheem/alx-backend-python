#!/usr/bin/env python3
"""defines a type-annotated function"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, v * v)
