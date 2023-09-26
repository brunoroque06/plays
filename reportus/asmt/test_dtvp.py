from dateutil.relativedelta import relativedelta

from asmt import dtvp


def test_data():
    dtvp.validate()


def test_dtvp():
    age = relativedelta(years=6, months=11)

    raw = {"eh": 108, "co": 11, "fg": 52, "vc": 10, "fc": 32}

    sub, comp, rep = dtvp.process(age, raw)

    assert sub.select("raw").to_series().eq([108, 11, 52, 10, 32]).all()
    assert (
        sub.select("age_eq").to_series().eq(["4;3", "4;8", "10;5", "5;10", "6;3"]).all()
    )
    assert sub.select("percentile").to_series().eq(["1", "2", "75", "25", "50"]).all()
    assert sub.select("scaled").to_series().eq([3, 4, 12, 8, 10]).all()
    assert (
        sub.select("descriptive")
        .to_series()
        .eq(["Very Poor", "Poor", "Average", "Average", "Average"])
        .all()
    )

    assert comp.select("sum_scaled").to_series().eq([7, 30, 37]).all()
    assert comp.select("percentile").to_series().eq(["<1", "50", "14"]).all()
    assert (
        comp.select("descriptive")
        .to_series()
        .eq(["Very Poor", "Average", "Below Average"])
        .all()
    )
    assert comp.select("index").to_series().eq([61, 100, 84]).all()

    assert len(rep) > 0
