import pandas as pd

# Load the dataset
file_path = '/Users/shyampathak/Downloads/Electric_Vehicle_Population_Data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("Original DataFrame:")
print(df.head())

# Inspect the column names
print("Columns in the DataFrame:")
print(df.columns)

# Assuming 'Make', 'Model Year', and 'Electric Range' are suitable columns for hierarchical indexing
# Create a hierarchical index from 'Make' and 'Model Year' columns
hier_index = pd.MultiIndex.from_frame(df[['Make', 'Model Year']])

# Create a Series using the hierarchical index and 'Electric Range' column
series = pd.Series(df['Electric Range'].values, index=hier_index)

# Display the Series with hierarchical index
print("\nSeries with Hierarchical Index:")
print(series)

# Selecting subsets of data at the outer level (Make)
print("\nData for Tesla:")
print(series['TESLA'])

print("\nData for Nissan:")
print(series['NISSAN'])

# Selecting subsets of data at the inner level (Model Year) within an outer level
print("\nData for Tesla, Model Year 2020:")
print(series['TESLA', 2020])

print("\nData for Nissan, Model Year 2018:")
print(series['NISSAN', 2018])