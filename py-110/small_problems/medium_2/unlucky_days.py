"""
Some people believe that Fridays that fall on the 13th day of the month are unlucky days. 
Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. 
You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. 
You may also assume that the same calendar will remain in use for the foreseeable future.

P:
Determine the number of 13ths that fall on a Friday within a given year.

Rules:
    - Assume the year we're given is greater than 1752
    - Assume the same calendar will remain in use in the future

E: Understood

Data structures:
    - Input: Integer (year)
    - Output: Integer (# of Friday the 13ths)
    - Intermediary:
        - List: Store all Fridays within the given year, or all 13th days in a given year
        - Boolean: Determine if a given Friday is the 13th day of the month
        - Integer: Keep count of the number of Friday the 13ths

High-level strategies:
    - Create a list with all Fridays in a given year. Count the number of Fridays whose day is 13.
    - Iterate through every single 13th day in a year. Count the number that occur on a Friday.

A:
    - Create a list with the 13th day of each month in a year
        - Iterate through a range from 1 to 12 (inclusive) for our months
    - Count the number of days in this list that are on a Friday
        - Initialize a constant variable FRIDAY whose value is 4
        - Find the day of the week for every day in our previously defined list
        - Count the number of days whose value matches FRIDAY
    - Return this count

"""

from datetime import date

FRIDAY = 4

def friday_the_13ths(year):
    day_13s = [date(year, month, 13) for month in range(1, 13)]
    days_of_week = [day.weekday() for day in day_13s]
    return days_of_week.count(FRIDAY)


# Test cases
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True