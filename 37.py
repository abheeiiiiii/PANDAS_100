import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales["sale_date"] = pd.to_datetime(sales["sale_date"])
    
    q1 = sales[(sales["sale_date"] >= "2019-01-01") & (sales["sale_date"] <= "2019-03-31")]
    other = sales[(sales["sale_date"] < "2019-01-01") | (sales["sale_date"] > "2019-03-31")]
    
    valid_products = set(q1["product_id"]) - set(other["product_id"])
    
    result = product[product["product_id"].isin(valid_products)]
    return result[["product_id", "product_name"]]
