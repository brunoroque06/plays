import typing
from dataclasses import dataclass
from datetime import date

import pandas as pd
from dateutil.relativedelta import relativedelta


def load() -> pd.DataFrame:
    df = pd.read_csv("data/m-abc-i.csv")
    df["age"] = df.apply(
        lambda r: pd.Interval(left=r["age_min"], right=r["age_max"], closed="left"),
        axis=1,
    )
    df["val"] = df.apply(
        lambda r: pd.Interval(left=r["val_min"], right=r["val_max"], closed="both"),
        axis=1,
    )
    df = df.drop(["age_min", "age_max", "val_min", "val_max"], axis=1)
    return df


@dataclass
class Section:
    id: str
    values: typing.List[str]


def get_sections(bir: date, dat: date) -> typing.List[Section]:
    hand = Section(id="Handgeschicklichkeit", values=["hg11", "hg12", "hg2", "hg3"])
    ball = Section(id="Ballfertigkeiten", values=["bf1", "bf2"])
    balance = Section(id="Balance", values=["bl11", "bl12", "bl2"])
    if relativedelta(dat, bir).years <= 6:
        balance.values.append("bl3")
    else:
        balance.values.extend(["bl31", "bl32"])
    return [hand, ball, balance]
