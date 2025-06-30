from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])

    row_zero = set()
    col_zero = set()

    # first pass
    for row in range(m):
        for col in range(n):
            if matrix[row][col]==0:
                row_zero.add(row)
                col_zero.add(col)
    
    # Set any cell in the matrix to zero if its row index is in row_zero or its column index is in col_zero
    for row in range(m):
        for col in range(n):
            if row in row_zero or col in col_zero:
                matrix[row][col]=0
    

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix)
