"""
Q2:
Write a function that takes a list of integers as input and counts the number of
pairs in the list. A pair is defined as two equal integers separated by some
other integer(s).
"""

def get_counts(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return counts

def pairs(numbers):
    counts = get_counts(numbers)
    
    pairs = 0
    for count in counts.values():
        pairs += count // 2
    
    return pairs


print(pairs([1, 2, 5, 6, 5, 2])) # --> 2
print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2])) # --> 4



"""
Q5: 
Write a function that takes a lowercase string as input and returns the
length of the longest substring that consists entirely of vowels (a, e, i, o, u).

P:
Given a string, return the length of the longest vowel-only substring.

Rules:
    - Vowels consist of a, e, i, o, u
    - The input will be a lowercase string
    - Assume input will only have alphabetical characters

"roadwarriors"
- 'oa' -> 2 *
- 'a' => 1
- 'io' => 2

"suoidea"
- 'uoi' -> 3 *
- 'ea' -> 2

Data structures:
    - Input: string
    - Output: integer
    - Intermediary:
        - String: Store all vowel characters
        - List: List of substrings

High-level ideas:
    - Iterate through the input. If a char is a vowel, increment a counter. After each char, compare counter to prior longest substring length, resetting the longest length if needed. Return the longest length.
    - Get a list of all substrings. Filter list to substrings that consist only of vowels. Return the length of the longest substring 

A:
    - Create a constant variable VOWELS => 'aeiou'
    - Set a variable 'longest_count' to 0
    - Set a variable 'current_count' to 0
    - For each character in the input string:
        - If the character is in VOWELS:
            - Increment 'current_count' by 1
        - Else:
            - Set 'current_count' to 0
        - Set 'longest_count' to the larger of 'current_count' and 'longest_count'
    - Return 'longest_count'

"""

VOWELS = 'aeiou'

def solve(string):
    longest_count = 0
    current_count = 0
    for char in string:
        if char in VOWELS:
            current_count += 1
        else:
            current_count = 0
        longest_count = max(longest_count, current_count)
    return longest_count

# Examples
print(solve("roadwarriors")) # should return 2
print(solve("suoidea")) # should return 3


"""
Now what if we added the constraint that substrings can only be characters of 2 or more?


High-level ideas:
    - Iterate through the input. If a char is a vowel, increment a counter. After each char, if the counter >= 2, compare counter to prior longest substring length, resetting the longest length if needed. Return the longest length.
    - Get a list of all substrings of length 2 or more. Filter list to substrings that consist only of vowels. Return the length of the longest substring 

A:
    - Create a constant variable VOWELS => 'aeiou'
    - Set a variable 'longest_count' to 0
    - Set a variable 'current_count' to 0
    - For each character in the input string:
        - If the character is in VOWELS:
            - Increment 'current_count' by 1
        - Else:
            - Set 'current_count' to 0
        - If 'current_count' is 2 or greater:
            - Set 'longest_count' to the larger of 'current_count' and 'longest_count'
    - Return 'longest_count'

"""

def solve(string):
    longest_count = 0
    current_count = 0
    for char in string:
        if char in VOWELS:
            current_count += 1
        else:
            current_count = 0
        
        if current_count >= 2:
            longest_count = max(longest_count, current_count)
    return longest_count

# Examples
print(solve("roadwarriors")) # should return 2
print(solve("suoidea")) # should return 3



"""
Q6:
Write a function that takes a string of integers as input and returns the
number of substrings that result in an odd number when converted to an integer.

P:
Given a string of digits, return the number of substrings that create an odd number.

Rules:
    - Odd number means that the last digit of the substring is odd
    - Digits are from 0 to 9
    - Substrings are 1 or more digits
    - The input string itself can be a substring


"1341"
- "1", "13", "3", "1341", "341", "41", "1" => 7 substrings

"1357"
- "1", "13", "3", "135", "35", "5", "1357", "357", "57", "7" => 10

Data structures:
    - Input: String (of digits)
    - Output: Integer (count)
    - Intermediary:
        - List: All substrings, test if each is odd
        - Range: Iterate through each index of the string
        - Integer: 
            - Count all substrings that end with an odd digit, as we iterate through
            - Convert substrings into integers to test if odd
        - Boolean: Is a digit considered "odd"? Yes/no

High-level strategies:
    - Get a list of all substrings of length 1 or more. Filter list to substrings that end in an odd number. Return the list length
    - Iterate through each digit in a string. If a digit is odd, iterate a counter by the number of substrings we can form with the digits that precede, including the current digit. Return the counter value

A:
    - Set variable 'total_count' to 0
    - For each index and digit in the input
        - *is_digit_odd* => input: digit
        - If digit is odd
            - Increment 'total_count' by index + 1
    - Return 'total_count'


*is_digit_odd*: Check if digit is odd
    Input: String (digit)
    Output: Boolean
    Algo:
        - Convert input to integer => 'digit'
        - If 'digit' has a remainder when divided by 2:
            - Return True
        - Otherwise
            - Return False

"""

