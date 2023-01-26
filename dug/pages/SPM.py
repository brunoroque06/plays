import datetime

import streamlit as st

from asmt import spm

st.subheader("SPM")

today = datetime.date.today()
date = st.date_input("Assessment", today, max_value=today)

form = st.selectbox("Form", ("Classroom", "Home"))

scores = spm.get_scores()

raw = {}

dist = [(0, 3), (3, len(scores))]
cols = st.columns(len(dist))

for idx, (s, e) in enumerate(dist):
    for i in range(s, e):
        raw[scores[i][0]] = cols[idx].number_input(scores[i][1], step=1)

if not isinstance(date, datetime.date) or not isinstance(form, str):
    raise TypeError("type error")

res, rep = spm.process(date, form, raw)

st.markdown("---")

st.code(rep, language="markdown")

st.table(res)
