import pandas as pd
import numpy as np

def average_selling_price(prices: pd.DataFrame, unitsSold: pd.DataFrame) -> pd.DataFrame:
    df = prices.merge(unitsSold, on="product_id", how="left")
    df = df[(df["purchase_date"].between(df["start_date"], df["end_date"])) | df["purchase_date"].isna()]
    df["revenue"] = df["price"] * df["units"]
    result = df.groupby("product_id", as_index=False).agg({"revenue": "sum", "units": "sum"})
    result[["revenue", "units"]] = result[["revenue", "units"]].fillna(0)
    result["average_price"] = np.where(result["units"] == 0, 0, (result["revenue"] / result["units"]).round(2))
    return result[["product_id", "average_price"]]