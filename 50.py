import pandas as pd

def february_sales(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    feb = orders[(orders['order_date'] >= '2020-02-01') & (orders['order_date'] <= '2020-02-29')]
    total = feb.groupby('product_id', as_index=False)['unit'].sum()
    total = total[total['unit'] >= 100]
    res = total.merge(products, on='product_id')
    return res[['product_name', 'unit']]