"""
P: 
Given an integer, convert it to a Roman numeral string.

Rules:
    - To create the full Roman numeral, we get each digit from the integer from left to right and represent that digit + its place
      as a Roman numeral
    - Roman numerals include I (1), V (5), X (10), L (50), C (100), D (500), M (1000)
    - To create a Roman numeral per digit, we combine the Roman numerals above
        - If this would require 4 of the same Roman numeral in a row, replace with a lower value numeral
          placed before a higher value numeral, which signals "subtraction"
        - i.e. we don't write VIIII for 9, we write IX (1, 10 => 10 - 1 = 9)
    - We do not need to worry about converting numbers larger than 3000
    - We can ignore digits that are 0

E:
1990 => 1000 + 900 + 90 + 0 (ignore 0s) = M + CM + XC = MCMXC
    - 1000 matches M
    - 900 can be further split into 500 + 100 + 100 + 100 + 100. That's 4 100s in a row
        - Instead we go to the next highest digit and subtract => 1000 - 100. Switch the order to get CM
    - 90 can be split into 50 + 10 + 10 + 10 + 10 or 100 - 10 => XC
2008 => 2000 + 8 => MM + VIII = MMVIII
163 => 100 + 60 + 3 => C + LX + III = CLXIII

D:
    Input: Integer (instance variable in class RomanNumeral)
    Output: String (Roman numerals)
    Intermediary:
        - Dictionary: 
            - Keys are Roman num strings, values are integer values
            - Keep track of how many Roman num it takes to build an integer
        - List: Individual digits of the input / decomposition of input into its "parts"
        - Integer: Remainder after subtracting Roman numeral values from each "part", aid in building Roman numeral per "part"

High-level strategies:
    - Decompose the input into its parts based on digits + place. Build Roman numeral string for each part by finding the
      highest Roman numeral value divisible into the part and subtracting that value from the part, repeating until we are 
      left with 0. Combine all Roman numeral strings into one and return.

A:
    - Class constant `ROMAN_MAP`-> dict with keys Roman numerals and values as their integers
        - Include values of combinations where you would otherwise have to use 4 chars in a row
    - Constructor (__init__)
        - Create instance variable `integer`
    - `to_roman` method
        - Decompose input into its parts => *decompose*
        - Create empty string `result`
        - For each part:
            - Set remainder to part
            - For Roman numerals from largest to smallest:
                - Break if remainder is 0
                - Floor divide remainder by Roman numeral => `freq`
                - Add `freq` number of the Roman numeral to `result`
                - Subtract remainder by Roman num value * `freq`
        - Return `result`

*decompose*
    Input: Instance variable `integer`
    Output: List of ints
    Algo:
        - Turn input into a string and split into list of digits => `digits`
        - Set factor to 1
        - For each digit from right to left
            - Multiply digit by factor
            - Multiply factor by 10
        - Return `digits`

"""

class RomanNumeral:
    ROMAN_MAP = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    def __init__(self, num):
        self.number = num

    def to_roman(self):
        parts = self.decompose()
        
        result = ""
        for part in parts:
            remainder = part
            for roman_numeral, value in RomanNumeral.ROMAN_MAP.items():
                if remainder == 0:
                    break

                freq = remainder // value
                result += roman_numeral * freq
                remainder -= value * freq
        
        return result
    
    def decompose(self):
        digits = [int(digit) for digit in list(str(self.number))]
        
        factor = 1
        for idx in range(len(digits)):
            digits[-idx - 1] *= factor
            factor *= 10

        return digits
    
"""
Reflection:
I ended up wasting time doing the initial decomposition, when I really didn't need it.
I could have just kept in the remainder computing process, which would have done the decomposition at the same time.
That would have saved a for loop.
"""