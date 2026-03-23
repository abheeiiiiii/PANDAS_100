import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    no_trans = visits[~visits['visit_id'].isin(transactions['visit_id'])]
    result = (
        no_trans.groupby('customer_id')
        .size()
        .reset_index(name='count_no_trans')
    )

    return result