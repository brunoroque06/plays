import typing

import pandas as pd
import streamlit as st
from dateutil import relativedelta

from reportus import mabc, ui

ui.header("MABC")


def display_age(a: relativedelta.relativedelta) -> typing.Callable:
    if a.years < 7:
        return st.error
    if a.years < 11:
        return st.success
    return st.info


asmt_date, birth, age = ui.dates(5, 16, display_age)

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


def leveler(row: pd.DataFrame) -> ui.RowLevel:
    std = row["standard"]
    rank = mabc.rank(std)  # pyright: ignore
    if rank in (mabc.Rank.OK, mabc.Rank.UOK):
        return ui.RowLevel.OK
    elif rank == mabc.Rank.CRI:
        return ui.RowLevel.CRI
    return ui.RowLevel.NOK


st.code(rep, language="markdown")

for c in [
    ("Handgeschicklichkeit", "hg"),
    ("Ballfertigkeiten", "bf"),
    ("Balance", "bl"),
]:
    cat = (
        comp.to_pandas()
        .astype({"raw": pd.Int64Dtype()})
        .set_index("id")
        .filter(like=c[1], axis=0)
        .sort_values(
            by=["id"],
            key=lambda s: s.map(lambda i: i if len(i) == 4 else i + "z"),
        )
    )
    cat = ui.table_style_levels(cat, leveler)
    ui.table(cat, c[0])

order = {"hg": 0, "bf": 1, "bl": 2, "total": 4}
agg = agg.to_pandas().set_index("id").sort_values(by=["id"], key=lambda x: x.map(order))
agg = ui.table_style_levels(agg, leveler).format({"percentile": "{:.1f}"})
ui.table(agg, "Aggregated")
