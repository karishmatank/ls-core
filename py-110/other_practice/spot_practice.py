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


#### COME BACK TO THIS ONE ####
"""
Write a function that, given a string of text, returns a list of the top-3 most
occurring words, in descending order of the number of occurrences.

Assumptions:
- A word is a string of letters (A to Z) optionally containing one or more apostrophes (').
- Matches should be case-insensitive.
- Ties may be broken arbitrarily.
- If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty list if a text contains no words.

P:
Given a string, return the 3 most frequently occurring words.

Rules:
    - A word contains alphabetical characters, potentially including one or more '
    - Ignore case
    - If there is a tie, no rule to break it
    - If there are fewer than 3 words, return the top 2 or top 1, or an empty list if there are no words.
    - A single ' char doesn't count as a word

Data structures:
    - Input: string
    - Output: List of 3 strings
    - Intermediary
        - String: Common punctuation that we want to exclude
        - List: List of words (all lowercased)
        - Dictionary: Key = word, value = count

High-level strategies:
    - Create a string that takes out all punctuation. Create a list of words from the string, and populate a dictionary where keys are lowercased words and their values are counts. Return the 3 words with the highest count (highest to lowest order)
    - 

"""

# # Test cases
# top_3_words(" , e .. ") # ["e"]
# top_3_words(" ... ") # []
# top_3_words(" ' ") # []
# top_3_words(" ''' ") # []
# top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.""") # should return ["a", "of", "on"]


"""
Q13:
Modify the kebabize function so that it converts a camel case string into a
kebab case. Kebab case separates words with dashes '-'; camel case identifies
separate words by upcasing the first character in each new word.


P:
Given a camel case string, convert to kebab case.

Rules:
    - Kebab case separates words with -, all words are lowercase
    - Camel case separates words by uppercasing the first letter of each subsequent word (2nd, 3rd, ...)
    - Kebab case doesn't include digits (numbers/ int)
    - Assume all words are either all alphabetical or not at all

E:
camelsHaveThreeHumps
"camels" "have" "three" "humps"

myCamelHas3Humps
"my" "camel" "has" "humps"

Data structures:
    - Input: String
    - Output: New string
    - Intermediary
        - List: Store each word
        - Boolean: Is each word alphabetical? Yes/no

High-level ideas:
    - Parse each word of the input string into a list of words. If a word is not alphabetical, ignore. Combine the valid elements of the list with a "-" in between and return.

A:
    - *parse_words* => input: input str, output: list 'words'
    - Concat words in 'words' together with "-" in between
    - Return the resulting str


*parse_words*
    Input: String
    Output: List of strings
    Algo:
        - Create empty list 'words'
        - Create empty string 'word'
        - For each character in the input
            - If character is lowercase + alphabetical:
                - Add on to end of 'word'
            - If char is uppercase + alphabetical:
                - Add current 'word' to the end of 'words'
                - Reset 'word' to an empty str
                - Add lowercased char to end of 'word'
            - Else:
                - Ignore
        - Add final 'word' to end of 'words'
        - Return 'words'


"""

def parse_words(text):
    words = []
    word = ""
    for char in text:
        if char.isalpha() and char.islower():
            word += char
        elif char.isalpha() and char.isupper():
            words.append(word)
            word = ""
            word += char.lower()
    words.append(word)
    return words

def kebabize(text):
    words = parse_words(text)
    return "-".join(words)

# # Test cases
print(kebabize('camelsHaveThreeHumps')) # should return 'camels-have-three-humps'
print(kebabize('myCamelHas3Humps')) # should return 'my-camel-has-humps'


"""
Reflection:
Time: 17 min 36 seconds. The call to .append can probably be cleaner as we have it twice, once after, but it works so I'll leave as is for now.

"""


