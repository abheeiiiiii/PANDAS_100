import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    m1 = insurance["tiv_2015"].duplicated(keep=False)
    m2 = insurance.duplicated(subset=["lat", "lon"], keep=False)

    return pd.DataFrame({
        "tiv_2016": [round(insurance[m1 & ~m2]["tiv_2016"].sum(), 2)]
    })
