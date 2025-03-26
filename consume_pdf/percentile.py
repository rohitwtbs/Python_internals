import pdfplumber
import pandas as pd
import numpy as np

# Open the PDF file
# pdf_path = "result.pdf"

# tables = []
# with pdfplumber.open(pdf_path) as pdf:
#     for page in pdf.pages:
#         table = page.extract_table()  # Extract table from page
#         if table:
#             tables.extend(table)  # Append extracted rows

# # Convert to DataFrame
# df = pd.DataFrame(tables)

# print(df)

# # Optionally, set the first row as column names if needed
# df.columns = df.iloc[0]
# df = df[1:].reset_index(drop=True)

# # Convert numeric columns (assuming a column "Score")
# df["Score"] = pd.to_numeric(df["Score"], errors="coerce")

# # Calculate the percentile of "Score"
# df["Score Percentile"] = df["Score"].rank(pct=True) * 100

# print(df)


import camelot

pdf_path = "your_file.pdf"
tables = camelot.read_pdf(pdf_path, pages="all")

# Convert first table into Pandas DataFrame
df = tables[0].df

# Rename columns if necessary
df.columns = ["ID", "Name", "Score"]  # Example column names

# Convert to numeric where necessary
df["Score"] = pd.to_numeric(df["Score"], errors="coerce")

# Compute percentile
df["Score Percentile"] = df["Score"].rank(pct=True) * 100

print(df)
