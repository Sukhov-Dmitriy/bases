import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 13)
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_colwidth', 45)
pd.set_option('display.width', 80)

df = pd.read_csv("taxi.csv", sep=';')
top_5_tips = df.nlargest(3,'tip')

total_tips = top_5_tips['tip'].sum()

print(f"Совокупная сумма чаевых топ-3 поездок: {total_tips:.2f} долларов")