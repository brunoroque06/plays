import datetime
import typing
from datetime import date

import pandas as pd
import streamlit as st
from dateutil.relativedelta import relativedelta

from asmt import dtvp, time


@st.cache_data
@typing.no_type_check
def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    std = pd.read_csv("data/dtvpa-std.csv")
    std["age"] = std.apply(
        lambda r: pd.Interval(
            left=time.delta_idx(relativedelta(years=r["age_min"])),
            right=time.delta_idx(relativedelta(years=r["age_max"])),
            closed="left",
        ),
        axis=1,
    )
    std["raw"] = std.apply(
        lambda r: pd.Interval(left=r["raw_min"], right=r["raw_max"] + 1, closed="left"),
        axis=1,
    )
    std = std.drop(["age_min", "age_max", "raw_min", "raw_max"], axis=1)
    std = std.set_index(["id", "age", "raw"], verify_integrity=True).sort_index()

    sums = pd.read_csv("data/dtvpa-sum.csv")
    sums = sums.set_index(["id", "sum"], verify_integrity=True).sort_index()

    return std, sums


def get_tests():
    return {
        "co": "Copying",
        "fg": "Figure-Ground",
        "vse": "Visual-Motor Search",
        "vc": "Visual Closure",
        "vsp": "Visual-Motor Speed",
        "fc": "Form Constancy",
    }


def report(asmt: datetime.date, sub: pd.DataFrame, comp: pd.DataFrame) -> str:
    return "\n".join(
        [
            f"Developmental Test of Visual Perception - Adolescent and Adult (DTVP-A) - ({asmt.day}.{asmt.month}.{asmt.year})",
            "",
        ]
        + [
            f"{n}: PR {comp.loc[i]['%ile']} - {dtvp.desc_index(comp.loc[i]['index'], True)}"  # type: ignore
            for n, i in [
                ("Visuomotorische Integration", "Visual-Motor Integration (VMII)"),
                (
                    "Motorik-Reduzierte Wahrnehmung",
                    "Motor-Reduced Visual Perception (MRPI)",
                ),
                ("Globale Visuelle Wahrnehmung", "General Visual Perception (GVPI)"),
            ]
        ]
        + [
            "",
            "Subtests:",
        ]
        + [
            f"{n}: PR {sub.loc[i]['%ile']} - {dtvp.desc_sca(sub.loc[i]['standard'], True)}"  # type: ignore
            for n, i in [
                ("Abzeichnen", "co"),
                ("Figur-Grund", "fg"),
                ("Visuomotorisches Suchen", "vse"),
                ("Gesaltschliessen", "vc"),
                ("Visuomotorische Geschwindigkeit", "vsp"),
                ("Formkonstanz", "fc"),
            ]
        ]
    )


def process(
    age: relativedelta, raw: dict[str, int], asmt: date | None = None
) -> tuple[pd.DataFrame, pd.DataFrame, str]:
    if asmt is None:
        asmt = date.today()

    std, sums = load()

    tests = get_tests()

    def get_std(k: str, r: int):
        l = std.loc[k].loc[time.delta_idx(age)].loc[r]
        return [
            dtvp.to_pr(l["percentile"]),
            l["standard"],
            dtvp.desc_sca(l["standard"]),
        ]

    sub = pd.DataFrame(
        [[k, v, raw[k], *get_std(k, raw[k])] for k, v in tests.items()],
        columns=["id", "label", "raw", "%ile", "standard", "description"],
    ).set_index("id")

    comps = [
        (
            "gvpi",
            "General Visual Perception (GVPI)",
            sub["standard"].sum(),  # pylint: disable=unsubscriptable-object
            "sum6",
        ),
        (
            "mrpi",
            "Motor-Reduced Visual Perception (MRPI)",
            sub.loc["fg"]["standard"]
            + sub.loc["vc"]["standard"]
            + sub.loc["fc"]["standard"],
            "sum3",
        ),
        (
            "vmii",
            "Visual-Motor Integration (VMII)",
            sub.loc["co"]["standard"]
            + sub.loc["vse"]["standard"]
            + sub.loc["vsp"]["standard"],
            "sum3",
        ),
    ]

    comp = pd.DataFrame(
        [
            [
                l,
                v,
                sums.loc[s].loc[v]["index"],
                dtvp.to_pr(sums.loc[s].loc[v]["percentile"]),
                dtvp.desc_index(sums.loc[s].loc[v]["index"]),
            ]
            for k, l, v, s in comps
        ],
        columns=["id", "sum_standard", "index", "%ile", "description"],
    ).set_index("id")

    return sub.set_index("label"), comp, report(asmt, sub, comp)
