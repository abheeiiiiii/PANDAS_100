import pandas as pd
import numpy as np

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        employees
        .dropna(subset=["reports_to"])
        .groupby("reports_to")
        .agg(reports_count=("employee_id", "count"),
             average_age=("age", "mean"))
        .reset_index()
    )
    
    grouped["average_age"] = np.floor(grouped["average_age"] + 0.5).astype(int)
    
    result = grouped.merge(
        employees[["employee_id", "name"]],
        left_on="reports_to",
        right_on="employee_id"
    )
    
    result = result[["employee_id", "name", "reports_count", "average_age"]]
    return result.sort_values("employee_id")