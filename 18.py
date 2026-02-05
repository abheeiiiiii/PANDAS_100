import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee.groupby("managerId").size().reset_index(name="cnt")
    managers = counts[counts["cnt"] >= 5]["managerId"]
    return employee[employee["id"].isin(managers)][["name"]]
