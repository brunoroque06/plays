import numpy as np

def calculate_type_damage_factors(types_chart, attack_type, types1, types2):
  types1_factors = types_chart.loc[attack_type, types1].values
  types2_nulls = types2.isnull()
  types2_without_nulls = types2.replace(np.NaN, 'Normal')
  types2_factors = types_chart.loc[attack_type, types2_without_nulls].values
  types2_factors = np.where(types2_nulls, 1, types2_factors)
  return types1_factors * types2_factors

def calculate_damages(defenses, type_factors):
  level = 2 * 100 / 5 + 2
  power = 80
  attack_defense = 70 / defenses
  return ((level * power * attack_defense) / 50 + 2) * type_factors
