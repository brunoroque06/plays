import datetime

import pandas as pd
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
    age = mabc.get_age(birth, dat)
    st.text(f"Age: {age.years} years, {age.months} months, {age.days} days")

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

    def color_rank(r):
        rank = r["rank"]
        if pd.isna(rank):
            color = None
        elif rank == 0:
            color = "rgba(40, 167, 69, 0.1)"
        elif rank == 1:
            color = "rgba(255, 193, 7, 0.1)"
        else:
            color = "#ffe6e6"

        if color is None:
            return [""] * len(r)
        return [f"background-color: {color}"] * len(r)

    st.subheader("Component Results")
    # df.style.hide() is not supported at the moment
    st.table(comp.style.apply(color_rank, axis=1))
    st.subheader("Aggregated Results")
    st.table(agg.style.apply(color_rank, axis=1).format({"percentile": "{:.1f}"}))
    st.balloons()