"""
Q17:
You will be given a number, and you need to return it as a string in
expanded form.

Note: All numbers will be whole numbers greater than 0.

P:
Given a number, return a string with the addition operations necessary to recreate the number.

Rules:
    - Input will be a whole number > 0
    - The numbers in the addition operations should represent each "place" in the number (i.e. 100s, 10s, 1000s, etc)

E:
12 => 10, 2 left over => 10 + 2
70304 => 4, leaves us 70300 => 300 => leaves us 70000

Data structures:
    - Input: Integer
    - Output: String
    - Intermediary:
        - List: Store each component
        - Integer: "Factor" for which to divide the input 
        - String: Represent input integer

High-level ideas:
    - Coerce input into string. Iterate over string, getting each digit alongside # of digits that follow as a "factor". Multiply int digit by the factor and add to an output list. Return the components of output list with a "+" in between elements
    - Start with a factor of 10. Create copy of input 'number'. Get remainder when dividing 'number' by factor to get the ones place, store in an output list and subtract from 'number' Keep repeating and multiplying factor by 10 until 'number' is 0. Reverse order of output list and combine into string with "+" in between elements

A:
    - Create 'number', set to input value
    - Create 'factor', set to 10
    - Create empty list 'components'
    - Repeat until 'number' is 0:
        - Get 'remainder' of 'number' div by 'factor'
        - If 'remainder' is not 0, add to end of 'components'
        - Set 'number' to prior value - 'remainder'
        - Multiply 'factor' by 10
    - Reverse order of 'components'
    - Coerce each element of 'components' to str
    - Concatenate together with "+" in between 
    - Return resulting string

"""

def expanded_form(input_num):
    number = input_num
    factor = 10
    components = []
    while number > 0:
        remainder = number % factor
        if remainder != 0:
            components.append(remainder)
        number -= remainder
        factor *= 10
    components.reverse()
    return " + ".join([str(component) for component in components])

# Test cases
print(expanded_form(12)) # should return '10 + 2'
print(expanded_form(42)) # should return '40 + 2'
print(expanded_form(70304)) # should return '70000 + 300 + 4'



"""
Q18:
Write a function, persistence, that takes in a positive parameter
`num` and returns its multiplicative persistence, which is the number
of times you must multiply the digits in `num` until you reach a single digit.

P:
Given a number, return the number of times to multiply the digits until we reach a single digit.

Rules:
    - Input will be a positive number
    - If input is already a single digit, return 0

Data structures:
    - Input: Integer
    - Output: Integer
    - Intermediary:
        - List: Store individual digits
        - Integer:
            - Keep track of number of iterations
            - Keep track of latest result after multiplying
        - Boolean: Is latest result one digit? Yes/no

High-level ideas:
    - Create a list of digits. Multiply digits and check if result only consists of one digit. Repeat until we get one digit, iterating a counter as we continue. Return counter at the end

A:
    - Set variable 'result' to the input
    - Set 'counter' to 0
    - Repeat until 'result' is one digit (less than 10):
        - Coerce 'result' into a string
        - Create a list of digits out of the string => 'digits'
        - Set variable 'product' to 1
        - For each element of 'digits'
            - Multiply 'product' by int version of element
        - Set 'result' to 'product'
        - Iterate 'counter' by 1
    - Return 'counter'

"""

def persistence(number):
    result = number
    counter = 0
    while result >= 10:
        digits = list(str(result))
        product = 1
        for digit in digits:
            product *= int(digit)

        result = product
        counter += 1

    return counter


# Examples:
print(persistence(39)) # should return 3, because 3*9=27, 2*7=14, 1*4=4
# and 4 has only one digit
print(persistence(999)) # should return 4, because 9*9*9=729, 7*2*9=126,
# # 1*2*6=12, and finally 1*2=2
print(persistence(4)) # should return 0, because 4 is already a one-digit number
print(persistence(25)) # should return 2, because 2*5=10, and 1*0=0




"""
Q20:
Write a function that takes a string as an argument and groups the
number of times each character appears in the string as a dictionary
sorted by the highest number of occurrences.

The characters should be sorted alphabetically, and you should ignore
spaces, special characters, and count uppercase letters as lowercase ones.
"""

def get_char_count(string):
    counts = {}
    for char in string:
        if char.isalnum():
            lowercase_char = char.lower()
            counts[lowercase_char] = counts.get(lowercase_char, 0) + 1
    
    unique_counts = list(set(counts.values()))
    unique_counts.sort(reverse=True)
    values = {}
    for count in unique_counts:
        values[count] = sorted([key for key, value in counts.items()
                                    if value == count])
    print(values)
    

# Test cases
# get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
# get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
# get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
# get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
# get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}




