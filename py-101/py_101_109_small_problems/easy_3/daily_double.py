# Write a function that takes a string argument and returns a new string 
# that contains the value of the original string with all consecutive duplicate 
# characters collapsed into a single character.

def crunch(string):
    if not string:
        return string
    
    new_string = [string[0]]
    for index in range(1, len(string)):
        if string[index] != string[index - 1]:
            new_string.append(string[index])
    return ''.join(new_string)

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')