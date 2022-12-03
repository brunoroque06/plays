from dateutil.relativedelta import relativedelta

from asmt import time


def test_delta_idx():
    assert time.delta_idx(relativedelta(years=4, months=2)) == 4.02
    assert time.delta_idx(relativedelta(years=4, months=10)) == 4.10
    assert time.delta_idx(relativedelta(years=4, months=12)) == 5.0
    assert time.delta_idx(relativedelta(years=4, months=11), inc=True) == 5.0
    assert time.delta_idx(relativedelta(years=4, months=13)) == 5.01
