from genetic_algorithm import individual


def test_mating_pool():
    pool = individual.mating_pool(fitnesses=[0.25, 0.5, 0.25, 0.75])
    assert pool == [0, 1, 1, 2, 3, 3, 3]
