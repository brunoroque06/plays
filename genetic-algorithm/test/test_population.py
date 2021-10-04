from genetic_algorithm import genetics, population


def test_create_population():
    target = "algo"

    def random_str():
        return "a___"

    target_genes = genetics.Genes(value=target)
    pop = population.create(
        target=target_genes,
        max_generation=10,
        random_str=random_str,
        elitism=0.25,
        mutation_rate=0.01,
        size=2,
    )

    assert pop.max_fitness == 0.25
