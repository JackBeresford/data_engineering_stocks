import pandas as pd

df = pd.read_csv("https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500")
latest = df.dropna().iloc[-1]
print(f"{latest["observation_date"]}, {latest["SP500"]}")
