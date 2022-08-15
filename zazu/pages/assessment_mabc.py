import datetime

import streamlit as st
from dateutil.relativedelta import relativedelta

from asmt import mabc


@st.cache()
def load():
    return mabc.load()


st.header("M ABC")

with st.sidebar:
    col1, col2 = st.columns(2)
    birth = col1.date_input("Birthday", datetime.date.today() - relativedelta(years=6))
    dat = col2.date_input("Date", datetime.date.today())

form = st.form(key="results")
comps = mabc.get_comps(birth, dat)
comp_ids = list(comps.keys())
cols = form.columns(len(comp_ids))

raw = {}

for i, col in enumerate(cols):
    comp_id = comp_ids[i]
    col.markdown(f"***{comp_id}***")
    for exe in comps[comp_id]:
        raw[exe] = col.number_input(
            label=exe.upper(), min_value=0, max_value=100, step=1
        )

submit = form.form_submit_button("Submit")

if submit:
    with st.spinner("Processing..."):
        comp, agg = mabc.process(birth, dat, raw)
    st.subheader("Component Results")
    st.table(comp)
    st.subheader("Total Results")
    st.table(agg.style.format({"percentile": "{:.1f}"}))
    st.balloons()
