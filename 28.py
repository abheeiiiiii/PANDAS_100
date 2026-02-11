import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    singles = counts[counts == 1].index

    if len(singles) == 0:
        return pd.DataFrame({'num': [None]})

    return pd.DataFrame({'num': [max(singles)]})
