'''Writes a list of lists of lists to a list of matrices.'''

from numpy import matrix
from numpy import linalg


def listToMatrix(listOfLists):
    listOfMatrices = []
    for item in listOfLists:
        m = matrix(item)
        listOfMatrices.append(m)
    for item in listOfMatrices:
        print(matrix)

if __name__ == '__main__':
    A = [[[1,2,3],[4,5,6],[7,8,9]],
         [[11,12,13],[14,15,16],[17,18,19]],
         [[21,22,23],[24,25,26],[27,28,29]]]
    listToMatrix(A)
