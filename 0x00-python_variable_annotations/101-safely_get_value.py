#!/usr/bin/env python3
"""defines a type-annotated function"""


from typing import Any, Mapping, Union, TypeVar, Optional


T = TypeVar('T')
default_t = Optional[T]


def safely_get_value(dct: Mapping,
                     key: Any, default: default_t = None) -> Union[Any, T]:
    """returns the value safely"""
    if key in dct:
        return dct[key]
    else:
        return default
