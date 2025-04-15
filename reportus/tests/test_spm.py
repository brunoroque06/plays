import datetime

import polars as pl
import pytest

from reportus import spm


def test_data():
    spm.validate()


@pytest.mark.parametrize(
    ("form", "raw", "ts"),
    [
        (
            "Classroom",
            {
                "soc": 27,
                "vis": 4,
                "hea": 15,
                "tou": 12,
                "t&s": 4,
                "bod": 10,
                "bal": 24,
                "pla": 28,
            },
            {
                "soc": 64,
                "vis": 40,
                "hea": 69,
                "tou": 63,
                "bod": 57,
                "bal": 72,
                "pla": 70,
                "tot": 63,
            },
        ),
        (
            "Home",
            {
                "soc": 26,
                "vis": 14,
                "hea": 11,
                "tou": 18,
                "t&s": 8,
                "bod": 22,
                "bal": 18,
                "pla": 26,
            },
            {
                "soc": 66,
                "vis": 57,
                "hea": 59,
                "tou": 63,
                "bod": 67,
                "bal": 63,
                "pla": 72,
                "tot": 63,
            },
        ),
    ],
)
def test_spm(form: str, raw: dict[str, int], ts: dict[str, int]):
    today = datetime.date.today()

    res, rep = spm.process(today, form, "t", raw)

    for i, t in ts.items():
        assert res.filter(pl.col("id") == i).select("t").item() == t

    assert len(rep) > 0
