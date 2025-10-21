"""
The transpose of a 3x3 matrix is the matrix that results from exchanging the rows and columns of the original matrix. 
Write a function that takes a list of lists that represents a 3x3 matrix and returns the transpose of the matrix. 
You should implement the function on your own, without using any external libraries.

Take care not to modify the original matrix -- your function must produce a new matrix and leave the input 
matrix list unchanged.

P:
Given a list of lists representing a 3x3 matrix, return the transpose of the matrix.

Rules:
    - A transpose is a matrix that switches the rows and columns of an input matrix
    - Our input matrix will consist of 3 nested lists, each with 3 elements
    - The output will also consist of 3 nested lists, each with 3 elements
    - Do not modify the original matrix

E:
    1 5 8    1 4 3
    4 7 2 => 5 7 9
    3 9 6    8 2 6
    - Take the first column (the same index element of each row) and create a row with those elements in the output
    - Same for the other two columns

Data structures:
    - Input: List of 3 nested lists
    - Output: List of 3 nested lists
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


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True