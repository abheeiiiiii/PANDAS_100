import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return (
        person.groupby("email", as_index=False)
        .filter(lambda x: len(x) > 1)[["email"]]
        .drop_duplicates()
    )