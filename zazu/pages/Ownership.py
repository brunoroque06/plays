import numpy as np
import pandas as pd
import streamlit as st

st.subheader("Renting vs Owning")

st.markdown(
    "Implementation of the oversimplified <https://www.pwlcapital.com/rent-or-own-your-home-5-rule>."
)

col1, col2 = st.columns(2)
with col1:
    tax = st.slider("Property Tax [%]", 0.0, 5.0, 1.0, 0.5)
    inte = st.slider("Mortgage Interest [%]", 0.0, 5.0, 3.0, 0.5)
with col2:
    main = st.slider("Maintenance Cost [%]", 0.0, 5.0, 1.0, 0.5)
    opo = st.slider("Cost of Opportunity [%]", 0.0, 5.0, 3.0, 0.5)

cost = st.slider("House Cost [k]", 200, 2_000, 1_000, 50)


def calc_cost(pri):
    cap = 0.2 * opo + 0.8 * inte
    return (tax + main + cap) / 100 * pri / 12


st.metric(
    label="Unrecoverable Cost of Owning [/month]", value=round(calc_cost(cost * 1000))
)

prices = np.arange(200_000, 2_000_000, 50_000)
cutoffs = np.array([round(calc_cost(p)) for p in prices])
st.line_chart(
    pd.DataFrame(
        cutoffs,
        index=prices,
        columns=["Unrec. Cost Owning [/month]"],
    ),
)
