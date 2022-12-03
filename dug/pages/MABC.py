import datetime
import time

import streamlit as st

from asmt import comp, mabc

st.subheader("MABC")

asmt_date, birth, age, age_disp = comp.dates(5, 16)

# st.color_picker(..., disabled=True, label_visibility="collapsed") is an alternative
if age.years < 7:
    st.error(age_disp)
elif age.years < 11:
    st.success(age_disp)
else:
    st.info(age_disp)

hand = st.selectbox("Preferred Hand", ("Right", "Left"))

with st.form(key="mabc"):
    comps = mabc.get_comps(age)
    comp_ids = list(comps.keys())
    cols = st.columns(len(comp_ids))

    raw = {}

    for i, col in enumerate(cols):
        comp_id = comp_ids[i]
        col.markdown(f"***{comp_id}***")
        for exe in comps[comp_id]:
            raw[exe] = col.number_input(
                label=exe.upper(), min_value=0, max_value=100, step=1
            )

    submit = st.form_submit_button(type="primary")

if submit:
    with st.spinner("Processing..."):
        time.sleep(1)  # UX? Oo
        comp, agg = mabc.process(age, raw)

    def color_row(row):
        std = row["standard"]
        rank = mabc.rank(std)
        if rank == mabc.Rank.OK:
            color = "rgba(33, 195, 84, 0.1)"
        elif rank == mabc.Rank.CRI:
            color = "rgba(255, 193, 7, 0.1)"
        else:
            color = "rgba(255, 43, 43, 0.09)"

        return [f"background-color: {color};"] * len(row)

    st.subheader("Report")
    st.code(mabc.report(asmt_date, age, hand, agg), language="markdown")

    for c in [
        ("Handgeschicklichkeit", "hg"),
        ("Ballfertigkeiten", "bf"),
        ("Balance", "bl"),
    ]:
        st.subheader(c[0])
        st.table(comp.filter(like=c[1], axis=0).style.apply(color_row, axis=1))

    st.subheader("Aggregated")
    order = {"hg": 0, "bf": 1, "bl": 2, "total": 4}
    st.table(
        agg.sort_values(by=["id"], key=lambda x: x.map(order))
        .style.apply(color_row, axis=1)
        .format({"percentile": "{:.1f}"})
    )

    if 2 < datetime.date.today().month < 12:
        st.balloons()
    else:
        st.snow()
