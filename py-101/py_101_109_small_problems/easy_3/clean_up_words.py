# Given a string that consists of some words and an assortment of non-alphabetic characters, 
# write a function that returns that string with all of the non-alphabetic characters replaced by spaces. 
# If one or more non-alphabetic characters occur in a row, you should only have one space in the result
# (i.e., the result string should never have consecutive spaces).

def clean_up(string):
    cleaned_up_str = ""
    for index in range(len(string)):
        if string[index].isalpha():
            cleaned_up_str += string[index]
        elif not cleaned_up_str or not cleaned_up_str.endswith(" "):
            cleaned_up_str += " "
        
    return cleaned_up_str

print(clean_up("---what's my +*& line?") == " what s my line ") # True