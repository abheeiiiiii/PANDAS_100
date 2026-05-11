import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    

    logins_2020 = logins[logins["time_stamp"].dt.year == 2020]
 
    result = (
        logins_2020
        .groupby("user_id", as_index=False)["time_stamp"]
        .max()
    )
    

    result = result.rename(columns={"time_stamp": "last_stamp"})
    
    return result