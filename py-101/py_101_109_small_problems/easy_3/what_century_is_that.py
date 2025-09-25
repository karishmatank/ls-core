# Write a function that takes a year as input and returns the century. 
# The return value should be a string that begins with the century number, 
# and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

def get_suffix(century):
    if 11 <= century % 100 <= 19:
        return "th"

    ending_digit = century % 10
    match ending_digit:
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
        case _:
            return "th"

def century(year):
    century = year // 100 if year % 100 == 0 else year // 100 + 1
    return f"{century}{get_suffix(century)}"

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
