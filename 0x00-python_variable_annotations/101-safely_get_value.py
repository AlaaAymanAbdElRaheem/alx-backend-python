#!/usr/bin/env python3
"""defines a type-annotated function"""


from typing import Any, Mapping, Union, TypeVar


def safely_get_value(dct: Mapping,
                     key: Any, default: TypeVar = None) -> Union[Any, None]:
    """returns the value safely"""
    if key in dct:
        return dct[key]
    else:
        return default
