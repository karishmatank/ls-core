"""
A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.

To be a valid triangle, the sum of the angles must be exactly 180 degrees, and every angle must be greater than 0. 
If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and returns one of the following four 
strings representing the triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to worry about floating point errors. 
You may also assume that the arguments are in degrees.

P:
Given 3 angles, determine whether they would make up a 'right', 'acute', 'obtuse' or 'invalid' triangle.

Rules:
    - A valid triangle means that the sum of the angles is exactly 180 degrees, and each angle > 0
    - A right triangle means one angle is 90 degrees
    - An acute triangle means that all 3 angles are < 90
    - Obtuse means 1 angle is > 90
    - Assume all angles have integer values
    - Assume all arguments are in degrees
    - Assume any one angle given isn't > 180

E: Confirmed

Data structures:
    - Input: 3 integers
    - Output: String - one of "right", "acute", "obtuse", or "invalid"
    - Intermediary:
        - List / Tuple: Store all input angles
        - Boolean: Do the angles make up a valid triangle? Yes / no
        - Integer: Store the sum of the angles

High-level strategies:
    - Use the input angles to determine whether we have a valid triangle. If so, classify the triangle into "acute", "obtuse",
      or "right". Otherwise, classify as an "invalid" triangle based on the value of the largest angle.

A:
    - Store the angles in a list 'angles'
    - (Helper) Check if these angles make up a valid triangle
        - If all angles are > 0 and the sum of the angles is 180, return True
            - In reality, we only need to check if the smallest angle is > 0, as that means all angles are > 0
        - Otherwise, return False
    - If triangle is not valid, return "invalid"
    - Get the value of the largest angle in 'angles'
    - If the largest angle is > 90, return "obtuse"
    - If the largest angle is 90, return "right"
    - Otherwise, return "acute"

"""

def is_valid_triangle(angles):
    return min(angles) > 0 and sum(angles) == 180

def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]
    if not is_valid_triangle(angles):
        return "invalid"
    
    largest_angle = max(angles)
    if largest_angle > 90:
        return "obtuse"
    elif largest_angle == 90:
        return "right"
    else:
        return "acute"
    


# Test cases
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

