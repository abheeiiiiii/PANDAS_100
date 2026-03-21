import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['price'] = stocks['price'] * stocks['operation'].map({'Buy': -1, 'Sell': 1})
    return stocks.groupby('stock_name', as_index=False)['price'].sum() \
                 .rename(columns={'price': 'capital_gain_loss'})
