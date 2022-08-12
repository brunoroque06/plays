import typing
from datetime import date

import pandas as pd
from dateutil.relativedelta import relativedelta


def load() -> pd.DataFrame:
    df = pd.read_csv("data/m-abc-i.csv")
    df["age"] = df.apply(
        lambda r: pd.Interval(left=r["age_min"], right=r["age_max"], closed="left"),
        axis=1,
    )
    df["res"] = df.apply(
        lambda r: pd.Interval(left=r["res_min"], right=r["res_max"] + 1, closed="left"),
        axis=1,
    )
    df = df.drop(["age_max", "age_min", "res_max", "res_min"], axis=1)
    df = df.set_index(["age", "id", "res"], verify_integrity=True).sort_index()
    return df


def get_age(birth: date, dat: date) -> int:
    return relativedelta(dat, birth).years


def get_sections(birth: date, dat: date) -> typing.Dict[str, typing.List[str]]:
    return {
        "Handgeschicklichkeit": ["hg11", "hg12", "hg2", "hg3"],
        "Ballfertigkeiten": ["bf1", "bf2"],
        "Balance": ["bl11", "bl12", "bl2", "bl3"]
        if get_age(birth, dat) <= 6
        else ["bl11", "bl12", "bl2", "bl31", "bl32"],
    }


def process(birth: date, dat: date, perf: typing.Dict[str, int]) -> pd.DataFrame:
    age = get_age(birth, dat)
    df = load().loc[age]
    res = []
    for k, v in perf.items():
        fil = df.loc[k].loc[v]
        r = fil['normalized']
        l = fil['level']
        res.append([k, r, l])

    return pd.DataFrame(res)
