import datetime
from enum import Enum
from typing import Callable

import pandas as pd
import streamlit as st
from dateutil.relativedelta import relativedelta
from pandas.io.formats.style import Styler


def header(title: str):
    st.subheader(title)


def date_input(label: str, date: datetime.date, **kwargs):
    return st.date_input(label, date, format="DD.MM.YYYY", **kwargs)


def dates(
    min_years: int,
    max_years: int,
    disp: Callable[[relativedelta], Callable] = lambda _: st.info,
) -> tuple[datetime.date, datetime.date, relativedelta]:
    col1, col2, col3 = st.columns([1, 1, 2])

    today = datetime.date.today()
    with col1:
        asmt = date_input("Assessment", today, max_value=today)

    if not isinstance(asmt, datetime.date):
        raise TypeError("not date")

    with col2:
        birth = date_input(
            "Birthday",
            asmt - relativedelta(years=min_years + int((max_years - min_years) / 2)),
            max_value=asmt - relativedelta(years=min_years),
            min_value=asmt - relativedelta(years=max_years - 1, days=364),
        )

    if not isinstance(birth, datetime.date):
        raise TypeError("not date")

    age = relativedelta(asmt, birth)

    with col3:
        st.text(" ")
        age_disp = f"Age: {age.years} years, {age.months} months, {age.days} days"
        disp(age)(age_disp, icon="🎂")
    # st.color_picker(..., disabled=True, label_visibility="collapsed") is an alternative

    return asmt, birth, age


class RowLevel(Enum):
    OK = 0
    CRI = 1
    NOK = 2


def table_style_levels(
    df: pd.DataFrame, leveler: Callable[[pd.DataFrame], RowLevel]
) -> Styler:
    levels = {
        RowLevel.OK: "rgba(33, 195, 84, 0.1)",
        RowLevel.CRI: "rgba(255, 193, 7, 0.1)",
        RowLevel.NOK: "rgba(255, 43, 43, 0.09)",
    }

    def color_row(row):
        lvl = leveler(row)
        color = levels[lvl]
        return [f"background-color: {color};"] * len(row)

    return df.style.apply(color_row, axis=1)


def table(dt: pd.DataFrame | Styler, title: str | None = None):
    if title:
        st.text(title)
    st.dataframe(dt, use_container_width=True)
