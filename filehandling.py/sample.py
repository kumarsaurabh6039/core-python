from openpyxl import Workbook

#create a new excel workbook
workbook = Workbook()

#select the default sheet
sheet = workbook.active

#rename the sheet
sheet.title = "Examplesheet"

#data set
sheet["A1"] = "Name"
sheet["b1"] = "age"
sheet["c1"] = "salary"

#add row of data
data= [
    ["john doe",30,5000],
    ["jane smith",25,6000],
    ["emily johnson",18,1300],
]
for row in data:
    sheet.append(row)
workbook.save("Examplesheet.xlsx")
