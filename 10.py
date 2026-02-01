import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on="departmentId", right_on="id", how="inner")
    
    df["rank"] = df.groupby("departmentId")["salary"] \
                    .rank(method="dense", ascending=False)
    
    result = df[df["rank"] <= 3][["name_x", "salary", "name_y"]]
    result.columns = ["Employee", "Salary", "Department"]
    
    return result
