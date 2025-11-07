"""
Q1: Write a program that asks the user for two numbers and divides the first number by the second number. 
Handle any potential ZeroDivisionError or ValueError exceptions (there is no need to retry inputs in this problem).

Q2: Expand your answer to the previous program so it prints the result only when no exceptions are raised. 
You should also print End of the program regardless of whether an exception is raised.

Q3: Modify your answer to the previous problem so it handles both ZeroDivisionError and ValueError 
with a single exception handler. The output for both exception types can be obtained from the exception object.
"""

# try:
#     input1 = float(input("Enter number: "))
#     input2 = float(input("Enter a second number: "))
#     result = input1 / input2
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Error: {e}")
# else:
#     print(result)


"""
Q4: Write a program that asks the user for a number. If the input isn't a number, 
let Python raise an appropriate exception. If the number is negative, raise a ValueError with an 
appropriate error message. If the number isn't negative, print a message that shows its value.

Q5: Modify your answer from the previous problem to raise a custom exception named NegativeNumberError 
instead of an ordinary ValueError exception.
"""

# try:
#     num = float(input("Enter a number: "))
# except Exception as e:
#     print(f"Error: {e}")
#     raise

# if num < 0:
#     raise ValueError("Number can't be negative.")

# print(num)

"""float will raise an exception if the number is not a float, so we didn't actually need the try/except there"""

# class NegativeNumberError(ArithmeticError):
#     def __init__(self, message="Number can't be negative."):
#         super().__init__(message)

# num = float(input("Enter a number: "))
# if num < 0:
#     raise NegativeNumberError

"""
Q6: Write a function that takes a list of numbers and returns the inverse of each number 
(if n is a number, then 1 / n is its inverse). Handle any exceptions that might occur.
"""

lst = [1, 0, "abc"]

def invert_list(numbers):
    inverse_lst = []
    for element in numbers:
        try:
            inverse_lst.append(1 / element)
        except ZeroDivisionError:
            inverse_lst.append(float('inf'))
        except TypeError:
            continue
    return inverse_lst

print(invert_list(lst))

"""
Q7: Which of the following code snippets would raise a ZeroDivisionError?

a) 5 / 2
b) 3 // 0
c) 8 % (1 - 1)
d) 7 / (3 + 4)

b and c

Q8: Given the *global* dictionary `students`, write a Python function get_age(name) that takes a student's 
name as an argument and returns their age. If the student's name isn't in the dictionary, 
the function should return 'Student not found'.
"""

students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    return students.get(name, "Student not found")

print(get_age('John'))
print(get_age('No'))


"""
Q9: Given the following list, write two functions to fetch the sixth element from the list: 
one using the LBYL approach and another using the AFNP approach. In both cases, the 
function should return None when the element isn't found.
"""

numbers = [1, 2, 3, 4, 5]

def lbyl(numbers):
    if len(numbers) >= 6:
        return numbers[5]
    else:
        return None

def afnp(numbers):
    try:
        return numbers[5]
    except IndexError:
        return None

"""
Q10: Which of the following code snippets would raise an AttributeError?

a) 'hello'.upper()
b) [1, 2, 3].push(4)
c) {'key': 'value'}.get('key')
d) (12345).length()

b and d
"""