from genetic_algorithm import genetics, population, stochastic


def main():
    target = "To be or not to be, that is the question."
    pool = "abcdefghijklmnopqrstuvxz ,.T"

    random_string = stochastic.string(pool=pool, length=len(target))

    target_genes = genetics.Genes(value=target)

    pop = population.create(
        target=target_genes,
        max_generation=200,
        random_string=random_string,
        elitism=0.25,
        mutation_rate=0.01,
        size=300,
    )

    random_char = stochastic.string(pool=pool, length=1)

    # Property drilling is quite bad here; dependency injection would help
    pop = population.resolve(
        random_bool=stochastic.boolean,
        random_integer=stochastic.integer,
        random_char=random_char,
        population=pop,
    )

    return pop


main()
