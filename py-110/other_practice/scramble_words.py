"""
SPOT wiki Q9: 
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