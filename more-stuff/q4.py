counter = 0

def increment_counter():
    global counter
    counter += 1


# Provided test code
print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101