'''
Imports supreme justice data since 1946 and turns into list of matrices with
judges on the y-axis and caes on the x-axis. A new matrix occurs when the court
changes.

Author: Hannah Kolano and Gracey Wilson
April 2017
hannah.kolano@students.olin.edu
'''
# import the needed libraries
from pyexcel_ods import get_data
import pyexcel as pe
import json

# get data from the spreadsheet
data = get_data("consolidated_data.ods", start_row=1, start_column=2, column_limit=3)
data = data["Sheet1"]

# initializes list of cases, list of justices, the first case, and the list to return
cases = []
judges = []
first_case = data[0:9]
court_matrix = []
case_info = []
case_indexes = []

# initializes judge list for the first case
for row in first_case:
    judges.append(row[2])

# creates the first matrix, of zeroes initially
new_sheet = [[0]*int(len(data)/9+1) for i in range(9)]

# some important counters
old_num_justices = 9
counter = 0
case_in_court_count = 0

# for row in data:
#     case = row[0]
#     if case not in cases:
#         cases.append(case)
#         case_indexes.append(cases.index(case))
#     counter += 1

cases = []

# parses spreadsheet row by row
# each row is a judge, rotating in intervals of 8/9
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
        n = 1
        num_justices = 0
        this_case = data[new_case_row_index][0]
        while this_case == case:
            num_justices += 1
            this_case = data[new_case_row_index+n][0]
            n += 1
        # reset all the variables
        for n in range(old_num_justices):
            new_sheet[n] = new_sheet[n][:int(case_in_court_count/old_num_justices)]
        court_matrix.append(new_sheet)
        new_sheet = [[0]*int(len(data)/num_justices+1) for i in range(num_justices)]
        cases = []
        # reset the judges
        new_first_case = data[new_case_row_index:new_case_row_index+num_justices]
        # print(new_first_case)
        judges = []
        for row in new_first_case:
            judges.append(row[2])
        case_in_court_count = 0
        old_num_justices = num_justices
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

for n in range(num_justices):
    new_sheet[n] = new_sheet[n][:int(case_in_court_count/num_justices)]
court_matrix.append(new_sheet)
print(court_matrix)
