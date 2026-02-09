import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium = stadium.sort_values("id").reset_index(drop=True)
    result_indices = []
    n = len(stadium)
    i = 0
    while i < n:
        if stadium.loc[i, "people"] >= 100:
            start = i
            while i < n and stadium.loc[i, "people"] >= 100:
                i += 1
            end = i
            if end - start >= 3:
                result_indices.extend(range(start, end))
        else:
            i += 1
    return stadium.loc[result_indices, ["id", "visit_date", "people"]]
