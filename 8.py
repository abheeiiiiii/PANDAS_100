import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered_customers = set(orders["customerId"])
    result = customers[~customers["id"].isin(ordered_customers)][["name"]]
    result.columns = ["Customers"]
    return result