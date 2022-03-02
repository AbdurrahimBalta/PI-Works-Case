from collections import Counter
import pandas as pd

df = pd.read_csv(r"C:\Users\LENOVO\Desktop\PI-Works-Case\country_vaccination_stats.csv")

df.dropna(inplace = True)

unique_features_name = df.country.unique()
median_country = {}

for a in unique_features_name:

    x = df[df["country"] == a]
    median = x.daily_vaccinations.median()    
    median_country.update({ a : median})
    
k = Counter(median_country)
print(k.most_common(3))   