"""
Q22:
Write a function `scramble(str1, str2)` that returns `True` if a portion of
`str1` characters can be rearranged to match `str2`, otherwise returns `False`.

Notes:
- Only lower case letters will be used (a-z). No punctuation or digits will
    be included.


P:
Given two strings, str1 and str2, return True if a portion of str1 can be used to create str2. False otherwise.

Rules:
    - str1 can have more characters than str2 but must have all of str2's characters to return True
    - Inputs will only have lowercase characters, no punctuation or digits


E:
'rkqodlw', 'world'
'kq' => True

'edewaassoqqy', 'carrot' => True

'kaa', 'steak'
    - No 'e', return False

Data structures:
    - Input: two strings
    - Output: boolean
    - Intermediary
        - List: List of characters in both strings, mutate lists as we find characters
        - Dictionary: Check that the chars and counts in dict from str2 are included with sufficient count in dict from str1

High-level ideas:
    - Create a list out of str1 ('list1'). For each char in str2, if char is in list1, remove from the list. If not, return False. If we successfully iterate, return True
    - Create a dictionary out of str1 and str2 (dict1 and dict2). For each char in dict1, get the counts from dict1 and dict2. If dict1 count is < dict2 count, return False. Else, if successful full way through, return True

A:
    - Create 'list1' out of chars of str1
    - Iterate through chars of str2:
        - If char is in 'list1'
            - Remove from 'list1', mutating in process
        - Else:
            - Return False
    - If all successful, return True

"""

def scramble(str1, str2):
    list1 = list(str1)
    
    for char in str2:
        if char in list1:
            list1.remove(char)
        else:
            return False
    
    return True


# Test cases
print(scramble('rkqodlw', 'world')) # should return True
print(scramble('cedewaraarossoqqyt', 'carrot')) # should return True
print(scramble('katas', 'steak')) # should return False
print(scramble('scriptjava', 'javascript')) # should return True
print(scramble('scriptingjava', 'javascript')) # should return True



"""
Q23:
Write a function `longest(s)` that finds and returns the longest substring of
`s` where the characters are in alphabetical order.

P:
Given a string 's', return the longest substring for which characters are in alphabetical order.

Rules:
    - A substring can be 1 or more chars
    - If there are multiple longest substrings, return the substring that we encounter "first"
        - First means starting char with the lowest index in the input
    - alphabetical order also means that characters can repeat
        - i.e. 'aa' counts as being in alphabetical order
    - If input is only one character, return the input
    - Assume that input is a lowercase alphabetical string


E:
'abcdeapbcdef'
    - 'abcde'
    - 'ap'
    - 'bcdef'

'asdfbyfgiklag'
    - 'as'
    - 'df'
    - 'by'
    - 'fgikl'
    - 'ag'


Data structures:
    - Input: String
    - Output: String (substring)
    - Intermediary:
        - List: Store all substrings / valid substrings
        - String: 
            - Build a valid substring as we iterate through input
            - Alphabet reference

High-level ideas:
    - Iterate through input. Build a series of substrings where each character comes after a prior character in the alphabet. For all valid substrings, find the longest substring and return. If multiple substrings match length, return the first one we found.


A:
    - Create constant var ALPHABET with value 'abcdefghijklmnopqrstuvwxyz'
    - *get_valid_substrings* => Input: input str, Output: 'substrings'
    - Sort 'substrings' from longest to smallest length (mutate)
    - Return the first element of 'substrings'


*get_valid_substrings*
    Input: String
    Output: List of substrings
    Algo:
        - Create an empty list 'substrings'
        - Create an empty string 'current_substring'
        - For each character in the input:
            - If 'current_substring' is not empty:
                - Compare character to last char in 'current_substring'
                - If index of char is < than index of last char in 'current_substring':
                    - Add 'current_substring' to the end of 'substrings'
                    - Reset 'current_substring' to empty string
                    - Add character to end of 'current_substring'
            - Add char to end of 'current_substring'
        - Add 'current_substring' to the end of 'substrings'
        - Return 'substrings'
"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def get_valid_substrings(string):
    substrings = []
    current_substring = ''
    for char in string:
        if current_substring:
            current_idx = ALPHABET.index(char)
            prior_idx = ALPHABET.index(current_substring[-1])
            if current_idx < prior_idx:
                substrings.append(current_substring)
                current_substring = ""
        current_substring += char
    substrings.append(current_substring)
    return substrings


def longest(string):
    substrings = get_valid_substrings(string)
    substrings.sort(key=len, reverse=True)
    return substrings[0]

# Test cases
print(longest('asd'))                  # should return 'as'
print(longest('nab'))                  # should return 'ab'
print(longest('abcdeapbcdef'))         # should return 'abcde'
print(longest('asdfaaaabbbbcttavvfffffdf')) # should return 'aaaabbbbctt'
print(longest('asdfbyfgiklag'))        # should return 'fgikl'
print(longest('z'))                    # should return 'z'
print(longest('zyba'))                 # should return 'z'


"""
Reflection:
Time: 23 min 32 seconds. Took a while because the algo took me a bit to figure out.
"""


"""
Q25:
# Pete is baking cakes and needs help calculating how many he can make with his recipes and available ingredients.
# Write a function cakes() that takes two dictionaries: the recipe and the available ingredients. Return the maximum number of cakes Pete can bake.

