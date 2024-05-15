from dateutil.relativedelta import relativedelta

from reportus import dtvp


def test_data():
    dtvp.validate()


def test_dtvp():
    age = relativedelta(years=6, months=11)

    raw = {"eh": 108, "co": 11, "fg": 52, "vc": 10, "fc": 32}

    sub, comp, rep = dtvp.process(age, raw)

    assert sub["raw"].eq([108, 11, 52, 10, 32]).all()  # pyright: ignore
    assert (
        sub["age_eq"].eq(["4;3", "4;8", "10;5", "5;10", "6;3"]).all()
    )  # pyright: ignore
    assert sub["percentile"].eq(["1", "2", "75", "25", "50"]).all()  # pyright: ignore
    assert sub["scaled"].eq([3, 4, 12, 8, 10]).all()  # pyright: ignore
    assert (
        sub["descriptive"]
        .eq(["Very Poor", "Poor", "Average", "Average", "Average"])
        .all()
    )  # pyright: ignore

    assert comp["sum_scaled"].eq([7, 30, 37]).all()  # pyright: ignore
    assert comp["percentile"].eq(["<1", "50", "14"]).all()  # pyright: ignore
    assert (
        comp["descriptive"].eq(["Very Poor", "Average", "Below Average"]).all()
    )  # pyright: ignore
    assert comp["index"].eq([61, 100, 84]).all()  # pyright: ignore

    assert len(rep) > 0
