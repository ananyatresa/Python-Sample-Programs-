import xlrd
from xlrd import open_workbook
file_location="D:\ANANYA\programming languages\Python lang\sample programs\sample.xls"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
data=[[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
print (data)
