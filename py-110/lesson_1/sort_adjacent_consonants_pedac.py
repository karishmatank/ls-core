"""
Problem statement (provided):
Given a list of strings, sort the list based on the highest number of adjacent consonants a string contains 
and return the sorted list. If two strings contain the same highest number of adjacent consonants, 
they should retain their original order in relation to each other. Consonants are considered adjacent if they 
are next to each other in the same word or if there is a space between two consonants in adjacent words.

**** Step 1: Understand the problem ****
Input: List of strings
Output: List of strings (sorted)
Problem requirements:
    - Explicit:
        - The list should be sorted based on highest number of adjacent consonants
        - If two strings have the same number of adjacent consonants, retain their order vs each other
            - If one of those strings is at a lower index value than the other, that order should be retained
        - Adjacent means two consonants next to each other or with a space in between
    - Implicit:
        - For each string in a list, we'll need to find the longest string length of just consonants
            - This will require stripping out space characters and potential others such as punctuation
        - Adjacency requires 2 or more consonants together. If a string has max 1 consonant in a row, that doesn't mean 
          that we count the number of adjacent consonants as 1. That's effectively treated the same as having no consonants 
          in the entire string

Questions:
    - Is consonant defined as any alphabetical character not a, e, i, o or u? What about y?
    - How is punctuation treated? Does that break a string of consonant characters?
    - Similarly, how should we treat numbers?
    - Should we be handling non English characters as well?
    - Does case matter? Uppercase vs lowercase?
    - Should the program return an empty list if it is fed an empty list?

**** Step 2: Examples and test cases ****
    - Test case 1 was helpful- I would have thought that 'baa' would come before 'aa', but I realize now that both
      don't have real sequences of adjacent consonants, so this helps me refine my thinking. It's not just about
      # of consonants, which was sort of my thought process before, but rather thinking about adjacent.
        - Reflected step 1 to incorporate this
    - No real clarity on my other questions though

**** Step 3: Data structures ****
There's two potential ways I can think of for now:
    - Store the string and the # of adjacent consonants in a list of tuples, allowing the data to be grouped together
        - Tuple for the individual elements so that we don't accidentally mutate the data after adding it to the list 
        - We would then need to sort our original list based on the integer count within the tuple
    - Use a dictionary to map each key, or string from the list, to its max adjacent consonant length, and use that
      to sort the items of the dictionary to then return the list of sorted strings

**** Step 4: Algorithm ****
1. Start with the input list, which we will refer to as such
2. Define an empty dictionary
2. For each word in the input list, find the length of the longest adjacent consonant string. Add this data to the
   dictionary
3. Sort the dictionary items based on longest to shortest length.
    a. sorted() maintains insertion order
4. Return a list of keys, sorted as per step 3

Step 2 is pretty vague, so we'll separate that into its own mini problem:
    - Problem statement: Find the length of the longest adjacent consonant string
    - Input: String, dictionary object
    - Output: None, mutates the dictionary object
    - Algorithm:
        1. Assign a counter variable to 0 and a longest_counter variable to 0
        2. For each character in the input string:
            a. Increment counter if character is not a, e, i, o, or u
            b. If character is a, e, i, o, or u:
                i. Assign longest_counter to counter value if counter > longest_counter
                ii. Reset counter back to 0
            c. If character is a space, keep going, don't do anything
        3. Mutate the dictionary object passed by object reference to add in a new key-value pair
            a. Key = string
            b. Value = value of counter if greater than 1, otherwise 0

"""

def find_longest_string(string, longest_lengths):
    counter = 0
    longest_counter = 0
    for char in string:
        if not char.isalpha():
            continue
        elif char.lower() in ['a', 'e', 'i', 'o', 'u']:
            longest_counter = max(counter, longest_counter)
            counter = 0
        else:
            counter += 1
    
    longest_counter = max(counter, longest_counter)
    
    if longest_counter > 1:
        longest_lengths[string] = longest_counter
    else:
        longest_lengths[string] = 0


def sort_by_consonant_count(str_list):
    longest_lengths = {}
    for string in str_list:
        find_longest_string(string, longest_lengths)
    sorted_list = sorted(longest_lengths.items(), key=lambda x: x[1], reverse=True)
    return [key for key, _ in sorted_list]


# Test cases
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']