import stochastic


def test_integer():
    i = stochastic.integer(10, 20)
    assert 10 <= i <= 20


def test_character():
    c = stochastic.character("abc")
    assert c in "abc"


def test_string():
    s = stochastic.string("abc", 10)
    assert len(s) == 10
    for c in s:
        assert c in "abc"
