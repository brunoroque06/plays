import typing
from dataclasses import dataclass


@dataclass(frozen=True)
class Genes:
    value: str


def calc_fitness(target: Genes, genes: Genes) -> float:
    match = 0
    for idx in range(0, len(target.value)):
        if target.value[idx] == genes.value[idx]:
            match = match + 1
    return match / len(target.value)


def crossover(
    random_bool: typing.Callable[[], bool], genes: typing.Tuple[Genes, Genes]
) -> Genes:
    gen = ""
    for i in range(len(genes[0].value)):
        gen = gen + genes[0 if random_bool() else 1].value[i]

    return Genes(value=gen)


def random_genes(random_string: typing.Callable[[], str]) -> Genes:
    return Genes(value=random_string())
