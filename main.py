import pandas as pd

atk_spd = pd.read_csv('attack_speed.csv')
skills = pd.read_csv('skills_db.csv')
inputs = pd.read_csv('inputs.csv')

print(inputs.iloc[0][1])

