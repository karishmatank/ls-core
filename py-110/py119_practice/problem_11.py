"""
Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, then s, t, and k must be related to each other such that s == t * k. The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.

P:
Given a string 's', find the smallest substring 't' and largest integer 'k', such that t * k matches the value of s. Return as a tuple (t, k)

Rules:
    - Input will be non-empty and entirely lowercase alphabetic chars
    - If there are no valid repeating substrings, return a tuple with the input string and integer 1 (we can't repeat)
    - Need smallest substring 't' and largest integer 'k'

Data structures:
    - Input: string
    - Output: Tuple (string , integer)
    - Intermediary:
        - Strings: Test validity of a substring
        - Integer: Keep track of potential valid 'k' values
        - Boolean: Is substring valid? Yes/no
        - Dictionary: Key is a character, value is a count

High-level strategies:
    - Iterate through input string. Form substrings 't' with characters, starting from first char. Calculate factor 'k' using length of substring vs length of input. If 't' * 'k' matches input, return both in tuple.
    - Create a dictionary with keys as characters and values as their counts. If all counts match, we have a valid substring based on the insertion order of the keys and the factor being the count. Return as a tuple. *Assumes non-repeating characters in a substr*

A:
    - Create empty string 'substring'
    - For each char in input:
        - Add char to end of 'substring'
        - Calculate 'factor' as length of input / length of 'substring'
        - If 'factor' is not whole number (there is a remainder):
            - Continue to next character
        - Create new string that multiplies 'substring' by 'factor' (as integer)
        - If new string is same as input:
            - Return tuple ('substring', 'factor')
    - Return tuple (input, 1)

"""

def repeated_substring(string):
    substring = ''
    for char in string:
        substring += char
        factor = len(string) / len(substring)
        if factor % 1 != 0:
            continue
        new_str = substring * int(factor)
        if new_str == string:
            return (substring, factor)
    return (string, 1)


# Test cases
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

"""
Reflection: 
Time: 23 min 20 seconds. Something weird happened as I was testing my code, where it was printing some lines multiple times
Not sure still what happened. It seemed to have fixed itself at the end?

One other note: In the tuple we return, should return the int casted factor, not the factor itself, as it is a float.
Our last return of (string, 1) is not reached either, which is fine, as the last loop of the code for a string that can't
find a smaller substring will effectively return (string, 1) too.

"""