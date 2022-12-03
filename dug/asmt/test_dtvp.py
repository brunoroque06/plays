from dateutil.relativedelta import relativedelta

from asmt import dtvp


def test_dtvp():
    age = relativedelta(years=4, months=0)

    raw = {}
    for k in dtvp.get_tests():
        raw[k] = 0

    sub, comp = dtvp.process(age, raw)

    assert sub is not None
    assert comp is not None
