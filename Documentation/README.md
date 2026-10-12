# AI-Based Vehicle Fuel Efficiency Anomaly Detection

## 1. Title Page

**Project Title:** AI-Based Vehicle Fuel Efficiency Anomaly Detection

**Project Domain:** Artificial Intelligence and Machine Learning (AIML)

**Project Type:** Data Analysis and Exploratory Data Analysis (EDA)

**Submitted by:**  S. PAVITHRA

**Course:** Artificial Intelligence and Machine Learning

**Tools Used:** Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook

**Academic Year:** 2026

---

## 2. Abstract

Vehicle fuel efficiency is an important factor in reducing fuel consumption and vehicle operating costs. Different vehicle characteristics, such as manufacturer, engine displacement, cylinder count, fuel type, and vehicle class, can influence fuel efficiency.

This project focuses on analysing vehicle data to understand fuel-efficiency patterns and identify unusual values that may require further investigation. Python libraries such as Pandas, Matplotlib, and Seaborn are used for data cleaning, exploratory data analysis, and visualization.

The analysis includes manufacturer distribution, fuel-type distribution, Combined MPG statistics, engine displacement comparisons, cylinder-based comparisons, and the relationship between fuel efficiency and CO₂ emissions.

The results of this analysis can support further development of an AI-based anomaly-detection system. The current project work focuses on data preparation and EDA; a trained anomaly-detection model would be a separate next step.

---

## 3. Introduction

Fuel efficiency describes how effectively a vehicle uses fuel to travel a distance. Vehicles with higher miles per gallon (MPG) generally travel farther using the same amount of fuel.

Fuel efficiency can vary depending on engine size, number of cylinders, fuel type, vehicle class, transmission, and other characteristics.

Analysing vehicle data helps us understand these differences and identify values that are unusual compared with other records.

This project uses Python-based data analysis and visualization to explore vehicle fuel efficiency and prepare the data for possible anomaly detection.

---

## 4. Problem Statement

Vehicle datasets contain information about different vehicles and their fuel-efficiency measurements. Understanding this information manually can be difficult when there are many records and multiple variables.

Unusually high or low fuel-efficiency values may indicate special vehicle characteristics, data-quality issues, or records that need additional investigation.

Therefore, this project aims to analyse vehicle fuel-efficiency data, understand relationships between vehicle characteristics, and identify potentially unusual observations through exploratory analysis.

An unusual value does not automatically indicate a faulty vehicle. Further investigation is required to understand its cause.

---

## 5. Objectives

The main objectives of this project are:

1. To understand the vehicle fuel-efficiency dataset.
2. To clean the dataset and prepare it for analysis.
3. To analyse fuel efficiency using statistical summaries.
4. To visualize manufacturer, fuel-type, and vehicle-class distributions.
5. To examine the relationship between engine displacement, cylinders, Combined MPG, and CO₂ emissions.
6. To identify potential outliers that require further investigation.
7. To prepare the dataset and findings for future AI-based anomaly detection.

---

## 6. Dataset Description

The project uses a vehicle fuel-efficiency dataset containing information about vehicle characteristics, fuel economy, fuel type, and emissions.

The dataset includes variables such as:

| Column | Description |
|---|---|
| Manufacturer | Name of the vehicle manufacturer |
| Model | Vehicle model name |
| Model_Year | Model year of the vehicle |
| Vehicle_Class | Category of the vehicle |
| Drive_Type | Vehicle drive configuration |
| Transmission | Type of transmission |
| Cylinders | Number of engine cylinders |
| Engine_Displacement | Measure of engine size |
| Fuel_Type | Fuel category |
| City_MPG | Fuel efficiency in city driving |
| Highway_MPG | Fuel efficiency in highway driving |
| Combined_MPG | Combined fuel-efficiency measurement |
| Annual_Fuel_Cost | Estimated annual fuel cost |
| Petroleum_Consumption | Petroleum consumption estimate |
| CO2_Emissions | Tailpipe CO₂ emissions measurement |
| Adjusted_City_MPG | Adjusted city fuel-efficiency measurement |
| Adjusted_Highway_MPG | Adjusted highway fuel-efficiency measurement |

**Dataset source:**  California Open Data — Vehicle Fuel Economy
**Number of records analysed:**  2000 rows
**Number of columns analysed:**   17 columns
The exact record and column counts should be taken from the final dataset used in the notebook.

---

## 7. Tools and Technologies

### Python
Python is the programming language used to perform data analysis and visualization.

### Pandas
Pandas is used to load CSV data, inspect records, rename columns, handle missing values, and calculate summary statistics.

### Matplotlib
Matplotlib is used to create graphs and customize chart titles, labels, and figure sizes.

### Seaborn
Seaborn is used to create statistical visualizations such as scatter plots, boxplots, and heatmaps.

### Jupyter Notebook
Jupyter Notebook provides an interactive environment to execute Python code, display results, and document the analysis.

### GitHub
GitHub is used to store and organize the project files, dataset, notebook, Python scripts if applicable, and visualization images.

---

## 8. Data Cleaning and Preparation

Data cleaning is an important step before performing exploratory data analysis.

The following activities were part of the project's data-preparation workflow:

