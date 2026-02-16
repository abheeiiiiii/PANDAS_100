import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity["activity_date"] = pd.to_datetime(activity["activity_date"])
    
    start_date = pd.to_datetime("2019-06-28")
    end_date = pd.to_datetime("2019-07-27")
    
    df = activity[(activity["activity_date"] >= start_date) & (activity["activity_date"] <= end_date)]
    
    result = df.groupby("activity_date")["user_id"].nunique().reset_index()
    result.columns = ["day", "active_users"]
    
    return result
