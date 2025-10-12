"""
As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. 
If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, 
the time is before midnight.

Write two functions that each take a time of day in 24 hour format, 
and return the number of minutes before and after midnight, respectively. 
Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.

P:
Input: String representing 24-hour format time of day
Output: Integer representing minutes
Rules:
    - Explicit
        - There are two functions we're creating here, one of which returns the minutes before midnight, the other the minutes
        after midnight
        - The output will be in the range of 0 through 1439, inclusive
    - Implicit
        - The input will have a format of hours, followed by a colon, followed by minutes, each padded to two digits
        - If the input is at midnight, we should return the integer 0
        - If the input is at "24:00", we should also return the integer 0
        - Assume input won't have hours > 24 or minutes > 59. If hours == 24, assume minutes will be 0

D: Strings

A:
    - Separate out the input into hours and minutes and coerce each to an integer
    - Assign a variable 'total_min' to 0
    - If we are calculating time after midnight:
        - Convert time to minutes (see below). Assign to variable 'total_min'
        - Return the remainder of 'total_min' after dividing by 1440 (24 * 60) to ensure we don't return 1440 accidentally
    - If we are calculating time before midnight:
        - Convert time to minutes (see below). Assign to variable 'total_min'
        - Subtract total_min from 1440 (24 * 60) and return the remainder of that value after dividing by 1440

Subalgorithm: Convert time to minutes
Input: Integers (hours and minutes)
Output: Integer (total minutes)
Algorithm:
    - Convert hours to minutes by multiplying by 60. Add to 'total_min'
    - Add minutes to 'total_min'
    - Return 'total_min'
"""

MINUTES_PER_DAY = 1440

def calculate_minutes(hours, minutes):
    return hours * 60 + minutes

def after_midnight(hr_min_str):
    hours, minutes = [int(result) for result in hr_min_str.split(":")]
    total_min = calculate_minutes(hours, minutes)
    return total_min % MINUTES_PER_DAY

def before_midnight(hr_min_str):
    hours, minutes = [int(result) for result in hr_min_str.split(":")]
    total_min = calculate_minutes(hours, minutes)
    return (MINUTES_PER_DAY - total_min) % MINUTES_PER_DAY



# Test cases
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True