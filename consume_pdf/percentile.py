import pandas as pd
import glob

# Step 1: Get all CSV file names
csv_files = glob.glob("page-*_table-*.csv")

# Step 2: Load all CSVs into a single DataFrame
df_list = [pd.read_csv(file) for file in csv_files]
df = pd.concat(df_list, ignore_index=True)

print(df)

# Step 3: Convert "Marks" column to numeric (replace with your actual column name)
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Step 4: Calculate percentile for the "Marks" column
df["Marks Percentile"] = df["Marks"].rank(pct=True) * 100

df = df.sort_values(by="Marks Percentile", ascending=False)

# Step 5: Save the final DataFrame to a CSV file
df.to_csv("final_accumulated_data.csv", index=False)

# Display the first few rows
print(df.head())
