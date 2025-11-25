# Q1:
# Predict the output of the following code:

a, b, c = (1, 2, 3)
print(a, b, c)

# This will print "1 2 3". We unpack the tuple into variables a, b, c, and then print them side by side.

# Q2:
# What value will _ have after executing the following code?

a, _, c = (1, 2, 3)

# _ will have the value 2

# Q3:
# Will the following code raise an error? If so, what kind? Try answering without running the code.

a, b = (1, 2, 3)

# Yes, this will raise a ValueError because there are too many values to unpack.

# Q4:
# What happens when you run the following code? Try answering without running the code.

a, b, c, d, e = (1, 2, 3)

# Python will raise a ValueError as there are too few values to unpack.

# Q5
# What will rest contain after running this code? Try answering without running the code.

a, *rest = [1, 2, 3, 4, 5]

# rest will contain [2, 3, 4, 5]

# Q6
# What will the following code output? Try answering without running the code.

first, *middle, last = "hello"
print(f"First: {first}, Middle: {middle}, Last: {last}")

# This will print "First: h, Middle: ['e', 'l', 'l'], Last: o"

# Q7
# Write a single line of code that swaps the values of a and b.

a = 1
b = 2

print(f"{b=}")
print(f"{a=}")

b, a = a, b

print(f"{b=}")
print(f"{a=}")

# Q8
# What will x and y be after this code runs?

((x, y), z) = ((1, 2), 3)

# x will be 1 and y will be 2