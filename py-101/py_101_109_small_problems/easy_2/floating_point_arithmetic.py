# Write a program that prompts the user for two positive numbers (floating-point), 
# then prints the results of the following operations on those two numbers: 
# addition, subtraction, product, quotient, floor quotient, remainder, and power. 
# Do not worry about validating the input.

def prompt(message):
    print(f"==> {message}")

prompt("Enter the first number:")
number1 = float(input())

prompt("Enter the second number:")
number2 = float(input())

prompt(f"{number1} + {number2} = {number1 + number2}")
prompt(f"{number1} - {number2} = {number1 - number2}")
prompt(f"{number1} * {number2} = {number1 * number2}")
prompt(f"{number1} / {number2} = {number1 / number2}")
prompt(f"{number1} // {number2} = {number1 // number2}")
prompt(f"{number1} % {number2} = {number1 % number2}")
prompt(f"{number1} ** {number2} = {number1 ** number2}")