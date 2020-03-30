import pandas as pd

#read the dataset
df = pd.read_csv("data.csv")

# Create crosstab
table = pd.crosstab(index=df['ev'], columns=df['year'])
# add difference in % to crosstab
table['difference in %'] = ((table[2019] - table[2018]) / table[2018] * 100)
# add absolute difference to crosstab
table['absolute difference'] = (table[2019] - table[2018])

# print crosstab
print(table)