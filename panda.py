import pandas as pd

ev2018 = pd.read_csv("EVs2018.csv")
ev2019 = pd.read_csv("EVs2018.csv")

print(pd.DataFrame.equals(ev2019, ev2018))
