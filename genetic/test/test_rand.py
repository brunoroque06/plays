from genetic import rand


def test_boolean():
    boolean = rand.boolean()
    assert boolean or boolean is False


def test_integer():
    num = rand.integer(10, 20)
    assert 10 <= num <= 20


def test_character():
    char = rand.character("abc")
    assert char in "abc"


def test_string():
    string = rand.string("abc", 10)()
    assert len(string) == 10
    for char in string:
        assert char in "abc"
