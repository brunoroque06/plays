from datetime import date

import streamlit as st

from reportus import components, spm

st.subheader("SPM")

cols = st.columns(3)
today = date.today()
with cols[0]:
    asmt = components.date_input("Assessment", today, max_value=today)
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
    not isinstance(asmt, date)
    or not isinstance(form, str)
    or not isinstance(person, str)
):
    raise TypeError("type error")

res, rep = spm.process(asmt, form, person, raw)

st.code(rep, language="markdown")

components.table(res.to_pandas().set_index("id"))
