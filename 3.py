import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col_name = f"getNthHighestSalary({N})"
    
    # Handle invalid N
    if N <= 0:
        return pd.DataFrame({col_name: [None]})
    
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    if len(salaries) < N:
        return pd.DataFrame({col_name: [None]})
    
    return pd.DataFrame({col_name: [salaries.iloc[N - 1]]})
