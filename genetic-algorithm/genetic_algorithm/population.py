import functools
import typing
from dataclasses import dataclass

from genetic_algorithm import genetics, individual


@dataclass(frozen=True)
class Stats:
    elitism: float
    mutation_rate: float
    max_generation: int
    target: genetics.Genes


@dataclass(frozen=True)
class Population:
    stats: Stats
    generation: int
    individuals: typing.List[individual.Individual]
    max_fitness: float


def create(
    elitism: float,
    mutation_rate: float,
    max_generation: int,
    size: int,
    target: genetics.Genes,
    random_string: typing.Callable[[], str],
) -> Population:
    stats = Stats(
        elitism=elitism,
        mutation_rate=mutation_rate,
        max_generation=max_generation,
        target=target,
    )
    genes = [genetics.random_genes(random_string) for _ in range(0, size)]
    inds = [
        individual.Individual(genes=g, fitness=genetics.calc_fitness(g, target))
        for g in genes
    ]
    fit = functools.reduce(
        lambda a, b: a if a > b else a,
        map(lambda i: i.fitness, inds),
    )
    return Population(stats=stats, generation=0, individuals=inds, max_fitness=fit)


def resolve() -> Population:
    return Population()
