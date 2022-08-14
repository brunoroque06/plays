import math
from datetime import date

import pandas as pd
from dateutil.relativedelta import relativedelta


def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    map_i = pd.read_csv("data/m-abc-i.csv")
    map_i["age"] = map_i.apply(
        lambda r: pd.Interval(left=r["age_min"], right=r["age_max"], closed="left"),
        axis=1,
    )
    map_i["perf"] = map_i.apply(
        lambda r: pd.Interval(left=r["perf_min"], right=r["perf_max"] + 1, closed="left"),
        axis=1,
    )
    map_i = map_i.drop(["age_max", "age_min", "perf_max", "perf_min"], axis=1)
    map_i = map_i.set_index(["age", "id", "perf"], verify_integrity=True).sort_index()

    map_t = pd.read_csv("data/m-abc-t.csv")
    map_t["perf"] = map_t.apply(
        lambda r: pd.Interval(left=r["perf_min"], right=r["perf_max"] + 1, closed="left"),
        axis=1,
    )
    map_t = map_t.drop(["perf_max", "perf_min"], axis=1)
    map_t = map_t.set_index(["id", "perf"], verify_integrity=True).sort_index()

    return map_i, map_t


def get_age(birth: date, dat: date) -> int:
    return relativedelta(dat, birth).years


def get_sections(birth: date, dat: date) -> dict[str, list[str]]:
    return {
        "Handgeschicklichkeit": ["hg11", "hg12", "hg2", "hg3"],
        "Ballfertigkeiten": ["bf1", "bf2"],
        "Balance": ["bl11", "bl12", "bl2", "bl3"]
        if get_age(birth, dat) <= 6
        else ["bl11", "bl12", "bl2", "bl31", "bl32"],
    }


def process(birth: date, dat: date, perf: dict[str, int]) -> pd.DataFrame:
    age = get_age(birth, dat)
    map_i, map_t = load()
    map_i_age = map_i.loc[age]
    res = {}
    for k, v in perf.items():
        fil = map_i_age.loc[k].loc[v]
        n = fil['normalized']
        l = fil['level']
        res[k] = [n, l]

    def avg(v0: int, v1: int):
        a = (v0 + v1) / 2
        if age < 10:
            return math.floor(a)
        return math.ceil(a)

    res['hg1'] = [avg(res['hg11'][0], res['hg12'][0]), None]
    res['bl1'] = [avg(res['bl11'][0], res['bl12'][0]), None]
    if age > 6:
        res['bl3'] = [avg(res['bl31'][0], res['bl32'][0]), None]

    res['hg'] = [res['hg1'][0] + res['hg2'][0] + res['hg3'][0], None]
    res['bf'] = [res['bf1'][0] + res['bf2'][0], None]
    res['bl'] = [res['bl1'][0] + res['bl2'][0] + res['bl3'][0], None]

    res['total'] = [res['hg'][0] + res['bf'][0] + res['bl'][0], None]

    for k in ['hg', 'bf', 'bl']:
        t = map_t.loc[k].loc[res[k][0]]
        l = t['level']
        n = t['normalized']
        p = t['percentage']
        res[k + 's'] = [n, l]
        res[k + 'p'] = [p, l]

    t = map_t.loc['gw'].loc[res['total'][0]]
    res['totals'] = [t['normalized'], t['level']]
    res['totalp'] = [t['percentage'], t['level']]

    return pd.DataFrame([[k] + v for k, v in res.items()], columns=['id', 'result', 'level']).set_index(
        "id").sort_index().astype({'result': int, 'level': pd.Int64Dtype()})
