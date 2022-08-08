from genetic_algorithm import individual
from genetic_algorithm import population


def test_create_population():
    def random_str():
        return "a___"

    pop = population.create(
        target="algo",
        max_gen=10,
        rnd_str=random_str,
        elitism=0.25,
        mutation_rate=0.01,
        size=2,
    )

    assert pop.gen == 0
    assert pop.max_fitness == 0.25
    assert len(pop.inds) == 2


def test_find_parents():
    par = 0

    def random_int(_, __):
        nonlocal par
        par += 1
        return 0 if par < 2 else 1

    par_x, par_y = population.find_parents(
        inds=[
            individual.Individual(fitness=0, genes="a"),
            individual.Individual(fitness=1, genes="b"),
        ],
        pool=[0, 1, 2, 3],
        rnd_int=random_int,
    )

    assert par_x == "a"
    assert par_y == "b"
