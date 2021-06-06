from genetic_algorithm import genetics, population


def test_create_population():
    target = "algo"

    def random_string():
        return "a___"

    target_genes = genetics.Genes(value=target)
    pop = population.create(
        target=target_genes,
        max_generation=10,
        random_string=random_string,
        elitism=0.25,
        mutation_rate=0.01,
        size=2,
    )

    assert pop.max_fitness == 0.25
