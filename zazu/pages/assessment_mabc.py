import datetime

import streamlit as st
from dateutil.relativedelta import relativedelta

from asmt import mabc


@st.cache()
def load():
    st.write("Cache miss")
    return mabc.load()


st.header("M ABC")

col1, col2 = st.columns(2)
birth = col1.date_input("Birthday", datetime.date.today() - relativedelta(years=6))
dat = col2.date_input("Date", datetime.date.today())

form = st.form(key="results")
sects = mabc.get_sections(birth, dat)
sect_ids = list(sects.keys())
cols = form.columns(len(sect_ids))

perf = {}

for i, col in enumerate(cols):
    sect_id = sect_ids[i]
    col.markdown(f"***{sect_id}***")
    for exe in sects[sect_id]:
        perf[exe] = col.number_input(
            label=exe.upper(), min_value=0, max_value=100, step=1
        )

submit = form.form_submit_button("Submit")

if submit:
    st.write("hello")
    st.json(perf)
    res = mabc.process(birth, dat, perf)
    st.dataframe(res)
    st.balloons()

cnt = load()
st.dataframe(cnt)
st.table(cnt)
