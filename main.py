import pandas as pd

atk_spd = pd.read_csv('attack_speed.csv')
skills = pd.read_csv('skills_db.csv')
inputs = pd.read_csv('inputs.csv')

print(inputs)

print(pd.melt(inputs, id_vars=['Class'], value_vars=['Skill_1', 'Skill_2', 'Skill_3', 'Skill_4'], var_name='skill_num', value_name='skill'))
