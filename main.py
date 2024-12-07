import pandas as pd
import matplotlib.pyplot as plt
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

df['Rank'].value_counts().plot(kind= 'pie')
plt.show()

df.plot(x = 'Rating', y = 'Category', kind = 'scatter')
plt.show()

df['Category'].value_couts().plot(kind = 'bar', figsize = (8, 5))
plt.show()

df['Rating'].plot(kind='hist', bins=5)

df[df['Type'] == 'Paid']['Price'].plot(kind = 'box')
plt.show()


