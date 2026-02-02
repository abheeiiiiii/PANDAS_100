import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values("recordDate")
    prev = weather.shift(1)

    return weather[
        (weather["temperature"] > prev["temperature"]) &
        ((weather["recordDate"] - prev["recordDate"]).dt.days == 1)
    ][["id"]]