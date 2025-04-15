import typing

import streamlit as st

from reportus import dtvp, dtvpa, ui


def page(rep: typing.Literal["dtvp3", "dtvpa"]) -> None:
    if rep == "dtvp3":
        title = "DTVP-3"
        min_age = 4
        max_age = 13
        mod = dtvp
    else:
        title = "DTVP-A"
        min_age = 11
        max_age = 18
        mod = dtvpa

    ui.header(title)

    asmt_date, _, age = ui.dates(min_age, max_age)

    raw: dict[str, int] = {}
    tests = mod.get_tests()

    cols = st.columns(3)
    for k, v in tests.items():
        with cols[1]:
            raw[k] = st.number_input(v, step=1)

    sub, comp, report = mod.process(age, raw, asmt_date)

    sub = sub.to_pandas().drop(columns=["id"]).set_index("label")  # type: ignore
    comp = comp.to_pandas().set_index("id")  # type: ignore

    st.code(report, language="markdown")
    ui.table(sub, "Subtest")
    ui.table(comp, "Composite")
