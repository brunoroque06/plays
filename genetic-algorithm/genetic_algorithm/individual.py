import typing
from dataclasses import dataclass

from genetic_algorithm import genetics


@dataclass(frozen=True)
class Individual:
    genes: genetics.Genes
    fitness: float


def mating_pool(fitnesses: typing.List[float]) -> typing.List[int]:
    pool = []
    fit_sum = sum(fitnesses)
    for idx, fit in enumerate(fitnesses, start=0):
        weight = int(fit / fit_sum * len(fitnesses) * 2)
        pool = pool + [idx] * weight
    return pool
