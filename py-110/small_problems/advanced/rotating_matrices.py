"""
Write a function that takes an arbitrary MxN matrix, rotates it clockwise by 90-degrees as described above, 
and returns the result as a new matrix. The function should not mutate the original matrix.

P:
Given a list of lists representing a matrix, rotate the matrix clockwise by 90 degrees and return the resulting list of lists.

Rules:
    - Our function should work with any sized matrix MxN
    - Do not mutate the original matrix
    - If an input matrix has dimensions MxN, the rotation will have dimensions NxM

E:
    3 7 4 2 => 5 3 => 8 0 1 5 => 2 8 => 3 7 4 2
    5 1 0 8    1 7    2 4 7 3    4 0    5 1 0 8
               0 4               7 1
               8 2               3 5
    - Take each "column", as per the indices of the first "row", but start collecting elements from the last row
      to the first row

Data structures:
    - Input: List of lists
    - Output: List of lists
    - Intermediary
        - List: Store the new rows of our rotated matrix
        - Range: Iterate through the rows and columns

High-level ideas:
    - For each column of our matrix, create a new list that orders elements within that column from the last row to the first.
      These now make up the new rows of our rotated matrix, which we can each store in a list that we'll return.

A:
    - Create an empty list 'rotated'
    - Find the number of columns of our input matrix
    - Find the number of rows of our input matrix
    - Iterate through each column of the matrix (via index of elements per row)
        - Create an empty list 'new_row'
        - Starting from the last row in the input matrix: 
            - Find the element in that row and in the column we are iterating through
            - Add the element to the end of 'new_row'
            - Start: -1
            - End: -length of input matrix - 1 (exclusive, we want to include -length of input matrix)
        - Once we finish iterating through rows, add 'new_row' to the end of 'rotated'
    - Return 'rotated'
               
"""

def rotate90(matrix):
    rotated = []
    num_cols = len(matrix[0])
    num_rows = len(matrix)

    for idx_col in range(num_cols):
        new_row = []
        for idx_row in range(-1, -num_rows - 1, -1):
            element = matrix[idx_row][idx_col]
            new_row.append(element)
        rotated.append(new_row)
    
    return rotated

# Test cases
matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)