import heapq
import typing
from dataclasses import dataclass


@dataclass(frozen=True)
class Individual:
    genes: str
    fitness: float


def top_individuals(fits: typing.List[float]) -> typing.Tuple[int, int]:
    ids = heapq.nlargest(2, range(len(fits)), key=fits.__getitem__)
    return ids[0], ids[1]


def mating_pool(fits: typing.List[float]) -> typing.List[int]:
    pool: typing.List[int] = []
    fit_sum = sum(fits)

    for idx, fit in enumerate(fits, start=0):
        weight = int(fit / fit_sum * len(fits) * 2)
        pool = pool + [idx] * weight

    return pool
