import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    
    df1 = movie_rating.groupby('user_id').size().reset_index(name='cnt')
    df1 = df1.merge(users, on='user_id')
    df1 = df1.sort_values(['cnt', 'name'], ascending=[False, True])
    top_user = df1.iloc[0]['name']
    
    feb = movie_rating[
        (movie_rating['created_at'] >= '2020-02-01') &
        (movie_rating['created_at'] <= '2020-02-29')
    ]
    
    df2 = feb.groupby('movie_id')['rating'].mean().reset_index()
    df2 = df2.merge(movies, on='movie_id')
    df2 = df2.sort_values(['rating', 'title'], ascending=[False, True])
    top_movie = df2.iloc[0]['title']
    
    return pd.DataFrame({'results': [top_user, top_movie]})