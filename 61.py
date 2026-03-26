import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start = activity[activity['activity_type'] == 'start']
    end = activity[activity['activity_type'] == 'end']

    merged = pd.merge(start, end, on=['machine_id', 'process_id'])
    merged['time'] = merged['timestamp_y'] - merged['timestamp_x']

    result = merged.groupby('machine_id')['time'].mean().reset_index()
    result['processing_time'] = result['time'].round(3)

    return result[['machine_id', 'processing_time']]