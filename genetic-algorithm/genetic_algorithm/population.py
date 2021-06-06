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


@dataclass
class Population:
    stats: Stats
    generation: int
    individuals: typing.List[individual.Individual]
    max_fitness: float


def max_fitness(individuals: typing.List[individual.Individual]) -> float:
    return functools.reduce(
        lambda a, b: a if a > b else a,
        map(lambda i: i.fitness, individuals),
    )


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
    return Population(
        stats=stats, generation=0, individuals=inds, max_fitness=max_fitness(inds)
    )


def next_generation(
    random_bool: typing.Callable[[], bool],
    stats: Stats,
    individuals: typing.List[individual.Individual],
) -> typing.List[individual.Individual]:

    fits = list(map(lambda i: i.fitness, individuals))
    pool = individual.mating_pool(fitnesses=fits)
    best, second = individual.top_individuals(fitnesses=fits)
    num_elites = round(len(individuals) * stats.elitism)

    inds: typing.List[individual.Individual] = []

    for i in range(len(individuals)):
        if i < num_elites:
            child = genetics.crossover(
                random_bool=random_bool,
                genes=(individuals[best].genes, individuals[second].genes),
            )

    return inds


# Recursion would be nice
# But without tail recursion it might be extremely inefficient memory/stack wise
def resolve(
    random_bool: typing.Callable[[], bool], population: Population
) -> Population:
    while (
        population.max_fitness != 1
        and population.generation != population.stats.max_generation
    ):
        inds = next_generation(
            random_bool=random_bool,
            stats=population.stats,
            individuals=population.individuals,
        )
        population.individuals = inds
        population.max_fitness = max_fitness(inds)
        population.generation = population.generation + 1

    return population
