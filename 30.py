import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat = seat.copy()
    max_id = seat['id'].max()

    seat['id'] = seat['id'].apply(
        lambda x: x + 1 if x % 2 == 1 and x != max_id
        else x - 1 if x % 2 == 0
        else x
    )

    return seat.sort_values('id').reset_index(drop=True)