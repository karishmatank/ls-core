# Q1: Write two distinct ways of reversing the list without mutating the original list
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
print(list(reversed(numbers)))
print(numbers[::-1])

# Q2: Given a number and a list, determine whether the number is included in the list
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8 
number2 = 95
print(f"number1 in numbers: {number1 in numbers}")
print(f"number2 in numbers: {number2 in numbers}")

# Q3: Programmatically determine whether 42 lies between 10 and 100, inclusive. Do the same for the values 100 and 101.
print(f"42 is between 10 and 100, inclusive: {42 in range(10, 101)}")
print(f"100 is between 10 and 100 inclusive: {100 in range(10, 101)}")
print(f"101 is between 10 and 100 inclusive: {101 in range(10, 101)}")

# Q4: Given a list of numbers, mutate hte list by remiving the number at index 2
lst = [1, 2, 3, 4, 5]
lst.pop(2)
print(lst)

# Q5: How would you verify whether the data structures assigned to the variables numbers and table are of type list?
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
print(f"numbers of type list: {isinstance(numbers, list)}")
print(f"table of type list: {isinstance(table, list)}")

# Q6: Center the following title with spaces such that total length = 40
title = "Flintstone Family Members"
total_spaces = 40 - len(title)
lspaces = total_spaces // 2
rspaces = total_spaces - lspaces
print(repr(" " * lspaces + title + " " * rspaces))
print(f"Same as LS solution?: {str(" " * lspaces + title + " " * rspaces) == title.center(40)}")

# Q7: Write a one-liner to count the number of lower-case t characters in each string
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
print(f"'t' in statement1: {statement1.count('t')}")
print(f"'t' in statement2: {statement2.count('t')}")

# Q8: Determine whether the following dictionary of people and their age contains an entry for 'Spot'
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print(f"'Spot' in ages dict: {'Spot' in ages}")

# Q9: Add entries for Marilyn and Spot to the dictionary
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}
for key, value in additional_ages.items():
    ages[key] = value
print(ages)