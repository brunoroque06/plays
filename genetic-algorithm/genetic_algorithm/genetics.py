import typing
from dataclasses import dataclass

from genetic_algorithm import container


@dataclass(frozen=True)
class Genes:
    value: str


def calc_fitness(target: Genes, genes: Genes) -> float:
    match = 0
    for i, _ in enumerate(target.value):
        if target.value[i] == genes.value[i]:
            match = match + 1
    return match / len(target.value)


def crossover(
    genes: typing.Tuple[Genes, Genes],
    random_bool: typing.Callable[[], bool] = container.Container.random_bool,
) -> Genes:
    gen = ""
    for i, _ in enumerate(genes[0].value):
        gen = gen + genes[0 if random_bool() else 1].value[i]

    return Genes(value=gen)


def random_genes(random_str: typing.Callable[[], str]) -> Genes:
    return Genes(value=random_str())


def mutate(
    random_char: typing.Callable[[], str],
    mutation_rate: float,
    genes: Genes,
    random_int: typing.Callable[[int, int], int] = container.Container.random_int,
):
    value = genes.value

    def does_mutate() -> bool:
        integer = random_int(0, 100) / 100
        return integer < mutation_rate

    for i, _ in enumerate(value):
        if does_mutate():
            lis = list(value)
            lis[i] = random_char()
            value = "".join(lis)

    return Genes(value=value)
