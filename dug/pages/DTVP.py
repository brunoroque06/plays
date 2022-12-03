import streamlit as st

from asmt import comp

st.subheader("DTVP")

asmt_date, birth, age, age_disp = comp.dates(4, 12)

st.info(age_disp)

with st.form("dtvp"):
    raw = {}
    keys = [
        ("Eye-Hand Coordination (EH)", "eh"),
        ("Copying (CO)", "co"),
        ("Figure-Ground (FG)", "fg"),
        ("Visual Closure (VC)", "vc"),
        ("Form Constancy (FC)", "fc"),
    ]

    for l, i in keys:
        raw[i] = st.number_input(l, step=1)

    submit = st.form_submit_button(type="primary")