def is_digit_odd(digit_str):
    digit = int(digit_str)
    return digit % 2 != 0


def solve(digits_str):
    total_count = 0
    for idx, digit in enumerate(digits_str):
        if is_digit_odd(digit):
            total_count += (idx + 1)
    
    return total_count


# # Test cases
print(solve("1341")) # should return 7
print(solve("1357")) # should return 10


"""
Q9: 
Write a function that generates text following a pattern where:
1) the first and last characters of each word remain in their original place
2) characters between the first and last characters are sorted alphabetically
3) punctuation should remain at the same place as it started

P:
Given a string of words, alter each word such that its middle characters are sorted alphabetically, keeping punctuation in place.

Rules:
    - The first and last characters should remain in their original places
    - The characters in between should be sorted alphabetically
    - Any punctuation should remain in the same place
    - If punctuation comes as the first or last character, keep in place the alpha character that comes before or after
        - i.e.: listening, => keep 'l' and 'g' in place, alongside ','
    - Words are separated by single spaces

E:
listening,
    - Ignore , at the end
    - Keep 'l' and 'g'
    - [i, s, t, e, n, i, n] => [e, i, i, n, n, s, t]
    - 'leiinnstg,'

you'll
    - ' is at index 3
    - 'youll'
    - 'y' [o, u, l] 'l'
    - 'yloul'
    - 'ylo'ul'

Data structures:
    - Input: string
    - Output: New string
    - Intermediary:
        - List: 
            - Keep track of all words
            - Keep track of individual characters of a word
        - String: Remove non alphabetical characters
        - Tuple: Keep track of non-alpha index and values

High-level strategies:
    - Create a list of all words. For each word, record the index and values of non-alpha chars. Separate out the middle chars and order alphabetically. Re-insert non-alpha chars at their indices. Add reconstructed word to the end of a new string. Return the string.

A:
    - Create a list 'words' from input
    - Create empty list 'new_words'
    - For each word:
        - *reconstruct_word* => input is word, output 'new_word'
        - Add 'new_word' to end of 'new_words'
    - Combine 'new_words' into one string, separating words by space
    - Return the string

*reconstruct_word*
Input: String
Output: New string
Algo:
    - Create a new string with no non-alpha chars => 'alpha_only'
    - Create a list of tuples 'non_alphas'
        - (index, value) of each non-alpha char
    - Separate the middle chars from 'alpha_only' into a new list => 'first', 'middle' (list), 'last'
    - Sort 'middle' alphabetically
    - Create new list 'reconstructed', concatenating 'first', 'middle', 'last'
    - Add in each char in 'non_alphas' at the index specified
    - Combine 'reconstructed' into one string => 'new_word'


"""


def reconstruct_word(word):
    alpha_only = ''
    non_alphas = []
    for idx, char in enumerate(word):
        if char.isalpha():
            alpha_only += char
        else:
            non_alphas.append((idx, char))
    
    first, *middle, last = alpha_only
    middle.sort()
    reconstructed = [first] + middle + [last]
    for idx, char in non_alphas:
        reconstructed.insert(idx, char)
    
    return ''.join(reconstructed)

def scramble_words(text):
    words = text.split()
    new_words = []
    for word in words:
        new_word = reconstruct_word(word)
        new_words.append(new_word)
    return " ".join(new_words)



# # Test cases
print(scramble_words('professionals')) # should return 'paefilnoorsss'
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.")) # should return "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."


"""
Reflection: 
Time: 23 min 41 seconds. Challenging!!! It worked out well, and I tested as I went, but it took a while.
"""


