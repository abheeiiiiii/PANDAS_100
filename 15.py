import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login['next_day'] = first_login['event_date'] + pd.Timedelta(days=1)

    merged = first_login.merge(
        activity,
        left_on=['player_id', 'next_day'],
        right_on=['player_id', 'event_date'],
        how='left'
    )

    fraction = round(merged['event_date_y'].notna().sum() / first_login['player_id'].nunique(), 2)
    return pd.DataFrame({'fraction': [fraction]})
