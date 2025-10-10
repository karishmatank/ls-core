"""
Write a function that counts the number of occurrences of each element in a given list. 
Once counted, print each element alongside the number of occurrences. 
Consider the words case sensitive e.g. ("suv" != "SUV").

P:
Input: List
Output: Print to console
Rules:
    - Explicit
        - The input list may have repeating elements
        - As an output, we should print each element alongside the number of occurrences of that element in the list
        - Strings with the same letters but in different cases are considered different (i.e. 'suv' != 'SUV')
    - Implicit
        - An empty list should return no output
        - Based on the test case, assume the strings will always have at least one character
        - Assume the elements will be strings
        - Output to the console should be formatted as the element value followed by " => " followed by the number of times
          the element appears in the list

Questions:
    - How should we treat an empty list?
    - Should we count elements that may be empty strings?
    - Will the elements always be strings?

E:
    - Confirmed understanding

D:
List is input. Two ideas for intermediary data structures:
    - Use dictionaries to keep track of counts
    - Use a set to get the unique elements, count the number of times we see each unique element in the list

A:
    - Get the unique elements in the input list and assign to variable 'unique_elements'
    - For each unique element
        - Find the number of times the element appears in the input list
        - Print the element, followed by " => ", followed by the number of times it appears in the input list

"""

def count_occurrences(lst):
    unique_elements = set(lst)
    for element in unique_elements:
        print(f"{element} => {lst.count(element)}")

# Test cases
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
# # your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2