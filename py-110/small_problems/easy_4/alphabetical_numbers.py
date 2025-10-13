"""
Write a function that takes a list of integers between 0 and 19 and returns a list of those integers 
sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, 
fifteen, sixteen, seventeen, eighteen, nineteen


P:
Input: List of integers
Output: New list of integers
Rules:
    - Explicit
        - The output list sorts based on the Enlgish word for each number
        - The input list contains integers from 0 to 19, inclusive
    - Implicit
        - An empty input list means we receive an empty output list
        - Sort based on English sort refers to a lexicographical sort based on strings
        - Our output list is not a mutated version of the input list

E: - Confirmed

D:
- We can use a dictionary to store key-value pairs between an integer and its English word perhaps
- Or we can store the English words in a list, where each English word corresponds to the index of the number it represents

A:
    - Create a global variable 'ENGLISH_TRANSLATION' that is assigned a list of English words per index in the list
      (i.e. the first element of the list will be 'zero', which corresponds to the index 0)
    - For each number in the input list:
        - Get its English word
    - Sort the list based on the English words, sorting lexicographically

"""

ENGLISH_TRANSLATION = ["zero", "one", "two", "three", "four", "five", "six", 'seven', 'eight', 'nine', 'ten', 
                       'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

def get_english_word(number):
    return ENGLISH_TRANSLATION[number]

def alphabetic_number_sort(numbers):
    return sorted(numbers, key=get_english_word)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True