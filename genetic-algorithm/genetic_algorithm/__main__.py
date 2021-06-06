from genetic_algorithm import genetics, population, stochastic


def main():
    target = "To be or not to be, that is the question."
    random_string = stochastic.string(
        pool="abcdefghijklmnopqrstuvxz ,.T", length=len(target)
    )

    target_genes = genetics.Genes(value=target)
    pop = population.create(
        target=target_genes,
        max_generation=200,
        random_string=random_string,
        elitism=0.25,
        mutation_rate=0.01,
        size=100,
    )
    print(pop)
    return 0


main()
