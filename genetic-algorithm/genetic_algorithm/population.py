import typing
from dataclasses import dataclass

from genetic_algorithm import genetics, individual


@dataclass(frozen=True)
class Population:
    target: genetics.Genes
    individuals: typing.List[individual.Individual]
    elitism: float
    mutation_rate: float
    max_generations: int

def initialize(target: genetics.Genes, size: int, elitism: ):