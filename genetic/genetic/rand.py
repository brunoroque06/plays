import functools
import random
from typing import Callable


def boolean() -> bool:
    return bool(random.getrandbits(1))


def integer(mini: int, maxi: int) -> int:
    return mini + round(random.random() * (maxi - mini))


def character(pool: str) -> str:
    return pool[integer(0, len(pool) - 1)]


def string(pool: str, length: int) -> Callable[[], str]:
    def gen():
        chars = [character(pool) for _ in range(length)]
        return functools.reduce(lambda a, b: a + b, chars)

    return gen
