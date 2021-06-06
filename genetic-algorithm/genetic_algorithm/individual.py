import heapq
import typing
from dataclasses import dataclass

from genetic_algorithm import genetics


@dataclass(frozen=True)
class Individual:
    genes: genetics.Genes
    fitness: float


def top_individuals(fitnesses: typing.List[float]) -> typing.Tuple[int, int]:
    ids = heapq.nlargest(2, range(len(fitnesses)), key=fitnesses.__getitem__)
    return ids[0], ids[1]


def mating_pool(fitnesses: typing.List[float]) -> typing.List[int]:
    pool: typing.List[int] = []
    fit_sum = sum(fitnesses)
    for idx, fit in enumerate(fitnesses, start=0):
        weight = int(fit / fit_sum * len(fitnesses) * 2)
        pool = pool + [idx] * weight
    return pool
