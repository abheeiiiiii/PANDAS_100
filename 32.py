import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    total_products = product['product_key'].nunique()
    
    result = (
        customer.groupby('customer_id')['product_key']
        .nunique()
        .reset_index()
    )
    
    return result[result['product_key'] == total_products][['customer_id']]