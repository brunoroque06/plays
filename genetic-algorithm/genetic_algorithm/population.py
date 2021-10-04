import functools
import typing
from dataclasses import dataclass

from genetic_algorithm import container, genetics, individual


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
    random_str: typing.Callable[[], str],
    size: int,
    max_generation: int,
    elitism: float,
    mutation_rate: float,
    target: genetics.Genes,
) -> Population:
    stats = Stats(
        elitism=elitism,
        mutation_rate=mutation_rate,
        max_generation=max_generation,
        target=target,
    )
    genes = [genetics.random_genes(random_str) for _ in range(0, size)]
    inds = [
        individual.Individual(genes=g, fitness=genetics.calc_fitness(g, target))
        for g in genes
    ]
    return Population(
        stats=stats, generation=0, individuals=inds, max_fitness=max_fitness(inds)
    )


def find_parents(
    individuals: typing.List[individual.Individual],
    pool: typing.List[int],
    random_int: typing.Callable[[int, int], int] = container.Container.random_int,
) -> typing.Tuple[genetics.Genes, genetics.Genes]:
    par_x = pool[random_int(0, len(pool) - 1)]
    par_y = pool[random_int(0, len(pool) - 1)]
    return individuals[par_x].genes, individuals[par_y].genes


def next_generation(
    random_char: typing.Callable[[], str],
    stats: Stats,
    individuals: typing.List[individual.Individual],
) -> typing.List[individual.Individual]:

    fits = list(map(lambda i: i.fitness, individuals))
    pool = individual.mating_pool(fitnesses=fits)
    best, second = individual.top_individuals(fitnesses=fits)
    num_elites = round(len(individuals) * stats.elitism)

    inds: typing.List[individual.Individual] = []

    for i in range(len(individuals)):
        parents = (
            (individuals[best].genes, individuals[second].genes)
            if i < num_elites
            else find_parents(individuals=individuals, pool=pool)
        )
        child = genetics.crossover(genes=parents)
        mutated_child = genetics.mutate(
            random_char=random_char,
            mutation_rate=stats.mutation_rate,
            genes=child,
        )
        inds.append(
            individual.Individual(
                genes=mutated_child,
                fitness=genetics.calc_fitness(target=stats.target, genes=mutated_child),
            )
        )

    return inds


def print_statistics(population: Population):
    fitnesses = [ind.fitness for ind in population.individuals]
    best = max(fitnesses)
    best_genes = [i for i in population.individuals if i.fitness == best]
    print(
        f"{population.generation}".zfill(3),
        f"{population.max_fitness:.2f}",
        best_genes[0].genes.value,
    )


# Recursion would be nice
# But without tail recursion it might be extremely inefficient memory/stack wise
def resolve(
    random_char: typing.Callable[[], str],
    population: Population,
) -> Population:
    while (
        population.max_fitness != 1
        and population.generation != population.stats.max_generation
    ):
        inds = next_generation(
            random_char=random_char,
            stats=population.stats,
            individuals=population.individuals,
        )
        population.individuals = inds
        population.max_fitness = max_fitness(inds)
        population.generation = population.generation + 1
        if population.generation % 10 == 0:
            print_statistics(population)

    print_statistics(population)
    return population
