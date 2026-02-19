import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    target_date = pd.to_datetime("2019-08-16")
    products["change_date"] = pd.to_datetime(products["change_date"])
    
    filtered = products[products["change_date"] <= target_date]
    
    latest = filtered.sort_values("change_date").groupby("product_id").tail(1)
    
    result = latest[["product_id", "new_price"]].rename(columns={"new_price": "price"})
    
    all_products = pd.DataFrame({"product_id": products["product_id"].unique()})
    
    result = all_products.merge(result, on="product_id", how="left")
    result["price"] = result["price"].fillna(10)
    
    return result
