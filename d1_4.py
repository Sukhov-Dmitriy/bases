import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 13)
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_colwidth', 45)
pd.set_option('display.width', 80)

df = pd.read_csv("taxi.csv", sep=';')
crt = len(df[df['color'] == 'green'])
print(f"{df[df['color'] == 'green']['total'].mean():.1f}")