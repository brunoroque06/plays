from genetic_algorithm import population, stochastic


def main():
    target = "To be or not to be, that is the question."
    pool = "abcdefghijklmnopqrstuvxz ,.T"

    random_str = stochastic.string(pool=pool, length=len(target))

    pop = population.create(
        random_str=random_str,
        size=200,
        max_generation=200,
        elitism=0.20,
        mutation_rate=0.01,
        target=target,
    )

    random_char = stochastic.string(pool=pool, length=1)

    pop = population.resolve(
        random_char=random_char,
        population=pop,
    )

    return pop


main()
