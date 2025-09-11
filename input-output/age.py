age = int(input("How old are you? "))

print(f"You are {age} years old.")

for interval in range(10, 50, 10):
    print(f"In {interval} years, you will be {age + interval} years old.")