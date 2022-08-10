import datetime

import streamlit as st
from dateutil.relativedelta import relativedelta

import file
import mabc

st.header("M ABC")

col1, col2 = st.columns(2)
bir = col1.date_input("Birthday", datetime.date.today() - relativedelta(years=8))
dat = col2.date_input("Date", datetime.date.today())

form = st.form(key="results")
secs = mabc.get_sections(age=dat - bir)
cols = form.columns(len(secs))

for i, col in enumerate(cols):
    sec = secs[i]
    col.markdown(f"***{sec.id}***")
    for val in sec.values:
        col.number_input(label=val.upper(), min_value=0, max_value=100, step=1)

submit = form.form_submit_button("Submit")

if submit:
    st.write("hello")

cnt = file.read("data/m-abc-i.csv")
