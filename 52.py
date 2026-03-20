import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employeeUNI: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employeeUNI, on='id', how='left')
    return df[['unique_id', 'name']]