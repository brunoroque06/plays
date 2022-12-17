# pylint:disable=duplicate-code
# Maybe create a dtvp component?
import time

import streamlit as st

from asmt import comp, dtvpa

st.subheader("DTVPA")

asmt_date, birth, age, age_disp = comp.dates(11, 18)

st.info(age_disp)

with st.form("dtvpa"):
    raw = {}
    tests = dtvpa.get_tests()

    for k, v in tests.items():
        raw[k] = st.number_input(v, step=1)

    submit = st.form_submit_button(type="primary")

if submit:
    with st.spinner("Processing..."):
        time.sleep(0.2)  # UX? Oo
        sub, comp = dtvpa.process(age, raw)

    st.table(sub.style.set_caption("Subtest"))
    st.table(comp.style.set_caption("Composite"))  # pylint: disable=no-member
