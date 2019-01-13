def calculate_type_damage_factors(types_chart, attack_type, types1, types2):
  types1_factor = types_chart.loc[attack_type, types1].values
  # type2_factor = types_chart.loc[attack_type, types2].values
  return types1_factor

def calculate_damages(defenses, type_factors):
  level = 2 * 100 / 5 + 2
  power = 80
  attack_defense = 70 / defenses
  return ((level * power * attack_defense) / 50 + 2) * type_factors
