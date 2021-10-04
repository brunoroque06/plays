# Inspired by https://python-dependency-injector.ets-labs.org/

from genetic_algorithm import stochastic


class Container:
    random_bool = stochastic.boolean
    random_int = stochastic.integer
