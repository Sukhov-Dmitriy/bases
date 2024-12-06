import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 13)
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_colwidth', 45)
pd.set_option('display.width', 80)

df = pd.read_csv("taxi.csv", sep=';')
df['pickup'] = pd.to_datetime(df['pickup'])
df['dropoff'] = pd.to_datetime(df['dropoff'])
df['duration'] = df['dropoff'] - df['pickup']
print(df['duration'].dt.total_seconds().mean())
