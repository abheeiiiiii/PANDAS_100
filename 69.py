import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    primary = employee[employee["primary_flag"] == "Y"][["employee_id", "department_id"]]
    
    single = employee.groupby("employee_id").filter(lambda x: len(x) == 1)[["employee_id", "department_id"]]
    
    result = pd.concat([primary, single])
    
    return result.reset_index(drop=True)