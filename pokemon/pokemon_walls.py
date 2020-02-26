# %% Pokemon Walls
import pandas as pd
import pokemon_utilities

pokemons = pd.read_csv("pokemons.csv").set_index("#")
types_chart = pd.read_csv("types-chart.csv").set_index("Attack")

pokemons.loc[197].to_frame().T

# %% Effective HP
pokemons["Effective HP"] = pokemon_utilities.effective_hp(pokemons["HP"])
pokemons.sort_values("Effective HP", ascending=False).filter(regex="Name|HP").head()

# %% Types Factors and Damages
for type in types_chart.iloc[:, 1:]:
    pokemons[type] = pokemon_utilities.calculate_type_damage_factors(
        types_chart, type, pokemons["Type 1"], pokemons["Type 2"]
    )
    pokemons[type + " Ph. Damage"] = pokemon_utilities.calculate_damages(
        pokemons["Defense"], pokemons[type]
    )
    pokemons[type + " Sp. Damage"] = pokemon_utilities.calculate_damages(
        pokemons["Sp. Def"], pokemons[type]
    )

# %% Average Damages
pokemons["Ph. Average Damage"] = pokemons.filter(like="Ph. Damage").mean(axis=1)
pokemons["Sp. Average Damage"] = pokemons.filter(like="Sp. Damage").mean(axis=1)
pokemons["Mix. Average Damage"] = pokemons.filter(like="Damage").mean(axis=1)

# %% Physical Walls
pokemons.sort_values("Ph. Average Damage").filter(regex="Name|Ph. Average").head()
pokemons["Ph. Attacks Sustained"] = (
    pokemons["Effective HP"] / pokemons["Ph. Average Damage"]
)
pokemons.sort_values("Ph. Attacks Sustained", ascending=False).filter(
    regex="Name|Ph. Attacks"
).head()

# %% Special Walls
pokemons.sort_values("Sp. Average Damage").filter(regex="Name|Sp. Average").head()
pokemons["Sp. Attacks Sustained"] = (
    pokemons["Effective HP"] / pokemons["Sp. Average Damage"]
)
pokemons.sort_values("Sp. Attacks Sustained", ascending=False).filter(
    regex="Name|Sp. Attacks"
).head()

# %% Mixed Walls
pokemons.sort_values("Mix. Average Damage").filter(regex="Name|Average Damage").head()
pokemons["Mix. Attacks Sustained"] = (
    pokemons["Effective HP"] / pokemons["Mix. Average Damage"]
)
pokemons.sort_values("Mix. Attacks Sustained", ascending=False).filter(
    regex="Name|Mix. Attacks"
).head()
