import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    nums = logs['num']
    mask = (nums == nums.shift(1)) & (nums == nums.shift(2))
    return pd.DataFrame({'ConsecutiveNums': nums[mask].drop_duplicates()})