import pandas as pd
import streamlit as st

from reportus import dtvp, dtvpa, table, ui
from reportus.dtvp import Level


def page(rep: str):
    if rep == "dtvp3":
        title = "DTVP-3"
        min_age = 4
        max_age = 13
        desc = "descriptive"
        mod = dtvp
    elif rep == "dtvpa":
        title = "DTVP-A"
        min_age = 11
        max_age = 18
        desc = "description"
        mod = dtvpa
    else:
        raise ValueError(f"Unknown report: {rep}")

    ui.header(title)

    asmt_date, _, age = ui.dates(min_age, max_age)

    raw = {}
    tests = mod.get_tests()

    cols = st.columns(3)
    for k, v in tests.items():
        with cols[1]:
            raw[k] = st.number_input(v, step=1)

    sub, comp, rep = mod.process(age, raw, asmt_date)

    def leveler(row: pd.DataFrame) -> table.Level:
        des = row[desc]
        if des in (Level.SUPERIOR.value, Level.VERY_SUPERIOR.value):
            return table.Level.OK
        elif des in (Level.POOR.value, Level.VERY_POOR.value):
            return table.Level.NOK
        return table.Level.CRI

    sub = sub.to_pandas().drop(columns=["id"]).set_index("label")
    sub = table.style_levels(sub, leveler)
    comp = comp.to_pandas().set_index("id")
    comp = table.style_levels(comp, leveler)

    st.code(rep, language="markdown")
    ui.table(sub, "Subtest")
    ui.table(comp, "Composite")
