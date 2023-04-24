import datetime

import pandas as pd
import streamlit as st
from dateutil.relativedelta import relativedelta
from pandas.io.formats.style import Styler


def dates(
    min_years: int, max_years: int
) -> tuple[datetime.date, datetime.date, relativedelta, str]:
    col1, col2 = st.columns(2)

    today = datetime.date.today()
    asmt = col1.date_input("Assessment", today, max_value=today)

    if not isinstance(asmt, datetime.date):
        raise TypeError("not date")

    birth = col2.date_input(
        "Birthday",
        asmt - relativedelta(years=min_years + int((max_years - min_years) / 2)),
        max_value=asmt - relativedelta(years=min_years),
        min_value=asmt - relativedelta(years=max_years - 1, days=364),
    )

    if not isinstance(birth, datetime.date):
        raise TypeError("not date")

    age = relativedelta(asmt, birth)

    age_disp = f"Age: {age.years} years, {age.months} months, {age.days} days"

    return asmt, birth, age, age_disp


def table(dt: pd.DataFrame | Styler, title: str | None = None):
    if title:
        st.text(title)
    st.dataframe(dt, use_container_width=True)


def dtvp(title: str, min_age: int, max_age: int, mod):
    st.subheader(title)

    asmt_date, _, age, age_disp = dates(min_age, max_age)

    st.info(age_disp)

    raw = {}
    tests = mod.get_tests()

    for k, v in tests.items():
        raw[k] = st.number_input(v, step=1)

    sub, comp, rep = mod.process(age, raw, asmt_date)

    st.divider()

    st.code(rep, language="markdown")
    table(sub, "Subtest")
    table(comp, "Composite")
