import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.merge(employee, on="employee_id")
    result = df.groupby("project_id", as_index=False)["experience_years"].mean()
    result["average_years"] = result["experience_years"].round(2)
    return result[["project_id", "average_years"]]