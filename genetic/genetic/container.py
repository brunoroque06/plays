# Inspired by https://python-dependency-injector.ets-labs.org/
from genetic import rand


class Container:
    rand_bool = rand.boolean
    rand_int = rand.integer
