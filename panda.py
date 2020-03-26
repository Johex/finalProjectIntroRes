import pandas as pd

df = pd.read_csv("data.csv")


table = pd.crosstab(index=df['ev'], columns=df['year'])
table['difference in %'] = ((table[2019] - table[2018]) / table[2018] * 100)

print(table)