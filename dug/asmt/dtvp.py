import typing
from datetime import date

import pandas as pd
import streamlit as st
from dateutil.relativedelta import relativedelta

from asmt import time


@st.cache
@typing.no_type_check
def load() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    ra = pd.read_csv("data/dtvp-raw-ageeq.csv")
    ra["raw"] = ra.apply(
        lambda r: pd.Interval(left=r["raw_min"], right=r["raw_max"] + 1, closed="left"),
        axis=1,
    )
    ra["age_eq"] = ra.apply(
        lambda r: relativedelta(years=r["age_eq_y"], months=r["age_eq_m"]), axis=1  # type: ignore
    )
    ra = ra.drop(["raw_min", "raw_max", "age_eq_y", "age_eq_m"], axis=1)
    ra = ra.set_index(["id", "raw"], verify_integrity=True).sort_index()

    rs = pd.read_csv("data/dtvp-raw-sca.csv")
    rs["age"] = rs.apply(
        lambda r: pd.Interval(
            left=time.delta_idx(
                relativedelta(years=r["age_min_y"], months=r["age_min_m"])
            ),
            right=time.delta_idx(
                relativedelta(years=r["age_max_y"], months=r["age_max_m"]), inc=True
            ),
            closed="left",
        ),
        axis=1,
    )
    rs["raw"] = rs.apply(
        lambda r: pd.Interval(left=r["raw_min"], right=r["raw_max"] + 1, closed="left"),
        axis=1,
    )
    rs = rs.drop(
        ["age_min_y", "age_min_m", "age_max_y", "age_max_m", "raw_min", "raw_max"],
        axis=1,
    )
    rs = rs.set_index(["id", "age", "raw"], verify_integrity=True).sort_index()

    sp = pd.read_csv("data/dtvp-sca-per.csv")
    sp = sp.set_index(["id", "scaled"], verify_integrity=True).sort_index()

    return ra, rs, sp


def get_tests() -> dict[str, str]:
    return {
        "eh": "Eye-Hand Coordination (EH)",
        "co": "Copying (CO)",
        "fg": "Figure-Ground (FG)",
        "vc": "Visual Closure (VC)",
        "fc": "Form Constancy (FC)",
    }


def desc_sca(s: int, de: bool = False) -> str:
    if s < 4:
        return "weit unterdurchschnittlich" if de else "Very Poor"
    if s < 6:
        return "unterdurchschnittlich" if de else "Poor"
    if s < 8:
        return "unterdurchschnittlich" if de else "Below Average"
    if s < 13:
        return "durchschnittlich" if de else "Average"
    if s < 15:
        return "überdurchschnittlich" if de else "Above Average"
    if s < 17:
        return "weit überdurchschnittlich" if de else "Superior"
    return "weit überdurchschnittlich" if de else "Very Superior"


def desc_index(i: int, de: bool = False) -> str:
    if i < 70:
        return "Weit unter der Norm" if de else "Very Poor"
    if i < 80:
        return "Weit unter der Norm" if de else "Poor"
    if i < 90:
        return "Unter der Norm" if de else "Below Average"
    if i < 111:
        return "Norm" if de else "Average"
    if i < 121:
        return "Über der Norm" if de else "Above Average"
    if i < 131:
        return "Weit über der Norm" if de else "Superior"
    return "Weit über der Norm" if de else "Very Superior"


def to_pr(p: int) -> str:
    if p == 0:
        return "<1"
    if p == 100:
        return ">99"
    return str(p)


def to_age(a: str) -> str:
    if a == "3;11":
        return "<4;0"
    if a == "13;0":
        return ">12;9"
    return a


def process(
    age: relativedelta, raw: dict[str, int], asmt: date = date.today()
) -> tuple[pd.DataFrame, pd.DataFrame, str]:
    ra, rs, sp = load()

    tests = get_tests()

    def age_eq(k: str):
        a = ra.loc[k].loc[raw[k]]["age_eq"]
        return f"{a.years};{a.months}"

    def scaled(k: str):
        l = rs.loc[k].loc[time.delta_idx(age)].loc[raw[k]]
        per = l["percentile"]
        sca = l["scaled"]
        return [per, sca, desc_sca(sca)]

    sub = pd.DataFrame(
        [[k, v, raw[k], age_eq(k)] + scaled(k) for k, v in tests.items()],
        columns=["id", "label", "raw", "age_eq", "percentile", "scaled", "descriptive"],
    ).set_index("id")

    # pylint: disable=unsupported-assignment-operation,unsubscriptable-object
    comps = [
        (
            "vmi",
            "Visual-Motor Integration",
            sub.loc["eh"]["scaled"] + sub.loc["co"]["scaled"],
        ),
        (
            "mrvp",
            "Motor-reduced Visual Perception",
            sub.loc["fg"]["scaled"] + sub.loc["vc"]["scaled"] + sub.loc["fc"]["scaled"],
        ),
        (
            "gvp",
            "General Visual Perception",
            sub["scaled"].sum(),
        ),
    ]

    comp = pd.DataFrame(
        [
            [
                l,
                v,
                sp.loc[k].loc[v]["percentile"],
                desc_index(sp.loc[k].loc[v]["index"]),
                sp.loc[k].loc[v]["index"],
            ]
            for k, l, v in comps
        ],
        columns=["id", "sum_scaled", "percentile", "descriptive", "index"],
    ).set_index("id")

    rep = report(asmt, sub, comp)

    sub["age_eq"] = sub["age_eq"].apply(to_age)
    sub["percentile"] = sub["percentile"].apply(to_pr)

    comp["percentile"] = comp["percentile"].apply(to_pr)

    return sub.set_index("label"), comp, rep


def report(asmt: date, sub: pd.DataFrame, comp: pd.DataFrame) -> str:
    return "\n".join(
        [
            f"Developmental Test of Visual Perception (DTVP-3) - {asmt.day}.{asmt.month}.{asmt.year}",
            "",
        ]
        + [
            f"- {n}: PR {to_pr(comp['percentile'][i])} - {desc_index(comp['index'][i], True)}"  # type: ignore
            for n, i in [
                ("Visuomotorische Integration", 0),
                ("Visuelle Wahrnehmung mit reduzierter motorischer Reaktion", 1),
                ("Globale visuelle Wahrnehmung", 2),
            ]
        ]
        + ["", "Subtests:"]
        + [
            f"- {n}: {to_age(sub['age_eq'][i])} J ({desc_sca(sub['scaled'][i], True)})"  # type: ignore
            for n, i in [
                ("Augen-Hand-Koordination", 0),
                ("Abzeichnen", 1),
                ("Figur-Grund", 2),
                ("Gesaltschliessen", 3),
                ("Formkonstanz", 4),
            ]
        ]
    )
