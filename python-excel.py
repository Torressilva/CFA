from mmap import mmap, ACCESS_READ
from xlrd import open_workbook, xldate_as_tuple, cellname
from datetime import date, datetime, time

#
# Open
#
print open_workbook('simple.xls')
with open('simple.xls','rb') as f:
	print open_workbook(
		file_contents=mmap(f.fileno(),0,access=ACCESS_READ)
		)
	aString = open('simple.xls','rb').read()
	print open_workbook(file_contents=aString)
#
# Navigate
#
wb = open_workbook('simple.xls')
for s in wb.sheets():
	print 'Sheet:',s.name
	for row in range(s.nrows):
		values = []
		for col in range(s.ncols):
			values.append(s.cell(row,col).value)
			print ','.join(values)
			print
#
# Sheets
#
book = open_workbook('simple.xls')
print book.nsheets
for sheet_index in range(book.nsheets):
	print book.sheet_by_index(sheet_index)
	print book.sheet_names()
	for sheet_name in book.sheet_names():
		print book.sheet_by_name(sheet_name)
		for sheet in book.sheets():
			print sheet
#
# Introspect sheet
#
book = open_workbook('odd.xls')
sheet = book.sheet_by_index(0)
print sheet.name
print sheet.nrows
print sheet.ncols
for row_index in range(sheet.nrows):
	for col_index in range(sheet.ncols):
		print cellname(row_index,col_index),'-',
		print sheet.cell(row_index,col_index).value
#
# Dates
#
book = open_workbook('types.xls')
sheet = book.sheet_by_index(0)
date_value =
xldate_as_tuple(sheet.cell(3,2).value,book.datemode)
print datetime(*date_value),date(*date_value[:3])
datetime_value =
xldate_as_tuple(sheet.cell(3,3).value,book.datemode)
print datetime(*datetime_value)
time_value =
xldate_as_tuple(sheet.cell(3,4).value,book.datemode)
print time(*time_value[3:])
print datetime(*time_value)
