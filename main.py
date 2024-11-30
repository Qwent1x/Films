import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('IMDB-Movie-Data.csv')
print(df.info())
# 1.Рейтиг нових фільмів краща за старі
2.
df.dropna()
print(df.info())


1 # Середній рейтинг по жанрах
genre_ratings = df.groupby('Genre')['Rating'].mean()
print(genre_ratings)

2 # Кількість фільмів за жанрами
genre_count = df['Genre'].value_counts()
print(genre_count)

3 # Середній рейтинг фільмів по роках
yearly_ratings = df.groupby('Year')['Rating'].mean()
print(yearly_ratings)


df['Rank'].value_counts().plot(kind= 'pie')
plt.show()