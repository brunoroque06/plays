from enum import Enum
from typing import Callable

import pandas as pd
from pandas.io.formats.style import Styler


class Level(Enum):
    OK = 0
    CRI = 1
    NOK = 2


def style_levels(df: pd.DataFrame, leveler: Callable[[pd.DataFrame], Level]) -> Styler:
    levels = {
        Level.OK: "rgba(33, 195, 84, 0.1)",
        Level.CRI: "rgba(255, 193, 7, 0.1)",
        Level.NOK: "rgba(255, 43, 43, 0.09)",
    }

    def color_row(row):
        lvl = leveler(row)
        color = levels[lvl]
        return [f"background-color: {color};"] * len(row)

    return df.style.apply(color_row, axis=1)
