"""
Refactor our recursive Fibonacci function to use memoization.

P:
Input: Integer 
Output: Integer
Rules:
    - Output is the Fibonacci number at the position specified by the input
    - Memoization involves saving answers for future reuse, instead of computing from scratch each time
        - Ex: fibonacci(number - 1) involves using fibonacci(number - 2), so we can save the answer to fibonacci(number-2) to
          avoid calling it again later within the recursion

D:
    - List: Store Fibonacci sequence values as they are computed

High-level strategies:
    - Populate a global list with Fibonacci sequence values as we compute them. Refer back to the list when we need to recall
      values already calculated

A: 
    - Create a global list to store the Fibonacci sequence values, initialized to two elements with values 1 and 1
    - Check if the list has an element at the index represented by the input number 'n' - 1
        - If it exists, return the element's value
        - If it doesn't
            - Calculate by finding the sum of the 'n-1' and 'n-2' Fibonacci numbers
            - Add the result to the list
            - Return the result

"""

fibonacci_sequence = [1, 1]

def fibonacci(number):
    if number <= len(fibonacci_sequence):
        return fibonacci_sequence[number - 1]
    value = fibonacci(number - 1) + fibonacci(number - 2)
    fibonacci_sequence.append(value)
    return value

# Test cases
print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True