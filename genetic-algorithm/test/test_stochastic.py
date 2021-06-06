from genetic_algorithm import stochastic


def test_boolean():
    boolean = stochastic.boolean()
    assert boolean or boolean is False


def test_integer():
    num = stochastic.integer(10, 20)
    assert 10 <= num <= 20


def test_character():
    char = stochastic.character("abc")
    assert char in "abc"


def test_string():
    string = stochastic.string("abc", 10)()
    assert len(string) == 10
    for char in string:
        assert char in "abc"
