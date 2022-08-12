from datetime import date

from asmt import mabc


def test_boolean():
    perf = {
        "hg11": 17,
        "hg12": 29,
        "hg2": 32,
        "hg3": 0,
        "bf1": 4,
        "bf2": 0,
        "bl11": 9,
        "bl12": 7,
        "bl2": 20,
        "bl3": 1,
    }

    res = mabc.process(date(2016, 1, 2), date(2022, 1, 1), perf)

    assert res is not None
