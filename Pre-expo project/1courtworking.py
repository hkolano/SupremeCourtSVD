for i in range(len(listOfCourts)):
    court = listOfCourts[i]
    sheet1 = book.add_sheet('Court'+str(i))       # i.e. Court1 because the count starts at 0

    rowJudge = 0
    rowVector = 0
    colVector = 3
    colValue = 2
    for element in court[0]:            # because it's a list containing a list
        rowJudge +=1
        sheet1.write(rowJudge, 0, element)      # write judge names in first col
    vectors = Court1[1:4]
    for row in vectors:
        for element in row:
            rowVector +=1
            sheet1.write(rowVector, colVector, element)      # write matrices into cols
        colVector += 3
        rowVector = 0
    for element in Court1[4]:
        sheet1.write(5, colValue, element)             # write singular values in
        colValue += 3
