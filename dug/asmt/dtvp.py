import pandas as pd
from dateutil.relativedelta import relativedelta

from asmt import time


def load() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    ra = pd.read_csv("data/dtvp-raw-ageeq.csv")
    ra["raw"] = ra.apply(
        lambda r: pd.Interval(left=r["raw_min"], right=r["raw_max"] + 1, closed="left"),
        axis=1,
    )
    ra["age_eq"] = ra.apply(
        lambda r: relativedelta(years=r["age_eq_y"], months=r["age_eq_m"]), axis=1
    )
    ra = ra.drop(["raw_min", "raw_max", "age_eq_y", "age_eq_m"], axis=1)
    ra = ra.set_index(["id", "raw"], verify_integrity=True).sort_index()

    rs = pd.read_csv("data/dtvp-raw-sca.csv")
    rs["age_min"] = rs.apply(
        lambda r: relativedelta(years=r["age_min_y"], months=r["age_min_m"]), axis=1
    )
    rs["age_max"] = rs.apply(
        lambda r: relativedelta(years=r["age_max_y"], months=r["age_max_m"]), axis=1
    )
    rs["age"] = rs.apply(
        lambda r: pd.Interval(
            left=time.delta_idx(r["age_min"]),
            right=time.delta_idx(r["age_max"], inc=True),
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


def process(
    age: relativedelta, raw: dict[str, int]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    ra, rs, sp = load()

    tests = get_tests()

    def desc_sca(v: int) -> str:
        if v < 4:
            return "Very Poor"
        if v < 6:
            return "Poor"
        if v < 8:
            return "Below Average"
        if v < 13:
            return "Average"
        if v < 15:
            return "Above Average"
        if v < 17:
            return "Superior"
        return "Very Superior"

    def age_eq(k: str):
        a = ra.loc[k].loc[raw[k]]["age_eq"]
        return f"{a.years};{a.months}"

    def scaled(k: str):
        # todo: finish dtvp-raw-sca
        # l = rs.loc[k].loc[time.delta_idx(age)].loc[raw[k]]
        # per = l["percentile"]
        # sca = l["scaled"]
        per = 25
        sca = 10
        return [per, sca, desc_sca(sca)]

    sub = pd.DataFrame(
        [[k, tests[k], raw[k], age_eq(k)] + scaled(k) for k in tests.keys()],
        columns=["id", "label", "raw", "age_eq", "percentile", "scaled", "descriptive"],
    ).set_index("id")

    comps = [
        (
            "vmi",
            "Visual-Motor Integration",
            sub.loc["eh"]["scaled"] + sub.loc["co"]["scaled"],
        ),
        (
            "mrvp",
            "Motor-reduced Visual Perception",
            sub.loc["fg"]["scaled"] + sub.loc["vc"]["scaled"] + sub.loc["vc"]["scaled"],
        ),
        ("gvp", "General Visual Perception", sub["scaled"].sum()),
    ]

    def desc_index(v: int) -> str:
        if v < 70:
            return "Very Poor"
        if v < 80:
            return "Poor"
        if v < 90:
            return "Below Average"
        if v < 111:
            return "Average"
        if v < 121:
            return "Above Average"
        if v < 131:
            return "Superior"
        return "Very Superior"

    comp = pd.DataFrame(
        [
            [
                l,
                v,
                sp.loc[k].loc[v]["percentile"],
                desc_index(sp.loc[k].loc[v]["percentile"]),
                sp.loc[k].loc[v]["index"],
            ]
            for k, l, v in comps
        ],
        columns=["id", "sum_scaled", "percentile", "descriptive", "index"],
    ).set_index("id")

    return sub.set_index("label"), comp
