import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    
    
    daily = customer.groupby("visited_on", as_index=False)["amount"].sum()
    
   
    daily = daily.sort_values("visited_on")
    
    
    daily["amount"] = daily["amount"].rolling(7).sum()
    

    daily["average_amount"] = (daily["amount"] / 7).round(2)
    
    result = daily.dropna()
    
    return result