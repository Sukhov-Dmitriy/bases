import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 13)
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_colwidth', 45)
pd.set_option('display.width', 80)

df = pd.read_csv("taxi.csv", sep=';')
cnt_credit = df[df['payment'] == 'credit card'].shape[0]
cnt_cash = df[df['payment'] == 'cash'].shape[0]
print(cnt_credit,cnt_cash)