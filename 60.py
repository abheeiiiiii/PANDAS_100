import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_users = users['user_id'].nunique()
    df = register.groupby('contest_id')['user_id'].nunique().reset_index()
    df['percentage'] = (df['user_id'] / total_users * 100).round(2)
    df = df[['contest_id', 'percentage']]
    df = df.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])
    return df