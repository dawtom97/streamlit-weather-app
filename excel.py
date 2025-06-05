import os
import pandas as pd

def save_to_excel(record, path):
    df_new = pd.DataFrame([record])

    # dodawanie nowego rekordu do istniejącego pliku
    if os.path.exists(path):
        df = pd.read_excel(path)
        df = pd.concat(
            [df, df_new],
            ignore_index=False
        )
    else:
        df = df_new

    df.to_excel(path, index=False)