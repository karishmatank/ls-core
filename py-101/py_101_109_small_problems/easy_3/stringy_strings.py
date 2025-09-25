# Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, 
# always starting with a '1'. The length of the string should match the given integer.

def stringy(string_len):
    result = ""
    for index in range(0, string_len):
        if index % 2 == 0:
            result += "1"
        else:
            result += "0"
    return result

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True