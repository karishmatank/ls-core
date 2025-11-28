# Use a generator expression to yield each character of a string in reverse order.

string = 'hello'

reversed_string = (char for char in string[::-1])
for char in reversed_string:
    print(char)