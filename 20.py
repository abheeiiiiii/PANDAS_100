import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return (
        orders
        .groupby("customer_number")
        .size()
        .reset_index(name="cnt")
        .sort_values("cnt", ascending=False)
        .head(1)[["customer_number"]]
    )
