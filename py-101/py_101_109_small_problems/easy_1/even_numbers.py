# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over just the even numbers?

for num in range(1, 100):
    if num % 2 == 0:
        print(num)

# The following is not valid: continue can't be in ternary expression since it is a statement
# for num in range(1, 100):
#     print(num if num % 2 == 0 else continue)

# This works though:
for num in range(1, 100):
    if num % 2 != 0:
        continue
    print(num)

# Bonus
for num in range(2, 100, 2):
    print(num)