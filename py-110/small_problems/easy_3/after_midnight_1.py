"""
The time of day can be represented as the number of minutes before or after midnight. 
If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, 
the time is before midnight.

Write a function that takes a time using this minute-based format and returns the 
time of day in 24-hour format (hh:mm). Your function should work with any integer input.

You may not use Python's datetime module.

Disregard Daylight Savings and Standard Time and other complications.


P:
Input: Integer (minutes)
Output: String (time of day in 24-hour format)
Rules:
    - Explicit
        - The input represents the number of minutes before or after midnight
        - The output represents the time of day in 24-hour format
        - If the input is positive, we calculate the time after midnight
        - If the input is negative, we calculate the time before midnight
    - Implicit
        - If we get an input of 0, we return the time at midnight
        - The output should be formatted as two digits before a colon and two digits after
        - The hour portion (before colon) should be a string representation of integers from 0 to 23 inclusive
        - The minute portion (after colon) should be the string representation of integers from 0 to 59 inclusive
        - If the input is > 1440, we calculate the time after midnight as if the input were the given value - 1440
            - Same for inputs that are > multiples of 1440
            - Similar strategy if input < -1440 or multiples thereof
        - Assume there will always be an input integer

E:
    - Confirmed understanding of the problem

D:
Input is an integer
Output is a string
We'll need variables to keep track of hour and minute, which don't need to be data structures.

A:
    - Assign the variable 'revised_minutes' to the input value
    - If the input is positive
        - Get the remainder of the input after dividing by (24 * 60 = ) 1440.
          Assign this result to a variable 'revised_minutes'
    - If the input is negative
        - Convert to a positive input by adding the input to 1440. Keep adding 1440 to this result until we get to a positive
          number. Assign this result to a variable 'revised_minutes'
    - Calculate the hours by taking 'revised_minutes' and dividing by 60. Capture the integer portion of the result in
      'hour'
    - Calculate minutes by multiplying 60 by 'hour' and subtracting that amount from 'revised_minutes'. Assign to 
      variable 'minute'
    - Return a formatted string with the hour padded to 2 digits, followed by a ":", followed by the minutes padded
      to 2 digits

"""

MAX_MINUTES_PER_DAY = 24 * 60

def time_of_day(minutes):
    revised_minutes = minutes
    if minutes > 0:
        revised_minutes = revised_minutes % MAX_MINUTES_PER_DAY
    elif minutes < 0:
        while revised_minutes < 0:
            revised_minutes += MAX_MINUTES_PER_DAY
    
    hour = revised_minutes // 60
    minute = revised_minutes - 60 * hour

    return f"{hour:02d}:{minute:02d}"

# Test cases
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True