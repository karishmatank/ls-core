"""
Create a function that takes two strings as arguments and returns True if some portion of the characters in the first string can be rearranged to match the characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

P:
Given two strings, return True if we can use a subset or all characters from the first string to form the second string.

Rules:
    - Both strings will only have lowercase alphabetic characters
    - Neither input will be empty
    - In order to return True, len of first input should be >= len of second


'', 'launchschool'
launchschool

'asa', 'pythonrules'
'pythonrul' => return false

Data structures:
    - Input: 2 strings
    - Output: Boolean
    - Intermediary:
        - List: Get all characters of the first input, mutate list as we are checking whether first input has all characters needed
        - Range: Iterate through second input
        - Dictionary: Count all characters in both strings. If dict related to second input is a "subset" of the first, return True

High-level strategies:
    - Create a list from the 1st string. Iterate through 2nd string. For each char in 2nd, if it is found in the list, remove from list. If not, return False. If we get to end, return True
    - Create a dictionary from the 1st string, where key = char and value = count. For each char in 2nd string, if char is a key in dict, increment down its value. If key doesn't exist or count would go negative, return False. Else, return True at the end

A:
    - Create list 'list_first' from 1st string input
    - For char in 2nd input:
        - Check if char is in 'list_first'
        - If there:
            - Remove char from 'list_first' (mutating)
        - Otherwise:
            - Return False
    - Return True

"""

def unscramble(str1, str2):
    list_first = list(str1)
    for char in str2:
        if char in list_first:
            list_first.remove(char)
        else:
            return False
    return True


# Test cases
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)

"""
Reflection:
Time: 15 min 49 seconds. Felt pretty easy compared to others. Liked that I came up with multiple ways to do this. Everything smooth.
"""