"""
Create a function that takes a string argument and returns a copy of the string with every second character in every third word converted to uppercase. Other characters should remain the same.

P:
Return a string that uppercases every second char in every third word.

Rules:
    - All other characters maintain the same case
    - Word is defined as continuous string of characters, separated by a space
    - If the third word only has one character, it remains the same
    - There can be punctuation included as part of a word

Data structures:
    - Input: string
    - Output: New string (with uppercases where relevant)
    - Intermediary:
        - List: Store words in order
        - String / list: Transform each word

High-level strategies:
    - Split string into words. For every third word (indices 2, 5, 8, ...), capitalize every second letter (odd indices). Combine back into one string and return.

A:
    - Create empty list "transformed"
    - Create a list of words from input
    - Create variable word_count, set to 0
    - For word in list:
        - Increment word_count by 1
        - If word_count is a multiple of 3:
            - Get string- *capitalize_every_second* input word
            - Add string to end of "transformed"
        - Else
            - Add word to end of "transformed"
    - Combine words in "transformed" into 1 str
    - Return the combined str

capitalize_every_second
- Input: String
- Output: String
- Algo:
    - For characters at odd indices:
        - Transform character into uppercase
    - Combine words in list into one string
    - Return string

"""

def capitalize_every_second(word):
    capitalized = []
    for idx, char in enumerate(word):
        if idx % 2 == 1:
            capitalized.append(char.upper())
        else:
            capitalized.append(char)
    return ''.join(capitalized)

def to_weird_case(text):
    transformed = []
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
        if word_count % 3 == 0:
            transformed.append(capitalize_every_second(word))
        else:
            transformed.append(word)
    return " ".join(transformed)



# Test cases
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

"""
Time: 22 min 21 s

Probably should have thought a bit more about how to get every third word instead of relying on index 2, 5, 7, ...
Eventually corrected in the algorithm.
"""