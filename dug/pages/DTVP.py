import streamlit as st

from asmt import comp, dtvp

st.subheader("DTVP")

asmt_date, birth, age, age_disp = comp.dates(4, 13)

st.info(age_disp)

raw = {}
tests = dtvp.get_tests()

for k, v in tests.items():
    raw[k] = st.number_input(v, step=1)

sub, comp, rep = dtvp.process(age, raw, asmt_date)

st.markdown("---")

st.code(rep, language="markdown")
st.table(sub.style.set_caption("Subtest"))
st.table(comp.style.set_caption("Composite"))  # pylint: disable=no-member
