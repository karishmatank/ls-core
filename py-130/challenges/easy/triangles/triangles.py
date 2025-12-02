"""
Write a program to determine whether a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has exactly two sides of the same length.

A scalene triangle has all sides of different lengths.

Note: For a shape to be a triangle at all, all sides must be of length > 0, and the 
sum of the lengths of any two sides must be greater than the length of the third side.

P:
Given 3 sides of a triangle, determine whether it is equilateral, isosceles, or scalene

Rules:
- A triangle exists when all sides are of length > 0, and the sum of the lengths of any two sides > the third
- An equilateral triangle has all 3 of the same length sides
- An isosceles triangle has 2 sides of the same length
- A scalene triangle has all different lengths
- We should raise a ValueError if we get invalid side lengths or if the lengths do not make up a triangle
- We should create a property `kind` that calculates the type of triangle
- Assume we will get integers as sides

E:
- 2, 2, 2 => all length > 0, sum of any 2 sides = 4 > 2. All equal => equilateral
- 3, 4, 4 => all > 0, sum of 2 smallest = 7 > 4. 2 equal => isosceles
- 3, 4, 5 => all > 0, sum of 2 smallest = 7 > 5. None equal => scalene

D:
Input: 3 integers (sides)
Output: `kind` property returns string or raises ValueError
Intermediate:
    - List: Store the triangle sides
    - Boolean: Helper function to check if is a valid triangle
    - Set: Get / count unique side values
    - Dictionary: Record counts of unique side values

High-level strategies:
    - Store sides in a list. Check if valid triangle by checking that each side > 0 and that the sum of the smallest 2 sides > 
      third side. If not valid, raise ValueError. Classify triangle by checking how many unique side values there are.

A:
- Create instance of class Triangle
    - Accept 3 int arguments, store in list `_sides`
    - Check that sides are valid => `_check_validity()`
    - If invalid, raise ValueError
- Property kind
    - Getter only, dynamically calculate triangle type
    - Create set out of `self._sides`
    - If 1 unique value, return "equilateral"
    - If 2, return "isosceles"
    - Else, return "scalene"

Helper: `_check_validity(self)`
Input: `_sides` instance variable (list)
Output: Boolean
Steps:
    - Sort sides from smallest to largest
    - If smallest side < 0, return False
    - If sum of smallest 2 sides <= third side, return False
    - Otherwise return True
"""

class Triangle:
    def __init__(self, side1, side2, side3):
        self._sides = sorted([side1, side2, side3])
        if not self._is_valid():
            raise ValueError
    
    def _is_valid(self):
        if self._sides[0] <= 0 or sum(self._sides[:-1]) <= self._sides[-1]:
            return False
        return True
    
    @property
    def kind(self):
        unique_sides = len(set(self._sides))
        if unique_sides == 1:
            return "equilateral"
        elif unique_sides == 2:
            return "isosceles"
        else:
            return "scalene"