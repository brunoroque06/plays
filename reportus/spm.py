import dataclasses
import datetime
import itertools
from typing import Literal

import polars as pl

from reportus import perf, time

Version = Literal[1, 2]


def get_scores() -> dict[str, str]:
    return {
        "vis": "Vision",
        "hea": "Hearing",
        "tou": "Touch",
        "t&s": "Taste and Smell",
        "bod": "Body Awareness",
        "bal": "Balance and Motion",
        "pln": "Planning and Ideas",
        "soc": "Social",
    }


@dataclasses.dataclass(frozen=True)
class Data:
    data: pl.DataFrame

    def get_row(self, form: str, i: str, r: int):
        return self.data.filter(
            (pl.col("type") == form)
            & (pl.col("id") == i)
            & (pl.col("raw_min") <= r)
            & (pl.col("raw_max") >= r)
        )


@perf.cache
def _load() -> Data:
    classroom = pl.read_csv("data/spm-classroom.csv")
    classroom = classroom.with_columns(pl.lit("classroom1").alias("type"))

    home = pl.read_csv("data/spm-home.csv")
    home = home.with_columns(pl.lit("home1").alias("type"))

    home2 = pl.read_csv("data/spm2-home.csv")
    home2 = home2.with_columns(pl.lit("home2").alias("type"))

    return Data(pl.concat([classroom, home, home2]))


def validate(ver: Version):
    data = _load()
    types = ["classroom", "home"] if ver == 1 else ["home"]
    ids = list(get_scores().keys())
    if ver == 1:
        ids.remove("t&s")
    ids.append("st")
    raws = range(0, 171)

    for t, i, r in itertools.product(types, ids, raws):
        row = data.get_row(t + str(ver), i, r)
        assert row.is_empty() is False
        for c in ["percentile", "t"]:
            assert row.select(c).item() > 0


def _report(
    asmt: datetime.date, form: str, person: str, ver: Version, res: pl.DataFrame
) -> str:
    asmt_fmt = time.format_date(asmt, False)
    spm = "SPM" if ver == 1 else "SPM 2"
    header = [
        f"Sensory Processing Measure ({spm}): Classroom Form",
        f"Fragebogen zur sensorischen Verarbeitung ausgefüllt von Kinders {person} ({asmt_fmt})",
    ]
    if form == "home":
        header = [
            f"Sensory Processing Measure ({spm}): Home Form",
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
        ("pln", "Planning and Ideas"),
        ("st", "Gesamttestwert"),
    ]

    return "\n".join(
        header
        + [
            f'{d}: PR {res.filter(pl.col("id") == i).select("percentile").item()} - "{res.filter(pl.col("id") == i).select("interpretive").item()}"'
            for i, d in scores
        ]
    )


def process(
    asmt: datetime.date,
    form: str,
    ver: Version,
    person: str,
    raw: dict[str, int],
) -> tuple[pl.DataFrame, str]:
    data = _load()

    form = f"{form.lower()}{ver}"

    def ver1():
        return ver == 1

    raw["st"] = sum(
        [raw["vis"], raw["hea"], raw["tou"], raw["t&s"], raw["bod"], raw["bal"]]
    )

    def per(p: int) -> str:
        if p == 100:
            return ">99"
        return str(p)

    def inter(t: int) -> tuple[str, int]:
        if t < 60:
            return ("Typical", 0)
        if t < 70:
            return ("Some Problems" if ver1() else "Moderate Difficulties", 1)
        return ("Definite Dysfunction" if ver1() else "Severe Difficulties", 2)

    def form_row(i: str, r: int):
        if ver1() and i == "t&s":
            return ["t&s", r, None, None, None, None]
        row = data.get_row(form, i, r)
        return [
            i,
            r,
            row.select("t").item(),
            per(row.select("percentile").item()),
            *inter(row.select("t").item()),
        ]

    res = pl.DataFrame(
        [form_row(i, r) for i, r in raw.items()],
        orient="row",
        schema=["id", "raw", "t", "percentile", "interpretive", "level"],
    )

    return res, _report(asmt, form, person, ver, res)
