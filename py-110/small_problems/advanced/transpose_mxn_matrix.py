"""
Matrix transposes are not limited to 3x3 matrices, or even square matrices. Any matrix can be transposed simply 
by switching columns with rows.

Modify your transpose function from the previous exercise so that it works with any MxN matrix with at least one 
row and one column.

P:
Given a list of lists representing an MxN matrix, return the transpose of the matrix.

Rules:
    - A transpose is a matrix that switches the rows and columns of an input matrix
    - Our input matrix will consist of M nested lists, each with N elements
    - The output will consist of N nested lists, each with M elements
    - Do not modify the original matrix

E:
    1 5 8 9    1 4 3
    4 7 2 8 => 5 7 9
    3 9 6 5    8 2 6
               9 8 5
    - Take the first column (the same index element of each row) and create a row with those elements in the output
    - Same for the other two columns

Data structures:
    - Input: List of M nested lists
    - Output: List of N nested lists
    - Intermediary
        - Range: Iterate through each "column" within the input, in addition to each row

High level ideas:
    - For each index in a list, representing a column, find the element in each nested list (row) within that column and
      create a new list with those elements. Append the resulting list to an output list.

A:
    - Create an empty list 'transposed'
    - Iterate through each column, as determined by the indices of each list
        - i.e. For a row that contains [1, 5, 8], 1 would belong to the first column, 5 to the second, 8 to the third
        - Get the value within each column per row, starting from the first row and ending with the last
        - Store these values in a new list 'new_row'
        - Add 'new_row' to the end of 'transposed'
    - Return 'transposed'

"""

def transpose(matrix):
    transposed = []

    for idx_col in range(0, len(matrix[0])):
        new_row = []
        for idx_row in range(0, len(matrix)):
            element = matrix[idx_row][idx_col]
            new_row.append(element)
        transposed.append(new_row)

    return transposed

# Test cases
# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)