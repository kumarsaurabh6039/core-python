from openpyxl import Workbook

# Create a new excel workbook
workbook = Workbook()

# Select the default sheet
sheet = workbook.active

# Rename the sheet
sheet.title = "Examplesheet"

# Data set (column-wise)
data = {
    "A": ["Name", "john doe", "jane smith", "emily johnson"],
    "B": ["Age", 30, 25, 18],
    "C": ["Salary", 5000, 6000, 1300],
}

# Add column-wise data
for col, values in data.items():
    for row, value in enumerate(values, start=1):
        sheet[f"{col}{row}"] = value

# Save the workbook
workbook.save("Examplesheet.xlsx")
