import datetime

import streamlit as st
from dateutil.relativedelta import relativedelta

from asmt import mabc


@st.cache()
def load():
    return mabc.load()


st.header("M ABC")

col1, col2 = st.columns(2)
bir = col1.date_input("Birthday", datetime.date.today() - relativedelta(years=8))
dat = col2.date_input("Date", datetime.date.today())

form = st.form(key="results")
secs = mabc.get_sections(bir, dat)
cols = form.columns(len(secs))

res = {}

for i, col in enumerate(cols):
    sec = secs[i]
    col.markdown(f"***{sec.id}***")
    for val in sec.values:
        res[val] = col.number_input(label=val.upper(), min_value=0, max_value=100, step=1)

submit = form.form_submit_button("Submit")

st.markdown(res)

if submit:
    st.write("hello")
    st.balloons()

cnt = load()
st.code(cnt.head())
