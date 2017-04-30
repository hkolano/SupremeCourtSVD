import xlwt
from relevant_data import listOfCourts

book = xlwt.Workbook(encoding="utf-8")

for i in range(len(listOfCourts)):
    Court = listOfCourts[i]
    sheet1 = book.add_sheet('Court'+str(i+1))       # i.e. Court1 because the count starts at 0

    rowJudge = 0
    rowVector = 0
    colVector = 3
    colValue = 2
    for element in Court[0]:            # because it's a list containing a list
        rowJudge +=1
        sheet1.write(rowJudge, 0, element)      # write judge names in first col
    vectors = Court[1:4]
    for row in vectors:
        for element in row:
            rowVector +=1
            sheet1.write(rowVector, colVector, element)      # write matrices into cols
        colVector += 3
        rowVector = 0
    for element in Court[4]:
        sheet1.write(5, colValue, element)             # write singular values in
        colValue += 3

'''Desired Format in excel spreadsheet: for each court:
judgenames   |   singularvalue1 * [vector1]   +   singularvalue2 * [vector2]   +   singularvalue3 * [vector3]
'''
# sheet1.write(1, 0, "Dominance")
# sheet1.write(2, 0, "Test")
#
# sheet1.write(0, 1, x)
# sheet1.write(1, 1, y)
# sheet1.write(2, 1, z)
#
# sheet1.write(4, 0, "Stimulus Time")
# sheet1.write(4, 1, "Reaction Time")
#
# i=4
# for n in list1:
#     i = i+1
#     sheet1.write(i, 0, n)

if __name__ == '__main__':
    book.save("Judges and Decisions.xls")
