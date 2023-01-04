import typing

from genetic import rand


def calc_fitness(target: str, genes: str) -> float:
    match = 0
    for tar, gen in zip(target, genes):
        if tar == gen:
            match += 1
    return match / len(target)


def crossover(
    parents: typing.Tuple[str, str], rnd_bool: typing.Callable[[], bool] = rand.boolean
) -> str:
    genes = [p_x if rnd_bool() else p_y for p_x, p_y in zip(parents[0], parents[1])]
    return "".join(genes)


def mutate(
    rnd_char: typing.Callable[[], str],
    mutation_rate: float,
    genes: str,
    rnd_int: typing.Callable[[int, int], int] = rand.integer,
):
    def does_mutate() -> bool:
        integer = rnd_int(0, 100) / 100
        return integer < mutation_rate

    new_genes = [rnd_char() if does_mutate() else g for g in genes]

    return "".join(new_genes)
