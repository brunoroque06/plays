from datetime import date

from dateutil.relativedelta import relativedelta

from asmt import dtvp


def test_dtvp():
    age = relativedelta(years=6, months=11)

    raw = {"eh": 108, "co": 11, "fg": 52, "vc": 10, "fc": 32}

    sub, comp, rep = dtvp.process(age, raw)

    assert (sub["raw"] == [108, 11, 52, 10, 32]).all()
    assert (sub["age_eq"] == ["4;3", "4;8", "10;5", "5;10", "6;3"]).all()
    assert (sub["percentile"] == [1, 2, 75, 25, 50]).all()
    assert (sub["scaled"] == [3, 4, 12, 8, 10]).all()
    assert (
        sub["descriptive"] == ["Very Poor", "Poor", "Average", "Average", "Average"]
    ).all()

    # pylint: disable=unsubscriptable-object
    assert (comp["sum_scaled"] == [7, 30, 37]).all()
    assert (comp["percentile"] == [0, 50, 14]).all()
    assert (comp["descriptive"] == ["Very Poor", "Average", "Below Average"]).all()
    assert (comp["index"] == [61, 100, 84]).all()

    assert len(rep(date.today())) > 0
