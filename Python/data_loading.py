
# data_loading.py

import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "Dataset" / "vehicle_fuel_efficiency_2000.csv"

def load_dataset():
    df = pd.read_csv(DATA_FILE)
    print("Dataset loaded successfully!")
    print("Rows and columns:", df.shape)
    print(df.head())
    return df

if __name__ == "__main__":
    df = load_dataset()

