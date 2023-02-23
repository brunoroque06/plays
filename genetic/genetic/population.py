import functools
from dataclasses import dataclass
from typing import Callable

from genetic import genetics, individual, rand


@dataclass(frozen=True)
class Stats:
    elitism: float
    mutation_rate: float
    max_gen: int
    target: str


@dataclass
class Population:
    stats: Stats
    gen: int
    inds: list[individual.Individual]
    max_fitness: float


def max_fitness(inds: list[individual.Individual]) -> float:
    return functools.reduce(
        lambda a, b: a if a > b else a,
        map(lambda i: i.fitness, inds),
    )


def create(
    rand_str: Callable[[], str],
    size: int,
    max_gen: int,
    elitism: float,
    mutation_rate: float,
    target: str,
) -> Population:
    stats = Stats(
        elitism=elitism,
        mutation_rate=mutation_rate,
        max_gen=max_gen,
        target=target,
    )
    genes = [rand_str() for _ in range(0, size)]
    inds = [
        individual.Individual(genes=g, fitness=genetics.calc_fitness(g, target))
        for g in genes
    ]
    return Population(stats=stats, gen=0, inds=inds, max_fitness=max_fitness(inds))


def find_parents(
    inds: list[individual.Individual],
    pool: list[int],
    rand_int: Callable[[int, int], int] = rand.integer,
) -> tuple[str, str]:
    par_x = pool[rand_int(0, len(pool) - 1)]
    par_y = pool[rand_int(0, len(pool) - 1)]
    return inds[par_x].genes, inds[par_y].genes


def next_generation(
    rand_char: Callable[[], str],
    stats: Stats,
    inds: list[individual.Individual],
) -> list[individual.Individual]:
    fits = list(map(lambda ind: ind.fitness, inds))
    pool = individual.mating_pool(fits=fits)
    best, snd = individual.top_individuals(fits=fits)
    num_elites = round(len(inds) * stats.elitism)

    def new_ind(i: int) -> individual.Individual:
        parents = (
            (inds[best].genes, inds[snd].genes)
            if i < num_elites
            else find_parents(inds=inds, pool=pool)
        )
        child = genetics.crossover(parents=parents)
        mutated_child = genetics.mutate(
            rand_char=rand_char,
            mutation_rate=stats.mutation_rate,
            genes=child,
        )
        return individual.Individual(
            genes=mutated_child,
            fitness=genetics.calc_fitness(target=stats.target, genes=mutated_child),
        )

    next_inds = [new_ind(i) for i, _ in enumerate(inds)]

    return next_inds


def print_stats(pop: Population):
    fits = [ind.fitness for ind in pop.inds]
    best = max(fits)
    best_genes = [i for i in pop.inds if i.fitness == best]
    print(
        f"{pop.gen}".zfill(3),
        f"{pop.max_fitness:.2f}",
        best_genes[0].genes,
    )


def resolve(
    rand_char: Callable[[], str],
    pop: Population,
) -> Population:
    inds = next_generation(
        rand_char=rand_char,
        stats=pop.stats,
        inds=pop.inds,
    )
    pop.inds = inds
    pop.max_fitness = max_fitness(inds)
    pop.gen = pop.gen + 1

    if pop.gen % 10 == 0:
        print_stats(pop)

    if pop.max_fitness != 1 and pop.gen != pop.stats.max_gen:
        pop = resolve(rand_char, pop)

    return pop
