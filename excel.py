import os
import pandas as pd

def save_to_excel(record):
    df_new = pd.DataFrame([record])

    # dodawanie nowego rekordu do istniejącego pliku
    if os.path.exists("weather.xlsx"):
        df = pd.read_excel("weather.xlsx")
        df = pd.concat(
            [df, df_new],
            ignore_index=False
        )
    else:
        df = df_new

    df.to_excel("weather.xlsx", index=False)