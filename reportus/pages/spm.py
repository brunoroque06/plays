import datetime

import pandas as pd
import streamlit as st

from reportus import spm, ui

ui.header("SPM")

cols = st.columns(3)
today = datetime.date.today()
with cols[0]:
    asmt = ui.date_input("Assessment", today, max_value=today)
with cols[1]:
    form = st.selectbox("Form", ("Classroom", "Home"))
with cols[2]:
    person = st.selectbox(
        "Filled by",
        ("Km", "Kv", "Ke") if form == "Home" else ("LP", "BP"),
    )

scores = spm.get_scores()

raw = {}

dist = [(0, 3), (3, len(scores))]
cols = st.columns(len(dist))

for idx, (s, e) in enumerate(dist):
    for i in range(s, e):
        raw[scores[i][0]] = cols[idx].number_input(scores[i][1], step=1)

if (
    not isinstance(asmt, datetime.date)
    or not isinstance(form, str)
    or not isinstance(person, str)
):
    raise TypeError("type error")

res, rep = spm.process(asmt, form, person, raw)

st.code(rep, language="markdown")

res = res.to_pandas().set_index("id")


def leveler(row: pd.DataFrame) -> ui.RowLevel:
    des = row["interpretive"]
    if des == spm.Level.TYPICAL.value:
        return ui.RowLevel.OK
    elif des == spm.Level.DEFINITE_DYSFUNCTION.value:
        return ui.RowLevel.NOK
    return ui.RowLevel.CRI


res = ui.table_style_levels(res, leveler)
ui.table(res)