# Rules:
# - Ingredients not present in the objects can be considered as 0.


P:
Given a recipe and available ingredients, return the number of cakes we can make.

Rules:
    - If an ingredient is not in either dict, assume its value is 0
    - We can have empty dictionaries


Recipe: 500 flour, 200 sugar, 1 eggs
available: 1200 flour, 1200 sugar, 5 eggs, 200 milk
    - 1200 vs 500 => 2x => we can bake 2 cakes
    - 1200 vs 200 => 6x
    - 5 vs 1 => 5x

Recipe: 200 cream, 300 flour, 150 sugar, 100 milk, 100 oil
available: 5000 cream, 20000 flour, 1700 sugar, 20000 milk, 30000 oil
    - 5000 vs 200 => 25x
    - 20000 vs 300 => 66x
    - 1700 vs 150 => 11x => we can bake 11 cakes
    - 20000 vs 100 => 200x
    - 30000 vs 100 => 300x


Data structures:
    - Input: 2 dictionaries
    - Output: Integer (# of cakes)
    - Intermediary:
        - List: Keep track of how many multiples we have of each ingredient

High-level ideas:
    - For each ingredient in recipe, find the amount we need vs amount we have. If we don't have enough, return 0. Else, keep track of the smallest "multiple" we have and return.

A:
    - Set variable 'lowest_multiple' to None
    - For each ingredient in recipe:
        - Get the amount we need from recipe => 'needed'
        - Get the amount we have => 'on_hand'
        - Divide 'on_hand' by 'needed', get integer component of result => 'current_multiple'
        - If 'current_multiple' is 0:
            - Return 0
        - If we don't have 'lowest_multiple' or 'current_multiple' < 'lowest_multiple':
            - Set 'lowest_multiple' to 'current_multiple'
    - Return 'lowest_multiple'

"""

def cakes(recipe, available):
    lowest_multiple = None
    for ingredient in recipe:
        needed = recipe.get(ingredient, 0)
        on_hand = available.get(ingredient, 0)
        
        current_multiple = on_hand // needed
        if current_multiple == 0:
            return 0
        
        if not lowest_multiple or current_multiple < lowest_multiple:
            lowest_multiple = current_multiple
    
    return lowest_multiple


# Test cases
# must return 2
print(cakes({"flour": 500, "sugar": 200, "eggs": 1},{"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) == 2)

# must return 11
print(cakes({"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream": 5000}) == 11)

# must return 0
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000, "milk": 2000}) == 0)

# must return 0
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000, "milk": 2000, "apples": 15, "oil": 20}) == 0)

# must return 0
print(cakes({"eggs": 4, "flour": 400},{}) == 0)

# must return 1
print(cakes({"cream": 1, "flour": 3, "sugar": 1, "milk": 1, "oil": 1, "eggs": 1},{"sugar": 1, "eggs": 1, "flour": 3, "cream": 1, "oil": 1, "milk": 1}) == 1)



"""
Q31:

Find the highest scoring word in a string.
Each letter scores points based on its position in the alphabet: a = 1, b = 2, c = 3, ... z = 26.
Return the highest scoring word. If two words score the same, return the word that appears earliest in the string.

P:
Given a string of words, return the word with the highest score.

Rules:
    - "Score" is based off of the sum of the scores of each letter, based on the letter's position in the alphabet
    - If 2 words have the same score, return the word that appears first
    - Input string will always have lowercase alphabetical characters
    - "Word" is defined as alpha strings separated by one space

E:
'man i need a taxi up to ubud'
    - 'man' => 13 + 1 + 14 = 28
    - 'i' => 9
    - 'need' => 14 + 5 + 5 + 4 = 28
    - 'a' => 1
    - 'taxi' => 20 + 1 + 24 + 9 = 54
    - 'ubud' => 21 + 2 + 21 + 4 = 48

Data structures:
    - Input: string
    - Output: String (substring)
    - Intermediary:
        - List: Store words
        - String: Store positions in alphabet
        - Dictionary: Key = word, value = score

High-level ideas:
    - Create a list of words from our input string. For each word, find its score and insert word and score into a dictionary. Find the word with the highest score and return. If more than one word with highest score, return the first word we saw.

A:
    - Create constant variable ALPHABET 'abcdefghijklmnopqrstuvwxyz'
    - Create a list 'words' from input string
    - *get_scores* => Input: 'words', output: 'scores'
    - Sort items in 'scores' from highest to lowest
    - Return the first resulting item in sorted list

*get_scores*
    Input: List of strings
    Output: Dictionary
    Algo:
        - Create empty dictionary 'word_scores'
        - For each word in input list:
            - Create a list of characters from word => 'chars'
            - Transform 'chars' into scores => 'scores'
                - Score = position of char in ALPHABET + 1
            - Sum 'scores'
            - Add new key-value pair to dictionary. Key = word, value = sum of 'scores'
        - Return 'word_scores'

"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def get_scores(str_list):
    word_scores = dict()
    for word in str_list:
        chars = list(word)
        scores = [ALPHABET.index(char) + 1 for char in chars]
        word_scores[word] = sum(scores)
    return word_scores


def high(text):
    words = text.split()
    scores = get_scores(words)
    
    sorted_words = sorted(scores.keys(), key=lambda key: scores[key], reverse=True)

    return sorted_words[0]


# get_scores(['man', 'i', 'need', 'a', 'taxi', 'up', 'to', 'ubud'])

print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano') == 'volcano')
print(high('take me to semynak') == 'semynak')
print(high('aaa b') == 'aaa')


"""
Reflection:
Time: 20 min 30 sec. Not too bad, but faltered a bit at the sorting stage as I panicked a bit.
"""



"""
Q35:
# Given an integer n, find the maximal number you can obtain by deleting
# exactly one digit of the given number.

P:
Given an integer, find the largest resulting number if we delete exactly one digit.

Rules:
    - Remove exactly one digit at a time
    - We will always get an input of 2 or more digits


E:
152
    - 52, 12, 15 => max is 52

1001
    - 1, 101, 101, 100 => max is 101


Data structures:
    - Input: Integer
    - Output: Integer
    - Intermediary:
        - List: 
            - Store all possible results
            - Storing individual digits of the input string
        - String: Work with individual digits


High-level ideas:
    - Turn input into a string. Create new numbers based on removing each digit from the string, one digit at a time, and store in a list. Find the max number of the resulting list and return.

A:
    - Convert input to string => 'input_str'
    - Create empty list 'candidates'
    - For each element of 'input_str'
        - Create list 'digits' from 'input_str'
        - Mutate 'digits' by removing current element
        - Combine 'digits' into str, convert str to int, add to 'candidates'
    - Return the max number in 'candidates'

"""

def delete_digit(number):
    input_str = str(number)
    candidates = []
    for ele in input_str:
        digits = list(input_str)
        digits.remove(ele)
        candidates.append(int(''.join(digits)))
    return max(candidates)


# Test cases
print(delete_digit(152) == 52)
print(delete_digit(1001) == 101)
print(delete_digit(10) == 1)



"""
Q37:
# The goal of this exercise is to convert a string to a new string where each character in the new string 
# is "(" if that character appears only once in the original string, or ")" if that character appears 
# more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

P:
Given a string, create a new string that replaces characters with ( if they only appear once or ) if they appear more than once, ignoring case.

Rules:
    - Case-insensitive
    - We can have non-alphabetical characters as well
    - Include ) in all locations of repeated character

Data structures:
    - Input: string
    - Output: string
    - Intermediary:
        - List: Store individual characters
        - Dictionary: Key = chars (lowercased), value = counts
        - String: Build the output step by step

High-level strategies:
    - Create a dictionary where key = lowercased char, value = count in input. Create an empty string. For each char in the input string, if its value > 1 in the dictionary, add a ")" to the new string, otherwise add an "(". Return the new string.

A:
    - Create dictionary out of input => *get_value_counts*, output = 'counts'
    - Create empty string 'transformed'
    - For each char in input string
        - Convert to lowercase
        - Check its value in 'counts'
        - If value > 1:
            - Add ')' to end of 'transformed'
        - Else:
            - Add '(' to end of 'transformed'
    - Return 'transformed'

*get_value_counts*
    Input: String
    Output: Dictionary
    Algo:
        - Create empty dict 'counts'
        - For each char in input:
            - Create 'lowercase_char'
            - If 'lowercase_char' not in 'counts', add it
            - Increment 'lowercase_char' value by 1
        - Return 'counts'

"""

def get_value_counts(string):
    counts = dict()
    for char in string:
        lowercase_char = char.lower()
        counts[lowercase_char] = counts.get(lowercase_char, 0) + 1
    return counts

def duplicate_encode(string):
    counts = get_value_counts(string)
    transformed = ''
    for char in string:
        value_count = counts[char.lower()]
        if value_count > 1:
            transformed += ")"
        else:
            transformed += "("
    return transformed

# Test cases
print(duplicate_encode("din") == "(((")
print(duplicate_encode("recede") == "()()()")
print(duplicate_encode("Success") == ")())())")
print(duplicate_encode("(( @") == "))((")


"""
Q38:
# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols and return the final state of the string.

P:
Given a string, iterate through and remove the right most character of a string at any given time if we see "#". Return the final version of the string.

Rules:
    - When we see a #, remove the most recently added character
    - Assume our string will only have alphabetical and # characters
    - If we have an empty string and see a #, do nothing

a#bc#d
'a' => '' => 'b' => 'bc' => 'b' => 'bd'

'abc#d##c'
'a' => 'ab' => 'abc' => 'ab' => 'abd' => 'ab' => 'a' => 'ac'

'abc####d##c#'
''

Data structures:
    - Input: string
    - Output: string
    - Intermediary:
        - List: Keep track of current state of output as we build it up

High-level strategies:
    - Iterate through input string. If char is not #, add to a list. If char is #, remove last element added to list. Once done iterating, combine elements in list into a string and return.

A:
    - Create empty list 'current_sequence'
    - For char in input string
        - If char is not a #
            - Add char to end of 'current_sequence'
        - Otherwise
            - If 'current_sequence' has elements:
                - Remove last element added to 'current_sequence'
    - Create one string out of elements of 'current_sequence'
    - Return resulting string

"""

def clean_string(sequence):
    current_sequence = []
    for char in sequence:
        if char != "#":
            current_sequence.append(char)
        else:
            if current_sequence:
                current_sequence.pop()
    return ''.join(current_sequence)    

# Test cases
print(clean_string('abc#d##c') == "ac")
print(clean_string('abc####d##c#') == "")



"""
Q42:
# Mothers arranged a dance party for the children in school. At that party,
# there are only mothers and their children. All are having great fun on the
# dance floor when suddenly all the lights went out. It's a dark night and no
# one can see each other. But you were flying nearby and you can see in the
# dark and have ability to teleport people anywhere you want.
# Legend:
# - Uppercase letters stands for mothers, lowercase stand for their children,
# i.e. "A" mother's children are "aaaa".
# - Function input: String contains only letters, uppercase letters are unique.

P:
Given a string, rearrange such that upper and lowercase chars of the same letter are grouped together, starting with upper, and such that all characters are in alphabetical order.

Rules:
    - Uppercase characters stand for moms, lowercase for children
    - String only contains letters
    - Uppercase letters will be unique
    - Empty input means empty output
    - If there is a child, there will be a parent. No orphans


"abBA"
- "Aa", "Bb" => "AaBb"

"AaaaaZazzz"
- "Aaaaaa", "Zzzz" => "AaaaaaZzzz"

"CbcBcbaA"
- "Ccc", "Bbb", "Aa" => "AaBbbCcc"

Data structures:
    - Input: String
    - Output: String (alphabetic order + upper followed by lower)
    - Intermediary:
        - List: Each group of letter (upper and lower) as elements
        - String: Groups themselves
        - Set: Unique lowercase letters
        - Dictionary: Key = lowercase letters only, Value = counts

High-level ideas:
    - Create a dictionary counting the number of children for each unique letter. For each unique letter, form substrings with a parent, followed by the number of children present, and insert into a list. Sort list alphabetically and combine into output string.

A:
    - If input is empty, return empty string
    - Create a dictionary of children => *get_children_counts*
    - Create empty list 'groups'
    - For child in dictionary:
        - Create a new string with parent (uppercase) followed by # of children specified by value of key
        - Add string to end of 'groups'
    - Sort 'groups' alphabetically from A-Z, mutating
    - Combine 'groups' into one string and return


*get_children_counts*
    Input: String
    Output: Dictionary
    Algo:
        - Create empty dictionary 'counts'
        - For each char in string:
            - If lowercase (it is a child):
                - Add child to 'counts' if not there
                - Increment value of key by 1
        - Return 'counts'
"""

def get_children_counts(string):
    counts = dict()
    for char in string:
        if char.islower():
            counts[char] = counts.get(char, 0) + 1
    return counts

def find_children(string):
    if not string:
        return ""
    
    children = get_children_counts(string)
    groups = []

    for child in children:
        num_children = children[child]
        family = child.upper() + child * num_children
        groups.append(family)

    groups.sort()

    return ''.join(groups)

print(find_children("abBA") == "AaBb")
print(find_children("AaaaaZazzz") == "AaaaaaZzzz")
print(find_children("CbcBcbaA") == "AaBbbCcc")
print(find_children("xXfuUuuF") == "FfUuuuXx")
print(find_children("") == "")



"""
Q43:
# Some numbers have funny properties. For example:
# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given a positive integer n written as abcd... (a, b, c, d... being digits)
# and a positive integer p we want to find a positive integer k, if it exists,
# such as the sum of the digits of n taken to the successive powers of p is
# equal to k * n.
# In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...)
# = n * k
# If it is the case we will return k, if not return -1.
# Note: n and p will always be given as strictly positive integers.


P:
Given a positive integer "n" and a positive integer "p", find a positive integer "k" such that the sum of "n"'s digits, respectively raised to the power "p", "p+1", etc. would equal "n" * "k". 

Rules:
    - If not possible, k should be -1
    - n and p will always be positive integers

89, 1 => 8^1 + 9^2 = 89 => 89 / 89 = 1 (k)

92, 1 => 9^2 + 2^2 = 85 => 85 / 92 not whole number, k = -1

46288, 3 => 4^3 + 6^4 + 2^5 + 8^6 + 8^7 = 2360688 / 46288 = 51 (k)

695, 2 => 6^2 + 9^3 + 5^4 = 1390 / 695 = 2 (k)

Data structures:
    - Input: Int
    - Output: integer
    - Intermediate:
        - String: Handle digits
        - List: Store each digit
        - Integer: Start at "p", increment by 1

High-level idea:
    - Convert input "n" to string and store digits in a list. For each digit, convert back to int and raise to the power of "p". Increment "p" by 1 and repeat the process until we finish working with all digits. Sum the resulting values. If sum can be divided by "n" an even number of times, return that result, otherwise return -1.

A:
    - *compute_powers* => Input: n, p; Output: 'powers'
    - Sum elements of 'powers' => 'sum_powers'
    - If no remainder when dividing 'sum_powers' by 'n':
        - Integer divide 'sum_powers" by 'n' => 'k'
        - Return 'k'
    - Else:
        - Return -1


*compute_powers*
    Input: 2 integers (n and p)
    Output: List of integers
    Algo:
        - Create list 'digits'
            - Convert input "n" to str
            - Create list from the string
        - Create empty list 'powers'
        - For digit in digits:
            - Convert digit to int
            - Calculate digit ^ p, add result to end of 'powers'
            - Increment 'p' by 1
        - Return 'powers'

"""

def compute_powers(n, p):
    digits = list(str(n))
    powers = []
    for digit in digits:
        powers.append(int(digit) ** p)
        p += 1
    return powers

def dig_pow(n, p):
    powers = compute_powers(n, p)
    sum_powers = sum(powers)
    
    if sum_powers % n == 0:
        k = sum_powers // n
        return k
    else:
        return -1



# print(compute_powers(89, 1))

# # Test cases
print(dig_pow(89, 1) == 1)
print(dig_pow(92, 1) == -1)
print(dig_pow(46288, 3) == 51)
print(dig_pow(695, 2) == 2)