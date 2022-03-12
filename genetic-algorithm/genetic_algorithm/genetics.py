import typing

from genetic_algorithm import container


def calc_fitness(target: str, genes: str) -> float:
    match = 0
    for tar, gen in zip(target, genes):
        if tar == gen:
            match += 1
    return match / len(target)


def crossover(
    parents: typing.Tuple[str, str],
    random_bool: typing.Callable[[], bool] = container.Container.random_bool,
) -> str:
    genes = [p_x if random_bool() else p_y for p_x, p_y in zip(parents[0], parents[1])]
    return "".join(genes)


def mutate(
    random_char: typing.Callable[[], str],
    mutation_rate: float,
    genes: str,
    random_int: typing.Callable[[int, int], int] = container.Container.random_int,
):
    def does_mutate() -> bool:
        integer = random_int(0, 100) / 100
        return integer < mutation_rate

    new_genes = [random_char() if does_mutate() else g for g in genes]
    return "".join(new_genes)
