# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product of all 
# numbers between 1 and the entered integer, inclusive.

def get_valid_num(message):
    while True:
        try:
            input_num = int(input(message))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if input_num > 0:
            break
        else:
            print("Please enter an integer greater than 0.")
    return input_num

def get_valid_operator(message):
    while True:
        op = input(message).lower()
        if op in ['s', 'p']:
            break
        print("Please enter either 's' or 'p'.")
    return "sum" if op == 's' else "product"

def compute_result(last_num, op):
    # Create a list of all numbers from 1 to the entered integer, inclusive
    numbers = list(range(1, last_num + 1))

    # If sum, compute sum
    if op == 'sum':
        return sum(numbers)
    
    # Compute product
    product = 1
    for i in numbers:
        product *= i

    return product


num = get_valid_num("Please enter an integer greater than 0: ")
operator = get_valid_operator('Enter "s" to compute the sum, or "p" to compute the product. ')

result = compute_result(num, operator)

print(f"The {operator} of the integers between 1 and {num} is {result}.")