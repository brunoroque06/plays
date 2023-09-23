import itertools
from datetime import date

import polars as pl
import streamlit as st

from asmt import time


def get_scores() -> list[tuple[str, str]]:
    return [
        ("soc", "Social"),
        ("vis", "Vision"),
        ("hea", "Hearing"),
        ("tou", "Touch"),
        ("items", "Taste and Smell"),
        ("bod", "Body Awareness"),
        ("bal", "Balance and Motion"),
        ("pla", "Planning and Ideas"),
    ]


class Data:
    def __init__(self, data: pl.DataFrame):
        self.data = data

    def get_row(self, form: str, i: str, r: int):
        return self.data.filter(
            (pl.col("type") == form)
            & (pl.col("id") == i)
            & (pl.col("raw_min") <= r)
            & (pl.col("raw_max") >= r)
        )


@st.cache_data
def _load() -> Data:
    classroom = pl.read_csv("data/spm-classroom.csv")
    classroom = classroom.with_columns(pl.lit("classroom").alias("type"))

    home = pl.read_csv("data/spm-home.csv")
    home = home.with_columns(pl.lit("home").alias("type"))

    return Data(pl.concat([classroom, home]))


def validate():
    data = _load()
    types = ["classroom", "home"]
    ids = ["tot" if s[0] == "items" else s[0] for s in get_scores()]
    raws = range(0, 171)

    for t, i, r in itertools.product(types, ids, raws):
        row = data.get_row(t, i, r)
        assert row.is_empty() is False
        for c in ["percentile", "t"]:
            assert row.select(c).item() > 0


def _report(asmt: date, form: str, person: str, res: pl.DataFrame) -> str:
    asmt_fmt = time.format_date(asmt, False)
    header = [
        "Sensory Processing Measure (SPM): Classroom Form",
        f"Fragebogen zur sensorischen Verarbeitung ausgefüllt von Kinders {person} ({asmt_fmt})",
    ]
    if form == "home":
        header = [
            "Sensory Processing Measure (SPM): Home Form",
            f"Elternfragebogen zur sensorischen Verarbeitung ausgefüllt von {person} ({asmt_fmt})",
            "Die Fähigkeit, sensorische Reize zu verarbeiten, beeinflusst die motorischen und selbstregulativen Fähigkeiten eines Kindes sowie sein soziales Verhalten.",
        ]

    scores = [
        ("soc", "Social"),
        ("vis", "Vision"),
        ("hea", "Hearing"),
        ("tou", "Touch"),
        ("bod", "Body Awareness"),
        ("bal", "Balance and Motion"),
        ("pla", "Planning and Ideas"),
        ("tot", "Gesamttestwert"),
    ]

    return "\n".join(
        header
        + [
            f"{d}: PR {res.filter(pl.col('id') == i).select('percentile').item()} - \"{res.filter(pl.col('id') == i).select('interpretive').item()}\""
            for i, d in scores
        ]
    )


def process(
    asmt: date, form: str, person: str, raw: dict[str, int]
) -> tuple[pl.DataFrame, str]:
    data = _load()

    form = form.lower()

    raw["tot"] = sum(
        [raw["vis"], raw["hea"], raw["tou"], raw["items"], raw["bod"], raw["bal"]]
    )
    del raw["items"]

    def per(p: int) -> str:
        if p == 100:
            return ">99"
        return str(p)

    def inter(t: int) -> str:
        if t < 60:
            return "Typical"
        if t < 70:
            return "Some Problems"
        return "Definite Dysfunction"

    def form_row(i: str, r: int):
        row = data.get_row(form, i, r)
        return [
            i,
            r,
            row.select("t").item(),
            per(row.select("percentile").item()),
            inter(row.select("t").item()),
        ]

    res = pl.DataFrame(
        [form_row(i, r) for i, r in raw.items()],
        schema=["id", "raw", "t", "percentile", "interpretive"],
    )

    return res, _report(asmt, form, person, res)
