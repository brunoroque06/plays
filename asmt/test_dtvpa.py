from dateutil.relativedelta import relativedelta

from asmt import dtvpa


def test_data():
    dtvpa.validate()


def test_dtvpa():
    sub, comp, rep = dtvpa.process(
        relativedelta(years=12),
        {"co": 13, "fg": 4, "vse": 60, "vc": 12, "vsp": 29, "fc": 6},
    )

    assert sub.select("raw").to_series().eq([13, 4, 60, 12, 29, 6]).all()
    assert sub.select("%ile").to_series().eq(["25", "9", "9", "25", "9", "16"]).all()
    assert sub.select("standard").to_series().eq([8, 6, 6, 8, 6, 7]).all()

    assert comp.select("sum_standard").to_series().eq([41, 21, 20]).all()
    assert comp.select("index").to_series().eq([78, 81, 79]).all()
    assert comp.select("%ile").to_series().eq(["7", "10", "8"]).all()

    assert len(rep) > 0
