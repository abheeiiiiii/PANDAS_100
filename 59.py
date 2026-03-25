import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    balances = transactions.groupby('account', as_index=False)['amount'].sum()
    merged = users.merge(balances, on='account', how='left')
    merged['amount'] = merged['amount'].fillna(0)
    result = merged[merged['amount'] > 10000][['name', 'amount']]
    result = result.rename(columns={'amount': 'balance'})
    return result