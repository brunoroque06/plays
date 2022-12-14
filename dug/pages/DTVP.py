import time

import streamlit as st

from asmt import comp, dtvp

st.subheader("DTVP")

asmt_date, birth, age, age_disp = comp.dates(4, 13)

st.info(age_disp)

with st.form("dtvp"):
    raw = {}
    tests = dtvp.get_tests()

    for k, v in tests.items():
        raw[k] = st.number_input(v, step=1)

    submit = st.form_submit_button(type="primary")

if submit:
    with st.spinner("Processing..."):
        time.sleep(0.2)  # UX? Oo
        sub, comp = dtvp.process(age, raw)

    st.subheader("Subtest Performance")
    st.table(sub)

    st.subheader("Composite Performance")
    st.table(comp)
