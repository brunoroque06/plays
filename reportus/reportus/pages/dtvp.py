import pandas as pd
import streamlit as st

from reportus import dtvp, dtvpa, ui


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

    def leveler(row: pd.DataFrame) -> ui.RowLevel:
        des = row[desc]
        if des in (dtvp.Level.SUPERIOR.value, dtvp.Level.VERY_SUPERIOR.value):
            return ui.RowLevel.OK
        elif des in (dtvp.Level.POOR.value, dtvp.Level.VERY_POOR.value):
            return ui.RowLevel.NOK
        return ui.RowLevel.CRI

    sub = sub.to_pandas().drop(columns=["id"]).set_index("label")
    sub = ui.table_style_levels(sub, leveler)
    comp = comp.to_pandas().set_index("id")
    comp = ui.table_style_levels(comp, leveler)

    st.code(rep, language="markdown")
    ui.table(sub, "Subtest")
    ui.table(comp, "Composite")
