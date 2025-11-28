# Create a generator function that yields user input strings until the word "stop" is entered.

def get_input():
    while True:
        string = input("Enter a string: ")

        if string == 'stop':
            break

        yield string

for string in get_input():
    print(string)