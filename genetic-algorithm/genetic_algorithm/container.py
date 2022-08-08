# Inspired by https://python-dependency-injector.ets-labs.org/

from genetic_algorithm import stochastic


class Container:
    rnd_bool = stochastic.boolean
    rnd_int = stochastic.integer
