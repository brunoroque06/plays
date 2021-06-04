from dataclasses import dataclass

from genetic_algorithm import genetics


@dataclass(frozen=True)
class Individual:
    genes: genetics.Genes
