from genetic_algorithm import genetics


def test_calc_fitness():
    fit = genetics.calc_fitness(
        target=genetics.Genes(value="abcd"), genes=genetics.Genes(value="ab__")
    )
    assert fit == 0.5


def test_crossover():
    time = 0

    def random_bool():
        nonlocal time
        time += 1
        if time < 3:
            return False
        return True

    genes = genetics.crossover(
        random_bool=random_bool,
        genes=(genetics.Genes(value="abc"), genetics.Genes(value="def")),
    )
    assert genes.value == "dec"


def test_mutate():
    time = 0

    def random_int(_: int, __: int):
        nonlocal time
        time += 1
        if time < 4:
            return 100
        return 0

    def char():
        return "_"

    genes = genetics.mutate(
        random_int=random_int,
        random_char=char,
        mutation_rate=0.10,
        genes=genetics.Genes(value="abcde"),
    )
    assert genes.value == "abc__"
