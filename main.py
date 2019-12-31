import pandas as pd

atk_spd = pd.read_csv('attack_speed.csv', index_col='class')
skills = pd.read_csv('skills_db.csv', index_col='skill_name')
data = pd.read_csv('data.csv')

char = []

#for each character, find the attack speed and charges for each skills
for i in range(0,4):
  char_class = data.iloc[i][0]
  char_speed = atk_spd.loc[char_class,'atk_spd']
  char_skills = []
  skill_charge = []

  for n in range(1,5):
    skill = data.iloc[i][n]
    char_skills.append(skill)
    temp = skills[skills['class']==char_class]
    skill_charge.append(int(temp.loc[skill,'charge']))

  if False:
    print(char_class,':')
    print('  attack speed =',atk_spd.loc[char_class,'atk_spd'])
    for j in range(0,4): 
      print('  skill {} = {} ({})'.format(j+1,char_skills[j],skill_charge[j]))
    print()

  time = 0
  count = 0
  last_skill = 0 
  temp = []

  while time < 70:
    time = time + char_speed
    count = count + 1
    temp.append(time)
  
  char.append(temp)

while True: 
  turn_min = min(char[0][0], char[1][0], char[2][0], char[3][0])
  for m in range(0,4):
    if turn_min == char[m][0]:
      time = char[m].pop(0)
      print('{0:.2f}s:'.format(time), '{} attacks'.format(data.iloc[m][0]))
      break

  left = len(char[0]) + len(char[1]) + len(char[2]) + len(char[3])
  if left == 0:
    break


