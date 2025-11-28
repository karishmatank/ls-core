# Use map to create a list of lengths of each string in the original list.

strings = ['a', 'bee', 'cello', 'dog', 'ears']
string_lengths = list(map(lambda string: len(string), strings))
print(string_lengths)

# Alternate is to just use len, don't have to pass in your own lambda!
# string_lengths = list(map(len, strings))