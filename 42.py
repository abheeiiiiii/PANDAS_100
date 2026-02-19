import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery["order_date"] = pd.to_datetime(delivery["order_date"])
    delivery["customer_pref_delivery_date"] = pd.to_datetime(delivery["customer_pref_delivery_date"])
    
    first_orders = delivery.sort_values("order_date").groupby("customer_id").first().reset_index()
    
    immediate = (first_orders["order_date"] == first_orders["customer_pref_delivery_date"]).sum()
    total = len(first_orders)
    
    percentage = round(immediate * 100 / total, 2)
    
    return pd.DataFrame({"immediate_percentage": [percentage]})
