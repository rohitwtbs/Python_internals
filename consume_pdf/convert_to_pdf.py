import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate

# Step 1: Read the sorted CSV
df = pd.read_csv("final_accumulated_data.csv")

# Step 2: Convert DataFrame to a List of Lists (for Table)
data = [df.columns.tolist()] + df.values.tolist()  # Include headers

# Step 3: Define PDF file path
pdf_path = "sorted_percentile_data.pdf"

# Step 4: Create PDF document
pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
table = Table(data)

# Step 5: Style the Table
style = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # Header background
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center align
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),  # Bold header
    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),  # Table background
    ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Table grid
])

table.setStyle(style)

# Step 6: Build the PDF
pdf.build([table])

print(f"PDF saved successfully as {pdf_path}")
