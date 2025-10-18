"""
The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. 
The first two Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, 
the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)

Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to the function:

P:
Input: Integer
Output: Integer
Rules:
    - Explicit
        - Return a number that represents the nth Fibonacci number, where "n" is passed in as input.
        - Fibonacci series is a sequence of numbers where each number is the sum of the prior two. The first two digits are 1s
    - Implicit
        - Assume our input will be a positive integer

D:
    - List: Store the Fibonacci sequence as we build it, and get the nth Fibonacci number at the nth index
    - Range: Iterate through a range of numbers, calculating each Fibonacci number as we go. Store only the latest numbers
    - Integer: Keep track of the two latest Fibonacci numbers as we iterate through a range

High-level strategies:
    - Build a list of Fibonacci numbers as we go, n times. Return the value at the nth index of the list
    - Use variables to keep track of the 2 latest numbers as we go, n times. Return the value of the variable 
      representing the latest value after we're done   
    - Similar to the strategy above but use a list to keep track of the 2 latest numbers

A:
    - If the input number is 1 or 2, return 1
    - Create a list 'latest_fibonacci_nums' with value [1, 1]
    - For a variable 'idx' ranging from 2 to the input number (exclusive):
        - Sum both values in 'latest_fibonacci_nums'
        - Add this new value to the end of 'latest_fibonacci_nums'
        - Remove the "oldest" value in the list
    - Return the value at index 1 in 'latest_fibonacci_nums'

"""

def fibonacci(number):
    if number in [1, 2]:
        return 1
    latest_fibonacci_nums = [1, 1]
    for _ in range(2, number):
        latest_fibonacci_nums.append(sum(latest_fibonacci_nums))
        latest_fibonacci_nums.pop(0)
    return latest_fibonacci_nums[1]


# Test cases
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True