import datetime

import streamlit as st

from reportus import spm, ui

ui.header("SPM")

cols = st.columns(4)
today = datetime.date.today()

with cols[0]:
    ver = st.selectbox("Version", (1, 2))
with cols[1]:
    asmt = ui.date_input("Assessment", today, max_value=today)


def ver1():
    return ver == 1


with cols[2]:
    form = st.selectbox("Form", ("Classroom", "Home") if ver1() else ("Home"))
with cols[3]:
    person = st.selectbox(
        "Filled by",
        ("Km", "Kv", "Ke") if form == "Home" else ("LP", "BP"),
    )

scores = spm.get_scores(ver)

left = ["soc", "vis", "hea"] if ver1() else ["vis", "hea", "tou", "t&s", "bod", "bal"]
right = ["tou", "t&s", "bod", "bal", "pla"] if ver1() else ["pln", "soc"]

raw: dict[str, int] = {}

cols = st.columns(2)
with cols[0]:
    for s in left:
        raw[s] = st.number_input(scores[s], step=1)

with cols[1]:
    for s in right:
        raw[s] = st.number_input(scores[s], step=1)

res, rep = spm.process(asmt, form, ver, person, raw)

st.code(rep, language="markdown")

res = res.to_pandas().set_index("id")  # type: ignore

res = res.style.format({"t": "{:.0f}"})  # type: ignore
ui.table(res)
