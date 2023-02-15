import datetime
import typing

import pandas as pd
import streamlit as st


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
@typing.no_type_check
def load() -> pd.DataFrame:
    clroom = pd.read_csv("data/spm-classroom.csv")
    clroom["type"] = "classroom"

    home = pd.read_csv("data/spm-home.csv")
    home["type"] = "home"

    both = pd.concat([clroom, home])

    both["raw"] = both.apply(
        lambda r: pd.Interval(left=r["raw_min"], right=r["raw_max"] + 1, closed="left"),
        axis=1,
    )

    both = both.drop(["raw_min", "raw_max"], axis=1)

    both = both.set_index(["type", "id", "raw"], verify_integrity=True).sort_index()

    return both


def inter(t: int) -> str:
    if t < 60:
        return "Typical"
    if t < 70:
        return "Some Problems"
    return "Definite Dysfunction"


def report(date: datetime.date, form: str, person: str, res: pd.DataFrame) -> str:
    header = [
        "Sensory Processing Measure (SPM): Classroom Form",
        f"Fragebogen zur sensorischen Verarbeitung ausgefüllt von Kinders {person} ({date.month}.{date.year})",
    ]
    if form == "home":
        header = [
            "Sensory Processing Measure (SPM): Home Form",
            f"Elternfragebogen zur sensorischen Verarbeitung ausgefüllt von {person} ({date.month}.{date.year})",
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
            f"{d}: PR {res.loc[k]['percentile']} - \"{res.loc[k]['interpretive']}\""
            for k, d in scores
        ]
    )


def process(
    date: datetime.date, form: str, person: str, raw: dict[str, int]
) -> tuple[pd.DataFrame, str]:
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

    res = pd.DataFrame(
        [
            [
                k,
                v,
                data.loc[form].loc[k].loc[v]["t"],
                per(data.loc[form].loc[k].loc[v]["percentile"]),
                inter(data.loc[form].loc[k].loc[v]["t"]),
            ]
            for k, v in raw.items()
        ],
        columns=["id", "raw", "t", "percentile", "interpretive"],
    ).set_index("id")

    return res, report(date, form, person, res)
