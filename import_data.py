from pyexcel_ods import get_data
import pyexcel as pe
import json

data = get_data("consolidated_data.ods", start_row=1, row_limit=100, start_column=2, column_limit=3)
data = data["Sheet1"]

cases = []
judges = []
first_case = data[0:8]

for row in first_case:
    # initializes judge indexes
    judges.append(row[1])

counter = 0
for row in data:
    if row[1] not in judges:
        case_w_new_judge = row[0]
        index_of_that = counter
        counter += 1

new_sheet = [[0]*int(index_of_that/9) for i in range(9)]

for row in data:
    case, leaning, judge = row[0], row[1], row[2]
    # change all the 2's to -1's
    if leaning == 2:
        leaning = -1
    # if it's a new case, add to the case dict and give a number to the case
    if case not in cases:
        cases.append(case)
    # now add to the matrix!
    new_sheet[judges.index(judge)][cases.index(case)] = leaning

    row[0], row[1], row[2] = case, leaning, judge

print(new_sheet)
