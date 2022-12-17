from dateutil.relativedelta import relativedelta

from asmt import dtvpa


def test_dtvpa():
    sub, comp = dtvpa.process(
        relativedelta(years=12),
        {"co": 13, "fg": 4, "vse": 60, "vc": 12, "vsp": 29, "fc": 6},
    )

    assert (sub["raw"] == [13, 4, 60, 12, 29, 6]).all()
    assert (sub["%ile"] == [25, 9, 9, 25, 9, 16]).all()
    assert (sub["standard"] == [8, 6, 6, 8, 6, 7]).all()

    # pylint: disable=unsubscriptable-object
    assert (comp["sum_standard"] == [41, 21, 20]).all()
    assert (comp["index"] == [78, 81, 79]).all()
    assert (comp["%ile"] == [7, 10, 8]).all()
