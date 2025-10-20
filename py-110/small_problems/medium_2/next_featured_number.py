"""
A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits occurring exactly once each. For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

Note: The largest possible featured number is 9876543201.

P:
Given an integer, return the next highest featured number greater than the integer itself.

Rules:
    - A featured number is:
        - odd, 
        - a multiple of 7
        - Each digit occurs once
    - The largest possible featured number is 9876543201
    - If there is no next featured number, return a string with an error message instead
    - If the input is a featured number, we still have to find the next featured number **greater** than the input. Can't be equal
    - Assume input is a positive integer

E:
Confirmed

Data structures:
    - Input: Integer
    - Output: Either integer or string
    - Intermediary:
        - Integer: 
            - Keep track of candidate featured numbers as we go that are larger than the input, run them through our tests
            - Keep track of a "factor" we can multiply by 7 to come up with our candidate featured numbers
        - Boolean: Is a candidate number a featured number? Yes/no
        - String: Parse through digits of candidate featured numbers to check if each digit occurs more than once
        - Set: Get the unique digits of a string after creating our intermediary string object

High-level ideas:
    - Find the integer component when we divide the input integer by 7. This component + 1 will be our starting "factor", incrementing up as we go. For each factor, test whether the factor * 7 qualifies as a featured number. If so, return this value

A:
    - Calculate our starting factor
        - Integer component after dividing the input by 7 + 1
    - Until we find our resulting value:
        - Calculate a candidate featured number by multiplying the factor by 7
        - If the candidate > 9876543201:
            - Return an error message in a tuple
        - Check if the candidate is a featured number
            - (Helper) Input: integer, Output: Boolean
            - Check if the input is odd, if not, return False
            - If all digits differ, return True
                - Create a string representation of the integer
                - Use a set to find all of the unique digits
                - If the length of the set is equal to the length of the string, return True
        - If so, return the number
        - If not, increment the factor by 1

"""

def is_featured_number(candidate):
    if candidate % 2 == 0:
        return False
    
    candidate_str = str(candidate)
    if len(set(candidate_str)) == len(candidate_str):
        return True

    return False

def next_featured(number):
    factor = (number // 7) + 1
    while True:
        candidate = factor * 7
        if candidate > 9876543201:
            return ("There is no possible number that "
                    "fulfills those requirements.")
        if is_featured_number(candidate):
            return candidate
        factor += 1

# Test cases
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True


"Reflection: Time just above 19 min. Take the time to test more as you go. Practice speaking out loud too."