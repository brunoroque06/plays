import math
import typing
from datetime import date

import pandas as pd
from dateutil.relativedelta import relativedelta


def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    map_i = pd.read_csv("data/m-abc-i.csv")
    map_i["age"] = map_i.apply(
        lambda r: pd.Interval(left=r["age_min"], right=r["age_max"], closed="left"),
        axis=1,
    )
    map_i["raw"] = map_i.apply(
        lambda r: pd.Interval(left=r["raw_min"], right=r["raw_max"] + 1, closed="left"),
        axis=1,
    )
    map_i = map_i.drop(["age_max", "age_min", "raw_max", "raw_min"], axis=1)
    map_i = map_i.set_index(["age", "id", "raw"], verify_integrity=True).sort_index()

    map_t = pd.read_csv("data/m-abc-t.csv")
    map_t["raw"] = map_t.apply(
        lambda r: pd.Interval(left=r["raw_min"], right=r["raw_max"] + 1, closed="left"),
        axis=1,
    )
    map_t = map_t.drop(["raw_max", "raw_min"], axis=1)
    map_t = map_t.set_index(["id", "raw"], verify_integrity=True).sort_index()

    return map_i, map_t


def get_age(birth: date, dat: date) -> relativedelta:
    return relativedelta(dat, birth)


def get_comps(birth: date, dat: date) -> dict[str, list[str]]:
    return {
        "Handgeschicklichkeit": ["hg11", "hg12", "hg2", "hg3"],
        "Ballfertigkeiten": ["bf1", "bf2"],
        "Balance": ["bl11", "bl12", "bl2", "bl3"]
        if get_age(birth, dat).years <= 6
        else ["bl11", "bl12", "bl2", "bl31", "bl32"],
    }


def process_comp(
    map_i: pd.DataFrame, age: int, raw: dict[str, int]
) -> dict[str, list[typing.Optional[int], int, typing.Optional[int]]]:
    map_i_age = map_i.loc[age]
    comp = {}
    for k, v in raw.items():
        fil = map_i_age.loc[k].loc[v]
        comp[k] = [v, fil["standard"], fil["rank"]]

    def avg(v0: int, v1: int) -> int:
        a = (v0 + v1) / 2
        if a < 10:
            return math.floor(a)
        return math.ceil(a)

    comp["hg1"] = [None, avg(comp["hg11"][1], comp["hg12"][1]), None]
    comp["bl1"] = [None, avg(comp["bl11"][1], comp["bl12"][1]), None]
    if age > 6:
        comp["bl3"] = [None, avg(comp["bl31"][1], comp["bl32"][1]), None]

    return comp


def process_agg(
    map_t: pd.DataFrame, comp: dict[str, list[int, int]]
) -> dict[str, list[int, int, int, int]]:
    agg = {}

    for c in ["hg", "bf", "bl"]:
        score = sum(v[1] if k.startswith(c) else 0 for k, v in comp.items())
        row = map_t.loc[c].loc[score]
        agg[c] = [score, row["standard"], row["percentile"], row["rank"]]

    score = sum(v[1] for v in comp.values())
    row = map_t.loc["gw"].loc[score]
    agg["total"] = [score, row["standard"], row["percentile"], row["rank"]]

    return agg


def process(
    birth: date, dat: date, raw: dict[str, int]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    age = get_age(birth, dat).years
    map_i, map_t = load()

    comp = process_comp(map_i, age, raw)

    agg = process_agg(map_t, comp)

    comp_res = (
        pd.DataFrame(
            [[k] + v for k, v in comp.items()],
            columns=["id", "raw", "standard", "rank"],
        )
        .set_index("id")
        .sort_index()
        .astype({"raw": pd.Int64Dtype(), "rank": pd.Int64Dtype()})
    )

    agg_res = (
        pd.DataFrame(
            [[k] + v for k, v in agg.items()],
            columns=["id", "raw", "standard", "percentile", "rank"],
        )
        .set_index("id")
        .sort_index()
        .astype({"raw": int, "standard": int, "rank": int})
    )

    return comp_res, agg_res
