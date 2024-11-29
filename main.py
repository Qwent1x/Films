import pandas as pd
df = pd.read_csv('IMDB-Movie-Data.csv')
print(df.info())
# 1.Рейтиг нових фільмів краща за старі
2.
df.dropna()
print(df.info())


1 # Середній рейтинг по жанрах
genre_ratings = df.groupby('genre')['rating'].mean()
print(genre_ratings)

2 # Кількість фільмів за жанрами
genre_count = df['genre'].value_counts()
print(genre_count)

3 # Середній рейтинг фільмів по роках
yearly_ratings = df.groupby('year')['rating'].mean()
print(yearly_ratings)
