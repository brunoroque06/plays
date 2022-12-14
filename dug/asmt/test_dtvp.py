from dateutil.relativedelta import relativedelta

from asmt import dtvp


def test_dtvp():
    age = relativedelta(years=6, months=11)

    raw = {"eh": 108, "co": 11, "fg": 52, "vc": 10, "fc": 32}

    sub, comp = dtvp.process(age, raw)

    assert (sub["age_eq"] == ["4;3", "4;8", "10;5", "5;10", "6;3"]).all()
    assert (sub["scaled"] == [3, 4, 12, 8, 10]).all()
    assert (
        comp["index"] == [61, 100, 84]  # pylint: disable=unsubscriptable-object
    ).all()
