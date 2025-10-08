"""
Problem (as provided):

Write a function that takes a floating point number representing an angle between 0 and 360 degrees 
and returns a string representing that angle in degrees, minutes, and seconds. 
You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, 
and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:
DEGREE = "\u00B0"

P:
Input: Float
Output: String
Rules:
    - Explicit:
        - Input represents an angle between 0 and 360
        - Output represents that angle in degrees, minutes and seconds
        - Use the degree symbol to represent degrees, single quote for minutes, double quote for seconds
        - 60 minutes in a degree
        - 60 seconds in a minute
    - Implicit:
        - Degrees represents the non-decimal part of the provided float (i.e. if we are provided 1.1, we would
          have a degree of 1, representing the whole number of that provided float)
        - The minutes and seconds refer to the decimal portion. If the decimal is .1, it looks like minutes and seconds 
          represent .1 of an hour
        - If we receive an input of 0, we should return 0 degrees, 0 seconds, and 0 minutes
        - We also need to use the escape character at the very end for the double quote
        - It looks like 360 is an edge case, where we can either return 0 degrees 0 min 0 sec or 360 degrees 0 min 0 sec
          I will return 360 degrees, 0 min, 0 sec in this case
        - There may be other edge cases related to rounding, as demonstrated by the 3rd test case
        - If we calculate a seconds figure that is not a whole number, we should round to the nearest integer.
            - i.e. if input is 93.034773, we have 93 degrees, 2 minutes, and we get 5.1828 seconds, which rounds down to 5
        - (I completely missed on the first go around that we have to zero pad if the result for any of 
           degrees, minutes, and seconds is one digit. EDIT: Missed yet again that degrees is not padded!)
        - (Also completely missed that if seconds ends up equal to 60, we need to add to minutes and change seconds to 0)

Questions:
    - Can you clarify what exactly you mean by representing an angle as degrees, minutes, and seconds?

E:
    - Clarified my understanding via my first question

D:
We'll definitely need to use floats, given that's the input, as well as strings, given that's the output.
We'll be working with integers too.

A:
    1. Take as input a float or int
    2. If we get an integer, we can return the required string with the input as degrees, 0 minutes, 0 seconds
        a. This fits in as well if we have an input of 360
    3. If float, extract the non-decimal part from the float to get the integer to the left of the decimal
    4. For the remaining decimal portion, multiply by 60
    5. From the result from step 4, extract out the part of the float to the left of the decimal
    6. For the remaining decimal portion again, multiply by 60 to get seconds. Round to nearest integer
    7. If seconds is 60, we'll need to add a minute to our calculated minutes and reassign our seconds variable to 0
    8. Craft the return string using the necessary symbols. We'll need to zero pad the numbers to get to 2 digits
    9. Return the string from step 8

"""

DEGREE = "\u00B0"

def dms(angle):
    if angle % 1 == 0:
        degrees = angle
        minutes = 0
        seconds = 0
    else:
        degrees = int(angle)
        min_and_sec = (angle - degrees) * 60
        minutes = int(min_and_sec)
        sec = min_and_sec - minutes
        seconds = round(sec * 60)

        if seconds == 60:
            seconds = 0
            minutes += 1

    return f"{degrees}{DEGREE}{minutes:02}'{seconds:02}\""


# Test cases
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")