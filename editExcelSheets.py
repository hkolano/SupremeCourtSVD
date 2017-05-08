from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy

rb = open_workbook("SingularValuesByYear.xls")
wb = copy(rb)

s = wb.get_sheet(0)
s.write(8,8,'A1')
wb.save('SingularValuesByYear.xls')
