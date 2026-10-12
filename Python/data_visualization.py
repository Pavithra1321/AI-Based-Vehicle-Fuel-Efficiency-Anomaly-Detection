
# data_visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "Dataset" / "vehicle_fuel_efficiency_2000_cleaned.csv"
OUTPUT_DIR = PROJECT_DIR / "Visualizations"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE)
sns.set_theme(style="whitegrid")

# 1. Distribution analysis: Combined MPG
plt.figure(figsize=(9, 5))
plt.hist(df["Combined_MPG"].dropna(), bins=30)
plt.title("Distribution of Combined Fuel Efficiency")
plt.xlabel("Combined MPG")
plt.ylabel("Number of Vehicles")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "distribution_analysis.png", dpi=150)
plt.close()

# 2. Trend/relationship analysis: Engine size vs MPG
plt.figure(figsize=(9, 5))
sns.scatterplot(data=df, x="Engine_Displacement", y="Combined_MPG")
plt.title("Engine Size vs Fuel Efficiency")
plt.xlabel("Engine Displacement")
plt.ylabel("Combined MPG")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "trend_analysis.png", dpi=150)
plt.close()

# 3. Category analysis: Average MPG by fuel type
fuel_mpg = df.groupby("Fuel_Type", dropna=False)["Combined_MPG"].mean()
plt.figure(figsize=(10, 5))
fuel_mpg.plot(kind="bar")
plt.title("Average Fuel Efficiency by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Average Combined MPG")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "category_analysis.png", dpi=150)
plt.close()

# 4. Correlation analysis: Numerical variables
numeric_df = df.select_dtypes(include="number")
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), cmap="coolwarm", center=0)
plt.title("Vehicle Data Correlation Analysis")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_analysis.png", dpi=150)
plt.close()

print("All four visualizations saved in:", OUTPUT_DIR)

