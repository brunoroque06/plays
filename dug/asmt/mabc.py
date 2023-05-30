import math
import typing
from datetime import date
from enum import Enum
from typing import Optional

import pandas as pd
import streamlit as st
from dateutil.relativedelta import relativedelta

from asmt import time


@st.cache_data
@typing.no_type_check
def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    map_i = pd.read_csv("data/mabc-i.csv")
    map_i["age"] = map_i.apply(
        lambda r: pd.Interval(left=r["age_min"], right=r["age_max"], closed="left"),
        axis=1,
    )
    map_i["raw"] = map_i.apply(
        lambda r: pd.Interval(left=r["raw_min"], right=r["raw_max"] + 1, closed="left"),
        axis=1,
    )
    map_i = map_i.drop(["age_max", "age_min", "rank", "raw_max", "raw_min"], axis=1)
    map_i = map_i.set_index(["id", "age", "raw"], verify_integrity=True).sort_index()

    map_t = pd.read_csv("data/mabc-t.csv")
    map_t["raw"] = map_t.apply(
        lambda r: pd.Interval(left=r["raw_min"], right=r["raw_max"] + 1, closed="left"),
        axis=1,
    )
    map_t = map_t.drop(["rank", "raw_max", "raw_min"], axis=1)
    map_t = map_t.set_index(["id", "raw"], verify_integrity=True).sort_index()

    return map_i, map_t


def get_comps(age: relativedelta) -> dict[str, list[str]]:
    return {
        "Handgeschicklichkeit": ["hg11", "hg12", "hg2", "hg3"],
        "Ballfertigkeiten": ["bf1", "bf2"]
        if age.years < 11
        else ["bf11", "bf12", "bf2"],
        "Balance": ["bl11", "bl12", "bl2", "bl3"]
        if age.years < 7
        else ["bl11", "bl12", "bl2", "bl31", "bl32"]
        if age.years < 11
        else ["bl1", "bl2", "bl31", "bl32"],
    }


def get_failed() -> list[str]:
    return ["hg11", "hg12", "hg2", "hg3"]


def process_comp(
    map_i: pd.DataFrame, age: int, raw: dict[str, Optional[int]]
) -> dict[str, tuple[int | None, int]]:
    comp: dict[str, tuple[int | None, int]] = {}
    for k, v in raw.items():
        std = 1 if v is None else map_i.loc[k].loc[age].loc[v]["standard"]
        comp[k] = (v, std)

    def avg(v0: int, v1: int) -> int:
        a = (v0 + v1) / 2
        if a < 10:
            return math.floor(a)
        return math.ceil(a)

    comp["hg1"] = (None, avg(comp["hg11"][1], comp["hg12"][1]))
    if age > 10:
        comp["bf1"] = (None, avg(comp["bf11"][1], comp["bf12"][1]))
    if age < 11:
        comp["bl1"] = (None, avg(comp["bl11"][1], comp["bl12"][1]))
    if age > 6:
        comp["bl3"] = (None, avg(comp["bl31"][1], comp["bl32"][1]))

    return comp


def process_agg(
    map_t: pd.DataFrame, comp: dict[str, tuple[int | None, int]]
) -> dict[str, list[int]]:
    agg = {}

    for cmp in ["hg", "bf", "bl"]:
        score = sum(
            v[1] if len(k) == 3 and k.startswith(cmp) else 0 for k, v in comp.items()
        )
        row = map_t.loc[cmp].loc[score]
        agg[cmp] = [score, row["standard"], row["percentile"]]

    score = sum(v[0] for v in agg.values())
    row = map_t.loc["gw"].loc[score]
    agg["total"] = [score, row["standard"], row["percentile"]]

    return agg


class Rank(Enum):
    OK = "ok"
    UOK = "uok"
    CRI = "cri"
    NOK = "nok"


def rank(std: int) -> Rank:
    if std > 7:
        return Rank.OK
    if std == 7:
        return Rank.UOK
    if std == 6:
        return Rank.CRI
    return Rank.NOK


def process(
    age: relativedelta,
    raw: dict[str, Optional[int]],
    asmt: date | None = None,
    hand: str = "Right",
) -> tuple[pd.DataFrame, pd.DataFrame, str]:
    if asmt is None:
        asmt = date.today()

    map_i, map_t = load()

    comp = process_comp(map_i, age.years, raw)

    agg = process_agg(map_t, comp)

    comp_res = (
        pd.DataFrame(
            [[k, *list(v)] for k, v in comp.items()],
            columns=["id", "raw", "standard"],
        )
        .set_index("id")
        .sort_index()
        .astype({"raw": pd.Int64Dtype()})
    )

    agg_res = (
        pd.DataFrame(
            [[k, *list(v)] for k, v in agg.items()],
            columns=["id", "raw", "standard", "percentile"],
        )
        .set_index("id")
        .sort_index()
        .astype({"raw": int, "standard": int})
    )

    return comp_res, agg_res, report(asmt, age, hand, agg_res)


def report(asmt: date, age: relativedelta, hand: str, agg: pd.DataFrame) -> str:
    if age.years < 7:
        group = "3-6"
    elif age.years < 11:
        group = "7-10"
    else:
        group = "11-16"

    def rank_str(std: int) -> str:
        rnk = rank(std)
        if rnk == Rank.OK:
            return "unauffällig"
        if rnk == Rank.UOK:
            return "unauffällig im untersten Normbereich"
        if rnk == Rank.CRI:
            return "kritisch"
        return "therapiebedürftig"

    return "\n".join(
        [
            f"Movement Assessment Battery for Children 2nd Edition (M-ABC 2) - {time.format_date(asmt)}",
            f"Protokollbogen Altersgruppe: {group} Jahre",
            "",
            f"Handgeschicklichkeit: PR {agg.loc['hg']['percentile']} - {rank_str(agg.loc['hg']['standard'])}",
            f"Händigkeit: {'Rechts' if hand == 'Right' else 'Links'}",
            f"Ballfertigkeit: PR {agg.loc['bf']['percentile']} - {rank_str(agg.loc['bf']['standard'])}",
            f"Balance: PR {agg.loc['bl']['percentile']} - {rank_str(agg.loc['bl']['standard'])}",
            "",
            f"Gesamttestwert: PR {agg.loc['total']['percentile']} - {rank_str(agg.loc['total']['standard'])}",
        ]
    )
