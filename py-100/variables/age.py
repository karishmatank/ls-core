# Q6: Calculate someone's age in 10,20,30,40 years
age = 22
print(f"You are {age} years old.")

for interval in range(10, 50, 10):
    print(f"In {interval} years, you will be {age + interval} years old.")