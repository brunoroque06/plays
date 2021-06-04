from genetic_algorithm import individual


def test_random_individual():
    ind = individual.random_individual()
    assert 10 <= num <= 20
