from typing import Callable

import streamlit as st
from dateutil.relativedelta import relativedelta

from asmt import components, mabc

st.subheader("MABC")


def display_age(a: relativedelta) -> Callable:
    if a.years < 7:
        return st.error
    if a.years < 11:
        return st.success
    return st.info


asmt_date, birth, age = components.dates(5, 16, display_age)

comps = mabc.get_comps(age)
comp_ids = list(comps.keys())

cols = st.columns([1, 2])
with cols[0]:
    hand = st.selectbox("Preferred Hand", ("Right", "Left"))

if not isinstance(hand, str):
    raise TypeError("not str")

with cols[1]:
    failed = st.multiselect("Failed", mabc.get_failed(), format_func=str.upper)

cols = st.columns(len(comp_ids))

raw = {}

for i, col in enumerate(cols):
    comp_id = comp_ids[i]
    col.markdown(f"***{comp_id}***")
    for exe in comps[comp_id]:
        raw[exe] = col.number_input(
            label=exe.upper(),
            min_value=0,
            max_value=150,
            step=1,
            disabled=(exe in failed),
        )

for f in failed:
    raw[f] = None

comp, agg, rep = mabc.process(age, raw, asmt=asmt_date, hand=hand)


def color_row(row):
    std = row["standard"]
    rank = mabc.rank(std)
    if rank in (mabc.Rank.OK, mabc.Rank.UOK):
        color = "rgba(33, 195, 84, 0.1)"
    elif rank == mabc.Rank.CRI:
        color = "rgba(255, 193, 7, 0.1)"
    else:
        color = "rgba(255, 43, 43, 0.09)"

    return [f"background-color: {color};"] * len(row)


st.divider()

st.code(rep, language="markdown")

for c in [
    ("Handgeschicklichkeit", "hg"),
    ("Ballfertigkeiten", "bf"),
    ("Balance", "bl"),
]:
    components.table(
        comp.filter(like=c[1], axis=0)
        .sort_values(
            by=["id"],
            key=lambda s: s.map(lambda i: i if len(i) == 4 else i + "z"),
        )
        .style.apply(color_row, axis=1),
        c[0],
    )

order = {"hg": 0, "bf": 1, "bl": 2, "total": 4}
components.table(
    agg.sort_values(by=["id"], key=lambda x: x.map(order))
    .style.apply(color_row, axis=1)
    .format({"percentile": "{:.1f}"}),
    "Aggregated",
)
