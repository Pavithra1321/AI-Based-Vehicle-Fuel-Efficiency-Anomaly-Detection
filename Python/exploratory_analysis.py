
# exploratory_analysis.py

import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "Dataset" / "vehicle_fuel_efficiency_2000_cleaned.csv"

def explore_dataset():
    df = pd.read_csv(DATA_FILE)

    print("Dataset shape:", df.shape)
    print("\nDataset information:")
    df.info()

    print("\nSummary statistics:")
    print(df.describe())

    print("\nTop 10 manufacturers:")
    print(df["Manufacturer"].value_counts().head(10))

    print("\nFuel type distribution:")
    print(df["Fuel_Type"].value_counts())

    print("\nCombined MPG statistics:")
    print(df["Combined_MPG"].agg(
        ["min", "max", "mean", "median"]
    ))

    print("\nCorrelation between numerical columns:")
    print(df.select_dtypes(include="number").corr())

if __name__ == "__main__":
    explore_dataset()

