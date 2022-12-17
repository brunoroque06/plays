import typing

import pandas as pd
from dateutil.relativedelta import relativedelta

from asmt import time


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


def process(
    age: relativedelta, raw: dict[str, int]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    std, sums = load()

    tests = get_tests()

    def get_std(k: str, r: int):
        l = std.loc[k].loc[time.delta_idx(age)].loc[r]
        return [l["percentile"], l["standard"]]

    sub = pd.DataFrame(
        [[k, v, raw[k]] + get_std(k, raw[k]) for k, v in tests.items()],
        columns=["id", "label", "raw", "%ile", "standard"],
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
                sums.loc[s].loc[v]["percentile"],
            ]
            for k, l, v, s in comps
        ],
        columns=["id", "sum_standard", "index", "%ile"],
    ).set_index("id")

    return sub.set_index("label"), comp
