"""
Write a function that takes a string and returns a dictionary containing the following three properties:

- the percentage of characters in the string that are lowercase letters
- the percentage of characters that are uppercase letters
- the percentage of characters that are neither

All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. 
Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

P
Given a string, return a dictionary that computes the % of characters that are lowercase, uppercase, or neither.

Rules
- The string will always contain at least one character
- The values of the dictionary should be strings representing 2-decimal place floats
- "Neither" includes any non cased character, such as spaces, other symbols, etc
- The keys of the dictionary are 'lowercase', 'uppercase', or 'neither'

Data structures:
    - Input: String
    - Output: Dictionary
    - Integers: Count the occurrence of lowercase, uppercase, or neither
    - Float: Calculate the percentage of each

High-level strategies:
    - Count the occurrence of each of lowercase, uppercase, or neither by going character by character through the input. 
      Calculate the percentage of each by dividing by the length of the input string. Create a dictionary to store the string
      representations of these percentages rounded to 2 decimals.

A:
    - (Helper) Get the lowercase, uppercase, neither counts
        - Create variables 'lowercase', 'uppercase', and 'neither', all with value 0
        - Check each character in the input string for whether it is alphabetical.
            - If not, increment up 'neither' by 1 and move to the next char
            - If alphabetical, check if lowercase or uppercase
                - If lowercase, increment 'lowercase' by 1
                - Else, increment 'uppercase' by 1
    - (Helper) Convert each of 'lowercase', 'uppercase' and 'neither' to a percentage, then multiply by 100
        - Divide by the length of the input string
    - Create a dictionary with each of these 3 keys ('lowercase', 'uppercase', 'neither'), with their values strings
      rounded to 2 decimals
    - Return the dictionary

"""

def get_counts(string):
    lowercase = 0
    uppercase = 0
    neither = 0
    
    for char in string:
        if not char.isalpha():
            neither += 1
        elif char.islower():
            lowercase += 1
        else:
            uppercase += 1
    
    return lowercase, uppercase, neither

def calculate_percentage(count, denominator):
    count /= denominator
    count *= 100
    return count

def letter_percentages(string):
    lowercase, uppercase, neither = get_counts(string)
    denominator = len(string)

    lowercase = calculate_percentage(lowercase, denominator)
    uppercase = calculate_percentage(uppercase, denominator)
    neither = calculate_percentage(neither, denominator)

    percentages = {}
    percentages['lowercase'] = f"{lowercase:.02f}"
    percentages['uppercase'] = f"{uppercase:.02f}"
    percentages['neither'] = f"{neither:.02f}"

    return percentages




# Test cases
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)