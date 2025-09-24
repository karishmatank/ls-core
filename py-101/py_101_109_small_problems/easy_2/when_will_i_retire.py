# Build a program that displays when the user will retire and how many years she has to work till retirement.

from datetime import datetime

def validate_input(message):
    while True:
        try:
            num_input = int(input(message))
            break
        except ValueError:
            print("Enter a valid integer.")

    return num_input

age = validate_input("What is your age? ")
retirement_age = validate_input("At what age would you like to retire? ")
years_to_go = max(0, retirement_age - age)

current_year = datetime.now().year

print(f"It's {current_year}. You will retire in {current_year + years_to_go}.")
print(f"You only have {years_to_go} years of work to go!")