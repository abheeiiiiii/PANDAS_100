import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.drop_duplicates()
    
    result = (df.groupby('sell_date')['product']
                .agg(lambda x: sorted(x))
                .reset_index())
    
    result['num_sold'] = result['product'].apply(len)
    result['products'] = result['product'].apply(lambda x: ','.join(x))
    
    return result[['sell_date', 'num_sold', 'products']].sort_values('sell_date')