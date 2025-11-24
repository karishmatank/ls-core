# Opening and reading from a file
file = open('example.txt', 'r')
content = file.read()
file.close()

print(repr(content))


# Opening and readlines
file = open('example.txt', 'r')
content = file.readlines()
file.close()

print(repr(content))


# Opening + readline (one at a time)
file = open('example.txt', 'r')
print(repr(file.readline()))
print(repr(file.readline()))
print(repr(file.readline()))
print(repr(file.readline()))
print(repr(file.readline()))
print(repr(file.readline()))
file.close()

# Opening + using a for loop (preferred method)
file = open('example.txt', 'r')
for line in file:
    print(repr(line))
file.close()

with open('example.txt', 'r') as file:
    for line in file:
        print(line)

try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist")


# Writing to a new file
file = open('output.txt', 'w')
file.write('Hello, world!\n')

lines = ['First line\n', 'Second line\n']
file.writelines(lines)
file.close()

# Appending to a file
file = open('output.txt', 'a')
file.write('Third line!\n')
file.write('Last line!\n')
file.close()
