import pandas as pd
from decimal import Decimal, ROUND_HALF_UP

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries["ratio"] = queries["rating"] / queries["position"]

    result = queries.groupby("query_name").agg(
        quality=("ratio", "mean"),
        poor_query_percentage=("rating", lambda x: (x.lt(3).sum() / len(x)) * 100)
    ).reset_index()

    # Proper rounding (ROUND_HALF_UP)
    result["quality"] = result["quality"].apply(
        lambda x: float(Decimal(str(x)).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP))
    )

    result["poor_query_percentage"] = result["poor_query_percentage"].apply(
        lambda x: float(Decimal(str(x)).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP))
    )

    return result