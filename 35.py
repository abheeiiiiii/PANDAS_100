import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    first_year = sales.groupby("product_id")["year"].min().reset_index(name="first_year")
    result = sales.merge(first_year, on="product_id")
    result = result[result["year"] == result["first_year"]]
    return result[["product_id", "first_year", "quantity", "price"]]