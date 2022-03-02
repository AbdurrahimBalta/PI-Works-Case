import numpy as np
import pandas as pd


df = pd.read_csv(r"C:\Users\LENOVO\Desktop\powerBI\country_vaccination_stats.csv")

print(df.isnull().sum())

df.daily_vaccinations.fillna(0,inplace = True)


print(df.isnull().sum())
