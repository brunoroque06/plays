import typing
from dataclasses import dataclass


@dataclass(frozen=True)
class Genes:
    value: str


def random_genes(random_string: typing.Callable[[], str]) -> Genes:
    return Genes(value=random_string())

def calc_fitness(target: Genes, genes: Genes) -> float:
