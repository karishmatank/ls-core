"""
Implement a function that takes a list of strings and groups anagrams together.
Anagrams are words that have the same characters but in a different order.

P:
Input: List of strings
Output: Nested list
Rules:
    - Explicit
        - The output should created nested lists, where each nested list consists of all related anagrams
        - Anagrams are words that have the same characters but in a different order
    - Implicit
        - An empty input list means we return an empty output list
        - Assume that if there are duplicate words in the input, keep the duplicates in the output
        - The order of the groups and words within the groups in the output doesn't ultimately matter

E: Confirmed

D: We can use a set to find the strings with unique letters.

A:
    - Assign a variable 'unique_letter_combos' to an empty set
    - Assign a variable 'grouped_words' to an empty list
    - For each word in the input list:
        - Assign a new variable 'reordered', which is a string with the letters in the word ordered from a to z
        - Add 'reordered' to 'unique_letters'
    - For each set of letters in 'unique_letters':
        - Create a list of all words in the input list that have the same letters
        - Append this list to 'grouped_words'
    - Return 'grouped_words'
        
"""

def reordered_string(string):
    return ''.join(sorted(string))

def group_anagrams(words):
    unique_letter_combos = set()
    grouped_words = []

    for word in words:
        reordered = reordered_string(word)
        unique_letter_combos.add(reordered)
    
    for combo in unique_letter_combos:
        grouped_words.append([word for word in words if reordered_string(word) == combo])
    
    return grouped_words

# Test cases
result1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# The order of the groups and words within the groups does not matter for correctness.
# The following check sorts both results to ensure they contain the same groups.
print(sorted([sorted(group) for group in result1]) == sorted([sorted(group) for group in expected1]))

result2 = group_anagrams(["listen", "silent", "enlist"])
expected2 = [["listen", "silent", "enlist"]]
print(sorted([sorted(group) for group in result2]) == sorted([sorted(group) for group in expected2]))