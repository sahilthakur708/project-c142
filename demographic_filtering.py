import pandas as pd
import numpy as np

df = pd.read_csv('articles.csv')

C = df['___'].mean()
m = df['___'].quantile(0.9)
q_movies = df.copy().loc[df['___'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['___']
    R = x['___']
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['____'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('___', ascending=False)

#output = q_movies[['title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].head(20).values.tolist()

