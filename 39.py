import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders["order_date"] = pd.to_datetime(orders["order_date"])
    
    orders_2019 = orders[orders["order_date"].dt.year == 2019]
    
    counts = orders_2019.groupby("buyer_id").size().reset_index(name="orders_in_2019")
    
    result = users.merge(counts, how="left", left_on="user_id", right_on="buyer_id")
    
    result["orders_in_2019"] = result["orders_in_2019"].fillna(0).astype(int)
    
    result = result.drop(columns=["buyer_id"])
    result = result.rename(columns={"user_id": "buyer_id"})
    
    return result[["buyer_id", "join_date", "orders_in_2019"]]
