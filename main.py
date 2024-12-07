import pandas as pd
df = pd.read_csv('IMDB-Movie-Data.csv')
print(df.info())
# 1.Рейтиг нових фільмів краща за старі
2.
df.dropna()
print(df.info())
print(df.groupby(by = "Year")['Rating'] > 4.9)