import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    rides_sum = rides.groupby('user_id', as_index=False)['distance'].sum()
    
    df = users.merge(rides_sum, how='left', left_on='id', right_on='user_id')
    
    df['distance'] = df['distance'].fillna(0)
    
    result = df[['name', 'distance']].rename(columns={'distance': 'travelled_distance'})
    
    result = result.sort_values(by=['travelled_distance', 'name'], ascending=[False, True])
    
    return result