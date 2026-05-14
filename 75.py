import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    

    merged = pd.merge(
        employees,
        salaries,
        on="employee_id",
        how="outer"
    )
    

    result = merged[
        merged["name"].isna() | merged["salary"].isna()
    ][["employee_id"]]
    

    result = result.sort_values(by="employee_id")
    
    return result