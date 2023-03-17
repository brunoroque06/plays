import streamlit as st

from asmt import components, mabc

st.subheader("MABC")

asmt_date, birth, age, age_disp = components.dates(5, 16)

# st.color_picker(..., disabled=True, label_visibility="collapsed") is an alternative
if age.years < 7:
    st.error(age_disp)
elif age.years < 11:
    st.success(age_disp)
else:
    st.info(age_disp)

hand = st.selectbox("Preferred Hand", ("Right", "Left"))

if not isinstance(hand, str):
    raise TypeError("not str")

comps = mabc.get_comps(age)
comp_ids = list(comps.keys())
cols = st.columns(len(comp_ids))

raw = {}

for i, col in enumerate(cols):
    comp_id = comp_ids[i]
    col.markdown(f"***{comp_id}***")
    for exe in comps[comp_id]:
        raw[exe] = col.number_input(
            label=exe.upper(),
            min_value=0,
            max_value=100,
            step=1,
        )

comp, agg, rep = mabc.process(age, raw, asmt=asmt_date, hand=hand)


def color_row(row):
    std = row["standard"]
    rank = mabc.rank(std)
    if rank == mabc.Rank.OK or rank == mabc.Rank.UOK:
        color = "rgba(33, 195, 84, 0.1)"
    elif rank == mabc.Rank.CRI:
        color = "rgba(255, 193, 7, 0.1)"
    else:
        color = "rgba(255, 43, 43, 0.09)"

    return [f"background-color: {color};"] * len(row)


st.markdown("---")

st.code(rep, language="markdown")

for c in [
    ("Handgeschicklichkeit", "hg"),
    ("Ballfertigkeiten", "bf"),
    ("Balance", "bl"),
]:
    components.table(
        comp.filter(like=c[1], axis=0).style.apply(color_row, axis=1),
        c[0],
    )

order = {"hg": 0, "bf": 1, "bl": 2, "total": 4}
components.table(
    agg.sort_values(by=["id"], key=lambda x: x.map(order))
    .style.apply(color_row, axis=1)
    .format({"percentile": "{:.1f}"}),
    "Aggregated",
)
