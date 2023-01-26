import datetime

import pytest

from asmt import spm


@pytest.mark.parametrize(
    "form,raw,ts",
    [
        (
            "Classroom",
            {
                "soc": 27,
                "vis": 4,
                "hea": 15,
                "tou": 12,
                "items": 4,
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
                "items": 8,
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
def test_spm(form, raw, ts):
    today = datetime.date.today()

    res, rep = spm.process(today, form, raw)

    for k, v in ts.items():
        assert res.loc[k].t == v

    assert len(rep) > 0
