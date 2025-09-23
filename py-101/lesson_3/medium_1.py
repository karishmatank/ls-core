# Q1:  Write a program that outputs The Flintstones Rock! 10 times, 
# with each line prefixed by one more hyphen than the line above it
for i in range(1, 11):
    print(f"{"-" * i}The Flintstones Rock!")

# Q2: Refactor the function to gracefully handle negative inputs
def factors(number):
    divisor = max(number, 0) # Changed from divisor = number
    result = []
    while divisor != 0: # Solution changed thhis to divisor > 0, which is the preferred method
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# Q3
# Key difference between the implementations is that the first mutates the buffer
# (and thus technically doesn't need to return the buffer at the end) whereas the second
# reassigns the buffer to include the new element, thus making a new local variable "buffer"

# Q4: What will these output:
print(0.3 + 0.6) # Something very close to 0.9 like 0.8999999999 or so
print(0.3 + 0.6 == 0.9) # This may print False, even though we would think True, given floating point imprecision

# Q5: What will the following code output?
nan_value = float("nan")
print(nan_value == float("nan")) # My first instinct was to say True, since I would think the values match

# Q6: What does the following output?
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8) # 34

# Q7: Does the following code mutate the dictionary?
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)

# Yes, it does. 

# Q8: What does the following output?
def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"

print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# This should print "paper"
# - rps("rock", "paper") = "paper" and rps("rock", "scissors") = "rock"
# - These both lead to rps("paper", "rock") = "paper"
# - This then leads to rps("paper", "rock") = "paper"

# Q9: What does the following return
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

bar(foo())
# It returns False because foo() returns "yes", and bar("yes") returns False due to param == "no" being False

# Q10: Predict the output
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
# True given interning as 42 is a small enough integer