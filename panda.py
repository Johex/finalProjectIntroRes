import pandas as pd

df = pd.read_csv("data.csv")


pd.crosstab(index=df['ev'], columns=df['year'])
