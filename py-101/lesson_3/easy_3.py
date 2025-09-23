## Q1: Write two different ways to remove all of the elements from the following list:

# Method 1
numbers = [1, 2, 3, 4]
numbers.clear()

# Method 2
numbers = [1, 2, 3, 4]
while numbers:
    numbers.pop(0)

## Q2- What will this output (don't run the code)
# print([1, 2, 3] + [4, 5])
# This will print [1, 2, 3, 4, 5]

## Q3 - What will this output (don't run the code)
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
# print(str1) - commented out to avoid it printing if file is run
# This will print "hello there"

## Q4 - What will this output (don't run the code)
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
# print(my_list1) - commented out to avoid it printing if file is run
# This will print [{"first": 42}, {"second": "value2"}, 3, 4, 5] because of shallow copies

## Q5: Rewrite to only include one return + no explicit True or False
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

# Solution 1
def is_color_valid(color):
    return color == "blue" or color == "green"

# Solution 2
def is_color_valid(color):
    return color in ["blue", "green"]