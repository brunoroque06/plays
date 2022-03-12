from genetic_algorithm import population


def test_create_population():
    def random_str():
        return "a___"

    pop = population.create(
        target="algo",
        max_generation=10,
        random_str=random_str,
        elitism=0.25,
        mutation_rate=0.01,
        size=2,
    )

    assert pop.max_fitness == 0.25
