'''
Hannah Kolano and Gracey Wilson
Supreme Court SVD Exploration
Linearity 1 Final Project
Spring 2017

Creates a spreadsheet containing the singular value decomposition of the
decisions of Supreme Court justices from 1946 - 2010 (on a liberal to
conservative axis).
INPUT: Data from a python file in the form of a list of list of lists
      (in this case, listOfCourts from relevant_data.py)
OUTPUT: An excel spreadsheet where each sheet shows the data of one "court"'s
decisions in the format:
judgenames   |   singularvalue1 * [vector1]   +   singularvalue2 * [vector2]   +   singularvalue3 * [vector3]
'''

import xlwt
from judgesAndValues import courtValues

book = xlwt.Workbook(encoding="utf-8")

for i in range(len(courtValues)):
    Court = courtValues[i]
    sheet1 = book.add_sheet('Court'+str(i+1))       # i.e. Court1 because the count starts at 0

    rowJudge = 0
    rowValue = 0
    for element in Court[0]:            # because it's a list containing a list
        rowJudge +=1
        sheet1.write(rowJudge, 0, element)      # write judge names in first col

    for element in Court[1]:
        rowValue +=1
        sheet1.write(rowValue, 2, element)            # write singular values into cols

if __name__ == '__main__':
    book.save("Judges & Singular Values.xls")
