import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('/Users/shyampathak/Downloads/Electric_Vehicle_Population_Data.csv')

# Display the first few rows of the original DataFrame
print("Original DataFrame:")
print(df.head())

# Identifying missing data
print("\nMissing Data (True indicates missing):")
print(df.isna())

# Filtering out missing data (remove rows with any missing values)
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing data:")
print(df_dropped)

# Filling missing data (e.g., with zero)
df_filled = df.fillna(0)
print("\nDataFrame after filling missing data with 0:")
print(df_filled)

# Removing duplicates
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)