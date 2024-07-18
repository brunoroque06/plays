import dataclasses
import itertools
import math
from datetime import date
from enum import Enum
from typing import Optional

import polars as pl
from dateutil.relativedelta import relativedelta

from reportus import perf, time


@dataclasses.dataclass(frozen=True)
class Data:
    map_i: pl.DataFrame
    map_t: pl.DataFrame

    def get_i_row(self, i: str, age: int, r: int):
        return self.map_i.filter(
            (pl.col("id") == i)
            & (pl.col("age_min") <= age)
            & (pl.col("age_max") > age)
            & (pl.col("raw_min") <= r)
            & (pl.col("raw_max") >= r)
        )

    def get_t_row(self, i: str, r: int):
        return self.map_t.filter(
            (pl.col("id") == i) & (pl.col("raw_min") <= r) & (pl.col("raw_max") >= r)
        )


@perf.cache
def _load() -> Data:
    map_i = pl.read_csv("data/mabc-i.csv")
    map_t = pl.read_csv("data/mabc-t.csv")
    return Data(map_i, map_t)


def validate():
    data = _load()
    ages = range(
        data.map_i.select("age_min").min().item(),
        data.map_i.select("age_max").max().item(),
    )
    for a in ages:
        ids = [i for lst in get_comps(relativedelta(years=a)).values() for i in lst]
        raws = range(0, 122)

        for i, r in itertools.product(ids, raws):
            row = data.get_i_row(i, a, r)
            assert row.select("standard").item() > 0

    ids = ["hg", "bf", "bl", "gw"]
    raws = range(0, 109)
    for i, r in itertools.product(ids, raws):
        row = data.get_t_row(i, r)
        assert row.select("standard").item() > 0
        assert row.select("percentile").item() > 0


def get_comps(age: relativedelta) -> dict[str, list[str]]:
    return {
        "Handgeschicklichkeit": ["hg11", "hg12", "hg2", "hg3"],
        "Ballfertigkeiten": (
            ["bf1", "bf2"] if age.years < 11 else ["bf11", "bf12", "bf2"]
        ),
        "Balance": (
            ["bl11", "bl12", "bl2", "bl3"]
            if age.years < 7
            else (
                ["bl11", "bl12", "bl2", "bl31", "bl32"]
                if age.years < 11
                else ["bl1", "bl2", "bl31", "bl32"]
            )
        ),
    }


def get_failed() -> list[str]:
    return ["hg11", "hg12", "hg2", "hg3"]


def _process_comp(
    data: Data, age: int, raw: dict[str, Optional[int]]
) -> dict[str, tuple[int | None, int]]:
    comp: dict[str, tuple[int | None, int]] = {}
    for k, v in raw.items():
        std = 1 if v is None else data.get_i_row(k, age, v).select("standard").item()
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


def _process_agg(
    data: Data, comp: dict[str, tuple[int | None, int]]
) -> dict[str, list[int]]:
    agg = {}

    for cmp in ["hg", "bf", "bl"]:
        score = sum(
            v[1] if len(k) == 3 and k.startswith(cmp) else 0 for k, v in comp.items()
        )
        row = data.get_t_row(cmp, score)
        agg[cmp] = [
            score,
            row.select("standard").item(),
            row.select("percentile").item(),
        ]

    score = sum(v[0] for v in agg.values())
    row = data.get_t_row("gw", score)
    agg["total"] = [
        score,
        row.select("standard").item(),
        row.select("percentile").item(),
    ]

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
) -> tuple[pl.DataFrame, pl.DataFrame, str]:
    if asmt is None:
        asmt = date.today()

    data = _load()

    comp = _process_comp(data, age.years, raw)

    agg = _process_agg(data, comp)

    comp_res = pl.DataFrame(
        [[k, *list(v)] for k, v in comp.items()],
        schema=["id", "raw", "standard"],
        orient="row"
    )

    agg_res = pl.DataFrame(
        [[k, *list(v)] for k, v in agg.items()],
        schema=["id", "raw", "standard", "percentile"],
        orient="row"
    )

    return comp_res, agg_res, report(asmt, age, hand, agg_res)


def report(asmt: date, age: relativedelta, hand: str, agg: pl.DataFrame) -> str:
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

    def perc(i: str):
        return agg.filter(pl.col("id") == i).select("percentile").item()

    def std(i: str):
        return agg.filter(pl.col("id") == i).select("standard").item()

    tot = agg.filter(pl.col("id") == "total")

    return "\n".join(
        [
            f"Movement Assessment Battery for Children 2nd Edition (M-ABC 2) - {time.format_date(asmt)}",
            f"Protokollbogen Altersgruppe: {group} Jahre",
            "",
            f"Handgeschicklichkeit: PR {perc('hg')} - {rank_str(std('hg'))}",
            f"Händigkeit: {'Rechts' if hand == 'Right' else 'Links'}",
            f"Ballfertigkeit: PR {perc('bf')} - {rank_str(std('bf'))}",
            f"Balance: PR {perc('bl')} - {rank_str(std('bl'))}",
            "",
            f"Gesamttestwert: PR {tot.select('percentile').item()} - {rank_str(tot.select('standard').item())}",
        ]
    )
