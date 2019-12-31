import pandas as pd

data = pd.read_csv('data.csv', index_col='class')
atk_spd = pd.read_csv('attack_speed.csv', index_col='class')
skills_all = pd.read_csv('skills_db.csv', index_col='skill_name')

turn = []

#change 1 to 4 for all 4 classes
for i in range(0,1):
  job = data.index[i]
  speed = atk_spd.loc[job,'atk_spd']
  skills = skills_all[skills_all['class']==job].drop('class', axis=1)
  skill = skills.loc[data.iloc[i]]
  print(skill)
  
  skill_turn.append(skill.iloc[0].charge)
  print(skill_turn)

  time = 0 
  turn = 1
  action = []
  while time < 70: 
    
    action.append([turn, time, 'Basic Attack'])
    print('{0:.2f}s:'.format(time),job,'attacks')

    time = time + speed
    turn = turn + 1

