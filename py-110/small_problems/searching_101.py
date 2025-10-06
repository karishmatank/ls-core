"""
Problem (as provided): 
Write a program that solicits six (6) numbers from the user and prints a message that describes whether the 
sixth number appears among the first five.

**** Step 1: Understand the problem ****
Input: 6 integers, provided one at a time
Output: String, which includes a message on whether the last number appears among the first 5.
Requirements:
    - Explicit:
        - Ask the user for 6 integers, having them provide each number one at a time
        - We then print a message based on whether the 6th integer is within the first 5 provided
    - Implicit:
        - We should prompt the user, indicating whether they are entering the 1st, 2nd, etc.
        - The message we print at the end should list the first 5 numbers provided, in order and comma separated, 
          after noting whether the last number is in that list

Questions:
    - How should the program treat empty inputs? Should we re-prompt the user if they fail to provide an input?
    - Can inputs be negative integers as well?
    - How should the program react if the user provides a non-integer input?
    - Is it important that we convert the integers to int? Or can we keep the input as strings?

**** Step 2: Examples and test cases ****
Example 1:
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Example 2:
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

Observations:
    - We should prompt the user for input for each number based on a customized message 
      (added above to implicit requirements)
    - No mention of invalid inputs, negative integers, etc. so we won't implement that right now

**** Step 3: Data structures ****
I think it makes sense to use a list here. We need a mutable collection to keep adding numbers on as the user provides them.
We also need to maintain order, which lists help well with.

**** Step 4: Algorithm ****
    1. Assign a variable 'numbers' to an empty list.
    2. Use a range to loop through counters, starting from 1 and ending at 6, inclusive.
    3. For each value of counter:
        a. If counter is 1 to 5 inclusive, provide a customized message that gives one of 1st, 2nd, 3rd, 4th, or 5th.
        b. If counter is 6, provide the message "Enter the last number: "
        c. Ask the user to provide a number
    4. Add the input to the end of 'numbers'
        a. I won't convert explicitly to int, as we don't need to for this problem. We are simply going to check if an 
           input is within the first 5 later, which doesn't require us to coerce to int
    5. Go back to step 3, stopping only when we have collected 6 numbers from the user
    6. Check if the last number is included within the first 5 provided by the user
        a. If so, print a message that states that the number "is in" followed by a list of the first 5 numbers 
           separated by commas
        b. If not, print a message that states the number "isnt' in" followed by a list of the first 5 numbers
           separated by commas

**** Step 5: Code ****
See below
"""

numbers = []
for counter in range(1, 7):
    match counter:
        case 1:
            ordinal = "1st"
        case 2:
            ordinal = "2nd"
        case 3:
            ordinal = "3rd"
        case 6:
            ordinal = "last"
        case _:
            ordinal = f"{counter}th"

    num = input(f"Enter the {ordinal} number: ")

    numbers.append(num)

if numbers[-1] in numbers[:-1]:
    print(f"{numbers[-1]} is in {','.join(numbers[:-1])}.")
else:
    print(f"{numbers[-1]} is not in {','.join(numbers[:-1])}.")