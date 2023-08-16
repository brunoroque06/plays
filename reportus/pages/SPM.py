from datetime import date

import streamlit as st

from asmt import components, spm

st.subheader("SPM")

cols = st.columns(3)
today = date.today()
asmt = cols[0].date_input("Assessment", today, max_value=today)
form = cols[1].selectbox("Form", ("Classroom", "Home"))
person = cols[2].selectbox(
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

st.divider()

st.code(rep, language="markdown")

components.table(res)
