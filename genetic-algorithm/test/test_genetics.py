from genetic_algorithm import genetics


def test_calc_fitness():
    fit = genetics.calc_fitness(
        target=genetics.Genes(value="abcd"), genes=genetics.Genes(value="ab__")
    )
    assert fit == 0.5
