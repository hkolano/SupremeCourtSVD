from pyexcel_ods import get_data
import pyexcel as pe
import json

data = get_data("consolidated_data.ods", start_row=1, start_column=2, column_limit=3)
data = data["Sheet1"]

cases = []
judges = []
first_case = data[0:9]

for row in first_case:
    # initializes judge indexes
    judges.append(row[2])

new_sheet = [[0]*int(len(data)/9+1) for i in range(9)]
one_court = []

counter = 0
case_in_court_count = 0
for row in data:
    case, leaning, judge = row[0], row[1], row[2]
    # if the judge is new, find the index of the last case without him/her
    if judge not in judges:
        n = 1
        prev_case = data[counter-n][0]
        while prev_case == case:
            n += 1
            prev_case = data[counter-n][0]
        new_case_row_index = counter-n+1
        # reset all the variables
        print(case_in_court_count/9)
        for n in range(9):
            new_sheet[n] = new_sheet[n][:int(case_in_court_count/9)]
        one_court.append(new_sheet)
        new_sheet = [[0]*int(len(data)/9+1) for i in range(9)]
        cases = []
        # reset the judges
        new_first_case = data[new_case_row_index:new_case_row_index+9]
        # print(new_first_case)
        judges = []
        for row in new_first_case:
            judges.append(row[2])
        case_in_court_count = 0
    # change all the 2's to -1's
    if leaning == '':
        leaning = 0
    if leaning == 2:
        leaning = -1
    # if it's a new case, add to the case dict and give a number to the case
    if case not in cases:
        cases.append(case)
    # now add to the matrix!
    new_sheet[judges.index(judge)][cases.index(case)] = leaning

    counter += 1
    case_in_court_count += 1
    row[0], row[1], row[2] = case, leaning, judge

for n in range(9):
    new_sheet[n] = new_sheet[n][:int(case_in_court_count/9)]
one_court.append(new_sheet)
print(one_court)
