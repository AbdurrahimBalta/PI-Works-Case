import numpy as np
import pandas as pd


df = pd.read_csv(r"C:\Users\LENOVO\Desktop\powerBI\country_vaccination_stats.csv")

print(df.isnull().sum())

df.daily_vaccinations.fillna(0,inplace = True)


print(df.isnull().sum())



#%% quesrion 2
from collections import Counter
import pandas as pd

df = pd.read_csv(r"C:\Users\LENOVO\Desktop\powerBI\country_vaccination_stats.csv")

df.dropna(inplace = True)

unique_features_name = df.country.unique()
median_country = {}

for a in unique_features_name:

    x = df[df["country"] == a]
    median = x.daily_vaccinations.median()    
    median_country.update({ a : median})
    
k = Counter(median_country)
print(k.most_common(3))   

#%% question 3 
from collections import Counter
import pandas as pd

df = pd.read_csv(r"C:\Users\LENOVO\Desktop\powerBI\country_vaccination_stats.csv")

df.dropna(inplace = True)
print(df.info())
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')
print(df.info())

sum_date = df[df["date"] == "1/6/2021"]

print(sum_date.daily_vaccinations.sum())



#[('United States', 378253.0), ('China', 276786.0), ('India', 173922.0)]

