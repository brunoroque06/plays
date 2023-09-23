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


@st.cache_data
def load() -> pl.DataFrame:
    clroom = pl.read_csv("data/spm-classroom.csv")
    clroom = clroom.with_columns(pl.lit("classroom").alias("type"))

    home = pl.read_csv("data/spm-home.csv")
    home = home.with_columns(pl.lit("home").alias("type"))

    return pl.concat([clroom, home])


def get_row(data: pl.DataFrame, form: str, k: str, v: int):
    return data.filter(
        (pl.col("type") == form)
        & (pl.col("id") == k)
        & (pl.col("raw_min") <= v)
        & (pl.col("raw_max") >= v)
    )


def validate():
    data = load()
    types = ["classroom", "home"]
    ids = ["tot" if s[0] == "items" else s[0] for s in get_scores()]
    raws = range(0, 171)

    for t, i, r in itertools.product(types, ids, raws):
        row = get_row(data, t, i, r)
        assert row.is_empty() is False
        for c in ["percentile", "t"]:
            assert row.select(c).item() > 0


def inter(t: int) -> str:
    if t < 60:
        return "Typical"
    if t < 70:
        return "Some Problems"
    return "Definite Dysfunction"


def report(asmt: date, form: str, person: str, res: pl.DataFrame) -> str:
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
            f"{d}: PR {res.filter(pl.col('id') == k).select('percentile').item()} - \"{res.filter(pl.col('id') == k).select('interpretive').item()}\""
            for k, d in scores
        ]
    )


def process(
    asmt: date, form: str, person: str, raw: dict[str, int]
) -> tuple[pl.DataFrame, str]:
    data = load()

    form = form.lower()

    raw["tot"] = sum(
        [raw["vis"], raw["hea"], raw["tou"], raw["items"], raw["bod"], raw["bal"]]
    )
    del raw["items"]

    def per(p: int) -> str:
        if p == 100:
            return ">99"
        return str(p)

    res = pl.DataFrame(
        [
            [
                k,
                v,
                get_row(data, form, k, v).select("t").item(),
                per(get_row(data, form, k, v).select("percentile").item()),
                inter(get_row(data, form, k, v).select("t").item()),
            ]
            for k, v in raw.items()
        ],
        schema=["id", "raw", "t", "percentile", "interpretive"],
    )

    return res, report(asmt, form, person, res)
