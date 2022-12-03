import pandas as pd
from dateutil.relativedelta import relativedelta

from asmt import time


def load():
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

    return ra, rs
