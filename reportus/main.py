import streamlit as st

st.set_page_config(
    initial_sidebar_state="expanded", page_icon=":sparkles:", page_title="Reportus"
)


def page(file: str, title: str):
    return st.Page(file, title=title)


pages = [
    ("pages/dtvp3.py", "DTVP-3"),
    ("pages/dtvpa.py", "DTVP-A"),
    ("pages/mabc.py", "MABC"),
    ("pages/spm.py", "SPM"),
]
pages = [page(file, title) for file, title in pages]

pg = st.navigation(pages)

pg.run()
