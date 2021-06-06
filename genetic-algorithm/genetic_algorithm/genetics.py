import typing
from dataclasses import dataclass


@dataclass(frozen=True)
class Genes:
    value: str


def calc_fitness(target: Genes, genes: Genes) -> float:
    match = 0
    for idx in range(len(target.value)):
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


def mutate(
    random_integer: typing.Callable[[int, int], int],
    random_char: typing.Callable[[], str],
    mutation_rate: float,
    genes: Genes,
):
    value = genes.value

    def does_mutate() -> bool:
        integer = random_integer(0, 100) / 100
        return integer < mutation_rate

    for i, _ in enumerate(value):
        if does_mutate():
            lis = list(value)
            lis[i] = random_char()
            value = "".join(lis)

    return Genes(value=value)
