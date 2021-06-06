import typing
from dataclasses import dataclass


@dataclass(frozen=True)
class Genes:
    value: str


def random_genes(random_string: typing.Callable[[], str]) -> Genes:
    return Genes(value=random_string())


def calc_fitness(target: Genes, genes: Genes) -> float:
    match = 0
    for idx in range(0, len(target.value)):
        if target.value[idx] == genes.value[idx]:
            match = match + 1
    return match / len(target.value)
