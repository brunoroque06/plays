from collections.abc import Callable

from genetic import rand


def calc_fitness(target: str, genes: str) -> float:
    match = 0
    for tar, gen in zip(target, genes, strict=True):
        if tar == gen:
            match += 1
    return match / len(target)


def crossover(
    parents: tuple[str, str], rand_bool: Callable[[], bool] = rand.boolean
) -> str:
    genes = [
        p_x if rand_bool() else p_y
        for p_x, p_y in zip(parents[0], parents[1], strict=True)
    ]
    return "".join(genes)


def mutate(
    rand_char: Callable[[], str],
    mutation_rate: float,
    genes: str,
    rand_int: Callable[[int, int], int] = rand.integer,
):
    def does_mutate() -> bool:
        integer = rand_int(0, 100) / 100
        return integer < mutation_rate

    new_genes = [rand_char() if does_mutate() else g for g in genes]

    return "".join(new_genes)
