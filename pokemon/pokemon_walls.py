# %% Pokemon Walls
import pandas as pd

import pokemon_util as pu

POKEMONS = pd.read_csv("pokemons.csv").set_index("#")
TYPES = pd.read_csv("types-chart.csv").set_index("Attack")

print(POKEMONS.loc[197].to_frame().T)

# %% Effective HP
POKEMONS["Effective HP"] = pu.effective_hp(POKEMONS["HP"])
POKEMONS.sort_values("Effective HP", ascending=False).filter(regex="Name|HP").head()

# %% Type Factors and Damage
for ptype in TYPES.iloc[:, 1:]:
    POKEMONS[ptype] = pu.calculate_type_damage_factors(
        TYPES, ptype, POKEMONS["Type 1"], POKEMONS["Type 2"]
    )
    POKEMONS[ptype + " Ph. Damage"] = pu.calculate_damages(
        POKEMONS["Defense"], POKEMONS[ptype]
    )
    POKEMONS[ptype + " Sp. Damage"] = pu.calculate_damages(
        POKEMONS["Sp. Def"], POKEMONS[ptype]
    )

# %% Average Damage
POKEMONS["Ph. Average Damage"] = POKEMONS.filter(like="Ph. Damage").mean(axis=1)
POKEMONS["Sp. Average Damage"] = POKEMONS.filter(like="Sp. Damage").mean(axis=1)
POKEMONS["Mix. Average Damage"] = POKEMONS.filter(like="Damage").mean(axis=1)

# %% Physical Walls
POKEMONS.sort_values("Ph. Average Damage").filter(regex="Name|Ph. Average").head()
POKEMONS["Ph. Attacks Sustained"] = (
    POKEMONS["Effective HP"] / POKEMONS["Ph. Average Damage"]
)
POKEMONS.sort_values("Ph. Attacks Sustained", ascending=False).filter(
    regex="Name|Ph. Attacks"
).head()

# %% Special Walls
POKEMONS.sort_values("Sp. Average Damage").filter(regex="Name|Sp. Average").head()
POKEMONS["Sp. Attacks Sustained"] = (
    POKEMONS["Effective HP"] / POKEMONS["Sp. Average Damage"]
)
POKEMONS.sort_values("Sp. Attacks Sustained", ascending=False).filter(
    regex="Name|Sp. Attacks"
).head()

# %% Mixed Walls
POKEMONS.sort_values("Mix. Average Damage").filter(regex="Name|Average Damage").head()
POKEMONS["Mix. Attacks Sustained"] = (
    POKEMONS["Effective HP"] / POKEMONS["Mix. Average Damage"]
)
POKEMONS.sort_values("Mix. Attacks Sustained", ascending=False).filter(
    regex="Name|Mix. Attacks"
).head()