1. **Loading the dataset:** The vehicle dataset was loaded into Python for analysis.
2. **Inspecting the data:** Rows, columns, data types, and sample records were examined.
3. **Renaming columns:** Column names were changed to clearer names, such as `Manufacturer`, `Vehicle_Class`, `Engine_Displacement`, and `Combined_MPG`.
4. **Checking duplicates:** Duplicate records were checked to understand whether repeated rows existed.
5. **Checking missing values:** Missing values were inspected to determine which columns required attention.
6. **Checking categories:** Manufacturer names and other categorical values were reviewed for inconsistent spellings or formats.
7. **Preparing data for EDA:** The dataset was organized so that the variables could be analysed and visualized more easily.

Only the cleaning operations actually performed should be described as completed. Any additional missing-value treatment, duplicate removal, or category correction should be included only if it was carried out in the notebook.

---

## 9. Exploratory Data Analysis and Visualization

Exploratory Data Analysis (EDA) helps us understand the dataset through statistics, graphs, and comparisons.

### 9.1 Manufacturer Analysis

A bar chart was used to examine the distribution of vehicle manufacturers.

It helps identify which manufacturers appear most frequently in the dataset. This describes the dataset's composition, not the total number of vehicles produced by each manufacturer in the real world.

### 9.2 Fuel-Type Distribution

A bar chart was used to compare the number of records across fuel types.

This helps us understand which fuel categories are represented in the dataset and prepares us for comparisons of fuel efficiency across fuel types.

### 9.3 Combined MPG Distribution

A histogram was used to examine the distribution of Combined MPG values.

The graph helps show where fuel-efficiency values are concentrated and whether some values occur much less frequently than others.

### 9.4 Combined MPG Statistical Summary

Minimum, maximum, mean, and median values were calculated for Combined MPG.

These statistics summarize the range and typical fuel efficiency of the vehicles in the dataset. The mean and median can also be compared to understand whether extreme values may influence the average.

### 9.5 Combined MPG Boxplot

A boxplot was used to summarize the distribution of Combined MPG and flag potential outliers.

Values outside the boxplot's usual range are observations for further investigation. They should not automatically be treated as errors or faulty vehicles.

### 9.6 Engine Displacement vs Combined MPG

A scatter plot was used to examine the relationship between engine displacement and Combined MPG.

It helps us investigate whether vehicles with different engine sizes show different fuel-efficiency patterns and whether some records differ from the general pattern.

### 9.7 Cylinders vs Combined MPG

A boxplot was used to compare fuel-efficiency distributions across different cylinder counts.

This helps examine differences in typical MPG and the variation in fuel efficiency among vehicles with different engine configurations.

### 9.8 Vehicle Class vs Combined MPG

A boxplot was used to compare Combined MPG across vehicle classes.

This is useful because fuel-efficiency expectations may differ between vehicle categories. An unusual value should be interpreted in the context of similar vehicles when possible.

### 9.9 Fuel Type vs Combined MPG

A bar chart was used to compare average Combined MPG across fuel types.

It provides a summary of fuel efficiency by category. The average does not describe every vehicle in a category, and comparisons may be affected by other vehicle characteristics.

### 9.10 Combined MPG vs CO₂ Emissions

A scatter plot was used to examine the relationship between fuel efficiency and tailpipe CO₂ emissions.

This helps us explore whether higher fuel efficiency is associated with lower CO₂ emissions per mile in the dataset and identify records that may require additional investigation.

### 9.11 Correlation Analysis

A correlation heatmap can be used to summarize relationships between numerical variables.

Positive correlation indicates that two variables tend to increase together, while negative correlation indicates that one tends to decrease as the other increases. Correlation does not prove causation.

### Overall EDA Findings

The visualizations provide a clearer understanding of fuel-efficiency distributions, vehicle categories, engine characteristics, and emissions relationships.

The actual findings—such as which category has the highest average MPG, the observed correlation values, and the number of potential outliers—should be added after reviewing the results displayed by the notebook.

---

## 10. Conclusion and Future Scope

### Conclusion

The project demonstrates how Python can be used to analyse vehicle fuel-efficiency data through data preparation, statistical summaries, and visualization.

The EDA examines manufacturer and fuel-type distributions, Combined MPG values, engine characteristics, vehicle classes, and CO₂ emissions. These analyses help us understand patterns in the dataset and flag unusual observations for further investigation.

The completed data-analysis work provides a foundation for developing an AI-based anomaly-detection system.

### Future Scope

The project can be extended in the following ways:

1. Apply a suitable anomaly-detection algorithm, such as Isolation Forest, to identify potentially unusual records.
2. Evaluate the model using appropriate validation methods and domain knowledge.
3. Investigate whether unusual values are caused by data-quality issues or legitimate vehicle differences.
4. Develop visual reports or a simple dashboard to present the findings.
5. Explore additional vehicle data to test whether the analysis generalizes to other datasets.

The current project focuses on data analysis and EDA. The future AI model should be implemented and evaluated before claiming automated anomaly detection.

---

## References

1. The original vehicle fuel-efficiency dataset source: [Insert the exact source URL.]
2. Pandas documentation: https://pandas.pydata.org/docs/
3. Matplotlib documentation: https://matplotlib.org/stable/
4. Seaborn documentation: https://seaborn.pydata.org/
5. Jupyter documentation: https://docs.jupyter.org/
