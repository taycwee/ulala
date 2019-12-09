import pandas as pd

atk_spd = pd.read_csv('attack_speed.csv')
skills = pd.read_csv('skills_db.csv')
inputs = pd.read_csv('inputs.csv')

#for each character, find the attack speed and charges for each skills

char = []
clock = 0 
print(inputs.iloc[0][0])
char_class = inputs.iloc[0][0]
#speed = atk_spd['class'=char_class]

print(char_class)

#while clock <= 60: 

