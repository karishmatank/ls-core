# Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two words.

def penultimate(string):
    words = string.split()
    return words[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

# To retrieve the middle word of a sentence:
# Edge cases:
#     - No words
#     - One word
#     - Even number of words

def middle_word(string):
    words = string.split()
    if not words or len(words) == 1:
        return string
    
    if len(words) % 2 == 0:
        # Let's say that we'll just return the index of len(words) / 2 - 1
        index = int(len(words) / 2) - 1
    else:
        index = len(words) // 2
    return words[index]

# These examples should print True
print(middle_word("last word"))
print(middle_word("Launch School is great!"))
print(middle_word("Launch School is so great!"))