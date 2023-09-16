import pandas as pd

df = pd.read_csv('./pokemon_data.csv')

# for index, row in df.iterrows():
#   print(index, row)
  
# sorted = df.sort_values(['Type 1', 'HP'], ascending=[1, 0])

totalDef = df['Total Def'] = df['Defense'] + df['Sp. Def']

sortByDef = df.sort_values(['Total Def'], ascending=False)

print(sortByDef)