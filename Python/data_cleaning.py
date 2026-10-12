
# data_cleaning.py

import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "Dataset" / "vehicle_fuel_efficiency_2000.csv"
OUTPUT_FILE = PROJECT_DIR / "Dataset" / "vehicle_fuel_efficiency_2000_cleaned.csv"

def clean_dataset():
    df = pd.read_csv(INPUT_FILE)

    df.columns = df.columns.str.strip()

    column_names = {
        "make": "Manufacturer",
        "model": "Model",
        "year": "Model_Year",
        "VClass": "Vehicle_Class",
        "drive": "Drive_Type",
        "trany": "Transmission",
        "cylinders": "Cylinders",
        "displ": "Engine_Displacement",
        "fuelType1": "Fuel_Type",
        "city08": "City_MPG",
        "highway08": "Highway_MPG",
        "comb08": "Combined_MPG",
        "fuelCost08": "Annual_Fuel_Cost",
        "barrels08": "Petroleum_Consumption",
        "co2TailpipeGpm": "CO2_Emissions",
        "UCity": "Adjusted_City_MPG",
        "UHighway": "Adjusted_Highway_MPG"
    }

    df = df.rename(columns=column_names)

    if "Drive_Type" in df.columns:
        df["Drive_Type"] = df["Drive_Type"].fillna("Unknown")

    for column in ["Cylinders", "Engine_Displacement"]:
        if column in df.columns:
            df[column] = df[column].ffill()

    print("Duplicate rows:", df.duplicated().sum())
    print("Missing values:\n", df.isnull().sum())

    df.to_csv(OUTPUT_FILE, index=False)
    print("Cleaned dataset saved:", OUTPUT_FILE)

if __name__ == "__main__":
    clean_dataset()

