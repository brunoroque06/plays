from collections import defaultdict

import streamlit as st

ints = {
    "ci": {"name": "Cerebellar Integrity"},
    "dpc": {"name": "Dynamic Postural Control"},
    "lmt": {"name": "Low Muscle Tone"},
    "mp": {"name": "Motor Planning"},
    "op": {"name": "Ocular Control/Motor Planning"},
    "pp": {"name": "Proprioception Processing"},
    "ps": {"name": "Postural Stability"},
    "sp": {"name": "Somatosensory Processing"},
    "sq": {"name": "Sequencing"},
    "ti": {"name": "Timing"},
    "vep": {"name": "Vestibular Processing"},
    "vip": {"name": "Visual Processing"},
}

obs = {
    "fam": {"name": "Forearm Alternating Movements", "ints": ("ci", "mp", "sp", "sq")},
    "sft": {
        "name": "Sequential Finger Touching",
        "ints": ("ci", "mp", "sp", "sq", "ti"),
    },
    "fnt": {"name": "Finger-to-Nose Test", "ints": ("ci", "mp", "sp")},
    "srm": {"name": "Slow Ramp Movements", "ints": ("pp", "lmt")},
    "om": {"name": "Ocular Movements", "ints": ("dpc", "op", "ps", "pp", "vep", "vip")},
    "rom": {"name": "Romberg's", "ints": ("ps", "pp", "vep", "vip")},
    "srom": {"name": "Sharpened Romberg's", "ints": ("ps", "pp", "vep", "vip")},
}

st.subheader("Observations (Draft)")

scores = {}

cols_num = 3
obs_items = list(obs.items())
for i in range(0, len(obs), cols_num):
    cols = st.columns(cols_num)
    for c in range(0, cols_num):
        if len(obs_items) == i + c:
            break
        k, v = obs_items[i + c]
        scores[k] = cols[c].selectbox(
            v["name"], options=("Bellow", "Average", "Superior"), index=1
        )

int_scores = defaultdict(list)
for ik, iv in ints.items():
    for ok, ov in obs.items():
        if ik in obs[ok]["ints"]:
            sc = scores[ok]
            int_scores[ik].append((ok, sc))


def avg(vals: list[tuple[str, str]]) -> float:
    def quant(v: str) -> int:
        if v == "Bellow":
            return -1
        if v == "Average":
            return 0
        return 1

    return sum([quant(val) for _, val in vals]) / len(vals)


for k, v in int_scores.items():
    a = avg(v)
    c = ":blue["
    if a < -0.3:
        c = ":red[↓"
    elif a > 0.3:
        c = ":green[↑"

    c1, c2, c3 = st.columns([3, 1, 4])
    with c1:
        st.write("")  # Streamlit issue: Vertical alignment for columns
        st.write(f"{ints[k]['name']}")
    with c2:
        st.write("")
        st.write(f"{c}{avg(v):.1f}]")
    with c3:
        with st.expander(f"Details ({len(v)})"):
            for i, s in v:
                st.write(f"{obs[i]['name']} - {s}")
