# Write a function that takes a positive integer, n, as an argument 
# and prints a right triangle whose sides each have n stars. 
# The hypotenuse of the triangle (the diagonal side in the images below) 
# should have one end at the lower-left of the triangle, and the other end at the upper-right.

def triangle(height):
    for row in range(height):
        num_stars = row + 1
        num_spaces = height - num_stars
        print(" " * num_spaces + "*" * num_stars)

triangle(5)
print()
triangle(9)