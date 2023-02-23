from genetic import population, rand


def main():
    target = "To be or not to be, that is the question."
    pool = "abcdefghijklmnopqrstuvxz ,.T"

    rand_str = rand.string(pool=pool, length=len(target))

    pop = population.create(
        rand_str=rand_str,
        size=200,
        max_gen=200,
        elitism=0.20,
        mutation_rate=0.01,
        target=target,
    )

    rand_char = rand.string(pool=pool, length=1)

    pop = population.resolve(
        rand_char=rand_char,
        pop=pop,
    )

    population.print_stats(pop)

    return pop


if __name__ == "__main__":
    main()
