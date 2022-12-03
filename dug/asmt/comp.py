import datetime

import streamlit as st
from dateutil.relativedelta import relativedelta


def dates(min_years: int, max_years: int):
    col1, col2 = st.columns(2)

    today = datetime.date.today()
    asmt = col1.date_input("Assessment", today, max_value=today)

    if not isinstance(asmt, datetime.date):  # thank you mypy
        raise TypeError("not date")

    birth = col2.date_input(
        "Birthday",
        asmt - relativedelta(years=max_years - min_years),
        max_value=asmt - relativedelta(years=min_years),
        min_value=asmt - relativedelta(years=max_years - 1, days=364),
    )

    if not isinstance(birth, datetime.date):
        raise TypeError("not date")

    age = relativedelta(asmt, birth)

    age_disp = f"Age: {age.years} years, {age.months} months, {age.days} days"

    return asmt, birth, age, age_disp
