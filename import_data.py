'''
Hannah Kolano and Gracey Wilson
Supreme Court SVD Exploration
Linearity 1 Final Project
Spring 2017

Imports supreme justice data since 1946 and turns into list of matrices with
judges on the y-axis and caes on the x-axis. A new matrix occurs when the court
changes.
'''

# import the needed libraries
from pyexcel_ods import get_data
from numpy import matrix, linalg
import numpy as np


def process_data():
    # get data from the spreadsheet
    data = get_data("consolidated_data.ods", start_row=1, start_column=2, column_limit=4)
    data = data["Sheet1"]

    # initializes list of cases, list of justices, the first case, and the list to return
    cases = []
    judges = []
    first_case = data[0:9]
    court_matrix = []
    case_indexes = []
    svd_data = []

    # initializes judge list for the first case
    for row in first_case:
        judges.append(row[2])

    # creates the first matrix, of zeroes initially
    new_sheet = [[0]*int(len(data)/9+1) for i in range(9)]
    for judge in judges:
        new_sheet[judges.index(judge)][0] = judge

    # some important counters
    counter = 0
    case_in_court_count = 0
    curr_year = first_case[0][3]

    # parses spreadsheet row by row
    # each row is a judge, rotating in intervals of 8/9
    for row in data:
        case, leaning, judge, year = row[0], row[1], row[2], row[3]

        # if the judge is new...
        if judge not in judges or year != curr_year:
            n = 1
            prev_case = data[counter-n][0]
            # check where the case with a different court started
            while prev_case == case:
                n += 1
                prev_case = data[counter-n][0]
            new_case_row_index = counter-n+1
            # get the zeroes off the end of each justices decisions
            for n in range(9):
                new_sheet[n] = new_sheet[n][:int(case_in_court_count/9)]
            # finish this sheet and make a new one
            court_matrix.append((new_sheet, curr_year))
            new_sheet = [[0]*int(len(data)/9+1) for i in range(9)]
            cases = []
            # reset the judges
            new_first_case = data[new_case_row_index:new_case_row_index+9]
            judges = []
            for row in new_first_case:
                judges.append(row[2])
            for judge in judges:
                new_sheet[judges.index(judge)][0] = judge
            case_in_court_count = 0
            curr_year = year
        # change all the 2's to -1's
        if leaning == '':
            leaning = 0
        if leaning == 2:
            leaning = -1
        # if it's a new case, add to the case list
        if case not in cases:
            cases.append(case)
        # insert the decision into the proper cell in the sheet
        new_sheet[judges.index(judge)][cases.index(case)+1] = leaning

        counter += 1
        case_in_court_count += 1
        row[0], row[1], row[2], row[3] = case, leaning, judge, year

    for n in range(9):
        new_sheet[n] = new_sheet[n][:int(case_in_court_count/9)]

    court_matrix.append((new_sheet, year))

    for mat_yr in court_matrix:
        matrix, year = mat_yr[0], mat_yr[1]
        if np.array(matrix).size == 9:
            pass
        else:
            these_judges = []
            for n in range(9):
                # print(matrix[n])
                if len(matrix[n]) > 1:
                    these_judges.append(matrix[n][0])
                    matrix[n] = matrix[n][1:]
            try:
                u, s, v = np.linalg.svd(matrix)
                singvals = s.tolist()
                j_sing_yr = [these_judges, singvals, year]
                svd_data.append(j_sing_yr)
            except np.linalg.linalg.LinAlgError as err:
                pass
    return svd_data


# def listToMatrix(listOfLists):
#     '''Writes a list of lists of lists to a list of matrices.'''
#     listOfMatrices = []
#     for item in listOfLists:
#         m = matrix(item)
#         listOfMatrices.append(m)
#     for item in listOfMatrices:
#         print(item)

if __name__ == '__main__':
    a = process_data()
    for year in a:
        print(year[0])
        print(year[1])
        print(year[2])
