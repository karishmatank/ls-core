"""
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.

To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the 
longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, 
the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the 
following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

P:
Determine whether the 3 given floats create an equilateral, isosceles, scalene or no triangle at all.

Rules:
    - A triangle is defined as the sum of the two shortest sides > longest side + every side > 0
    - Equilateral means all 3 sides have the same length
    - Isosceles means that 2 sides have the same length while the third is different
    - Scalene means that all 3 sides have different lengths
    - Assume we'll always receive 3 floats as input with value 0 or greater

E: Confirmed

Data structures:
    - Input: 3 floats, each representing the side of a triangle
    - Output: String, either "equilateral", "isosceles", "scalene", or "invalid"
    - Intermediary:
        - List / Tuple: List to store the lengths + use built-in methods to calculate the min or max sides
        - Boolean: Do the sides make up a valid triangle? Yes / no
        - Set: Determine the number of unique side "values" we got (1, 2, or 3 unique values)

High-level ideas:
    - Figure out whether the sides make a valid triangle first. If so, determine the type of triangle based on the number of
      unique side values given
        - To figure out whether the sides make a valid triangle, calculate the sum of the two shortest sides, check that 
          the sum is > than the longest side, and make sure every side > 0

A:
    - Store the inputs into a list 'sides'
    - (Helper) Figure out whether the sides make a valid triangle
        - If any one of the triangle sides is <= 0, return False
        - Find the two smallest sides and calculate their sum
        - If the sum is <= the longest side, return False
        - Otherwise, return True
    - If we have an invalid triangle, return "invalid"
    - Create a set using the input values
    - If the length of the set is 1, return "equilateral"
    - If the length is 2, return "isosceles"
    - Else, return "scalene"

"""

def is_triangle(sides):
    for side in sides:
        if side <= 0:
            return False

    sorted_sides = sorted(sides)
    *smallest, largest = sorted_sides
    if sum(smallest) <= largest:
        return False
    
    return True

def triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    if not is_triangle(sides):
        return "invalid"
    
    unique_side_values = set(sides)
    num_unique = len(unique_side_values)
    if num_unique == 1:
        return "equilateral"
    elif num_unique == 2:
        return "isosceles"
    else:
        return "scalene"


# Test cases
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

"""
Time: 17.5 min
"""