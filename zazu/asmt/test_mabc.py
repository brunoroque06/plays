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

    corr = [
        ["hg11", 11, 0],
        ["hg12", 1, 2],
        ["hg1", 6, None],
        ["hg2", 14, 0],
        ["hg3", 11, 0],
        ["hg", 31, None],
        ["hgs", 11, 0],
        ["hgp", 63, 0],
        ["bf1", 5, 2],
        ["bf2", 1, 2],
        ["bf", 6, None],
        ["bfs", 1, 2],
        ["bfp", 0.1, 2],
    ]
