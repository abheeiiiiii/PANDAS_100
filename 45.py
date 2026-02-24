import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values("turn")
    queue["total_weight"] = queue["weight"].cumsum()
    
    result = queue[queue["total_weight"] <= 1000].iloc[-1:]
    return result[["person_name"]]