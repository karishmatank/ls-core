"""
Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. 
If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, 
then s, t, and k must be related to each other such that s == t * k. The values of t and k should be the shortest possible 
substring and the largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.

P:
Create a tuple, consisting of a string and integer, where both components multiplied together create the input string.

Rules:
    - Input will be a nonempty string
    - t in (t, k) should be the smallest possible substring (by length)
    - k in (t, k) should be the largest possible repeat count
    - The string will be entirely lowercase alphabetic characters
    - If there is no substring shorter than the input string itself, the tuple will include the input string along with 
      the number 1
    - The substring t can be of length 1 or more

Data structures:
    - Input: String
    - Output: Tuple with substring and integer representing a 'factor'
    - Intermediary:
        - String: Creating substrings off of the input string
        - Integer: Represents the factor we'll look to find. Store the length of each substring + length of the input string
        - Dictionary: Store the character and # of occurrencesas they appear in the input string {'x': 2, 'y': 2, ...}
        - Set: Store the unique characters of the input string
        - List: Store valid substrings to then iterate through and find if they can be multiplied by a factor to back into the
          input string

High-level ideas:
    - Find all substrings of length 1 or more. Calculate the right factor that would create a string of the same length as
      the input from the substring, if possible. If the substring * factor recreates the input string, return a tuple with
      the substring and factor
    - Use a dictionary to store key-value pairs with each character and the number of times they occur. If all characters appear
      the same number of times, use the insertion order to recreate the substring, along with the factor being equal to the
      number of times each letter is present in the input string. Check if these recreate the input. If so, return as a tuple

A:
    - Create an empty dictionary 'characters'
    - Populate the dictionary with key-value pairs, with each key being a character and each value being a count for how
      often it occurs in the input string. Build the dictionary by going through character by character
    - Check if all values of the dictionary are the same integer
        - Min value = max value means all values are the same
        - If so, we know that there can a substring possible using the keys
            - Use the keys of the dictionary to create a substring
            - Use the repeating value as the factor
            - If these recreate the input string, return a tuple with both the substring and factor
    - If that method doesn't work , or if all values in the dictionary are not the same integer, return a tuple with the
      input string as our substring and factor of 1
"""

def repeated_substring(string):
    characters = {}
    for char in string:
        characters[char] = characters.get(char, 0) + 1
    
    values = list(characters.values())

    if min(values) == max(values):
        substring = ''.join(list(characters.keys()))
        factor = min(values)
        if substring * factor == string:
            return (substring, factor)
    
    return (string, 1)


# Test cases
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))


"""
Reflection - While this passed the tests, there's a fatal flaw in this algorithm. If we had 'abacabac', the correct substring
would be 'abac', but this algorithm would incorrectly note that 'abac' has 2 a's and one of b and c, therefore we miss seeing
'abac'. The correct algorithm was actually the first one that I had, which was more brute force but correctly goes through
all substrings to find the one that fits the bill here.
"""