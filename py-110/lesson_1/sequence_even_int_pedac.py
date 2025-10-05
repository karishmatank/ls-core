"""
Imagine a sequence of consecutive even integers beginning with two. 
The integers are grouped in rows, with the first row containing one integer, 
the second row containing two integers, the third row three integers, and so on. 
Given an integer representing the number of a particular row, return an integer representing 
the sum of all the integers in that row.

- Input: Integer (representing row #)
- Output: Integer (representing sum of integers in the row # provided)
- Problem requirements:
    - Explicit:
        - Sequence of integers, beginning with 2
        - Integers are all consecutive and even
        - Sequence grouped into rows
        - Each row is incrementally larger than the last (1st row = 1 int, 2nd row = 2 int, etc)
    - Implicit:
        - Row number = # of integers in that row
    - It's helpful here to visualize the sequence:
        - 2
        - 4, 6
        - 8, 10, 12
        - 14, 16, 18, 20
- Data structures: nested list

Algorithm:
1. Create an empty 'rows' list to hold all of our rows
2. Create a 'row' list and add it to the overall 'rows' list
3. Repeat step 2 until all necessary rows have been created
    1. Stop making rows when length of outer list 'rows' is equal to the input 
4. Sum the final row, which is the last element of 'rows'
5. Return the sum from step 4

Step 2 is pretty vague and sounds like it needs to be expanded upon even more. We can repeat our PEDAC process 
for that step specifically:

- Mini problem: Create a row
- Rules:
    - Row is a list
    - Row contains integers
    - Integers are consecutive even numbers
    - Integers in each row form part of a larger overall sequence
    - Rows are of different lengths
- Input:
    - The row number, which is the length of the row
    - The starting integer
- Output: The row itself (list)
- Examples:
    - If start is 2 and length is 1 —> [2]
    - If start is 4 and length is 2 —> [4, 6]
    - If start is 8 and length is 3 —> [8, 10, 12]
- Data structure: List
- Algorithm:
    1. Create an empty 'row' to contain the integers
    2. Add the starting integer
    3. Increment the starting integer by 2 to get the next integer in our sequence
    4. Repeat steps 2 and 3 until the list has reached the correct length
    5. Return 'row'

Note that we had to take a step back into our algorithm to figure out how to find the starting integer 
before creating the row, as per the input necessary for “create a row” mini problem detailed in step 4. We did so as follows:

- Mini problem: calculating the starting integer
- Rule: First integer of row == last integer of preceding row + 2
- Algorithm
    - Get the last row of the 'rows' list
    - Get the last integer of that row
    - Add 2 to that integer
    

"""


def sum_even_number_row(row_number):
    rows = []
    starting_int = 2

    for row_length in range(1, row_number + 1):
        row = create_row(row_length, starting_int)
        rows.append(row)
        starting_int = row[-1] + 2
    
    return sum(rows[-1])

def create_row(row_length, starting_int):
    row = []
    next_int = starting_int

    for _ in range(0, row_length):
        row.append(next_int)
        next_int += 2
    return row

# Test cases
print(sum_even_number_row(1) == 2)
print(sum_even_number_row(2) == 10)
print(sum_even_number_row(4) == 68)

# print(create_row(1, 2) == [2])
# print(create_row(2, 4) == [4, 6])
# print(create_row(3, 8) == [8, 10, 12])