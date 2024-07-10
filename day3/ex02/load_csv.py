import pandas as pd
from pandas import DataFrame


def load(path:str) -> DataFrame:
    try:
        df = pd.read_csv(path)
    except Exception:
        print("wrong csv path")
        return(None)
    print(f"Loading dataset of dimensions ({df.shape[0]}, {df.shape[1]})")
    return df
