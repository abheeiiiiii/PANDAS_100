import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    users = users[users['banned'] == 'No'][['users_id']]
    
    trips = trips.merge(users, left_on='client_id', right_on='users_id') \
                 .merge(users, left_on='driver_id', right_on='users_id')
    
    trips = trips[
        (trips['request_at'] >= '2013-10-01') &
        (trips['request_at'] <= '2013-10-03')
    ]
    
    total = trips.groupby('request_at').size()
    cancelled = trips[trips['status'] != 'completed'].groupby('request_at').size()
    
    result = (
        (cancelled / total)
        .fillna(0)
        .round(2)
        .reset_index()
        .rename(columns={'request_at': 'Day', 0: 'Cancellation Rate'})
    )
    
    return result
