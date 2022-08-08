from genetic_algorithm import individual


def test_top_individuals():
    best, snd = individual.top_individuals(fits=[0.5, 0.99, 0.25, 0.75])
    assert best == 1
    assert snd == 3


def test_mating_pool():
    pool = individual.mating_pool(fits=[0.25, 0.5, 0.25, 0.75])
    assert pool == [0, 1, 1, 2, 3, 3, 3]
