import numpy as np
import pandas as pd
import streamlit as st

st.title("Housing")

st.subheader("Renting vs Owning")

st.markdown(
    "Implementation of the oversimplified <https://www.pwlcapital.com/rent-or-own-your-home-5-rule>."
)

tax = st.slider("Tax [%]", 0.0, 5.0, 1.0, 0.5)
main = st.slider("Maintenance [%]", 0.0, 5.0, 1.0, 0.5)
inte = st.slider("Mortgage Interest [%]", 0.0, 5.0, 3.0, 0.5)
opo = st.slider("Cost of Opportunity [%]", 0.0, 5.0, 3.0, 0.5)


def calc_cutoff(pri):
    cap = 0.2 * opo + 0.8 * inte
    return (tax + main + cap) / 100 * pri / 12


prices = np.arange(200_000, 2_000_000, 1_000)

st.markdown("---")

st.metric(label="Cutoff for 1M", value=calc_cutoff(1_000_000))

cutoffs = np.array([calc_cutoff(p) for p in prices])

st.line_chart(pd.DataFrame(cutoffs, index=prices, columns=["cutoff"]))
