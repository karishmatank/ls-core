# print(({} and (2 > '1')) or ('c' > 'a'))


# def add_el1(lst, el):
#     lst + [el]
#     print(lst + [el])

# def add_el2(lst, el):
#     lst.append(el)

# letters = ['a', 'b', 'c']
# print(add_el1(letters, 'd'))
# print(add_el2(letters, 'd'))


# text = 'Hello! I am Eloise.'

# def swap(s):
#     new_string = ""
#     for char in s:
#         # s.replace(char, char.upper())
#         new_string += char.upper()
#     return new_string

# print(swap(text))
# print(text)


# greeting = "Hello"

# def greet():
#     greeting = "Hi"
#     print(greeting)

# greet()
# print(greeting)


# players = [
#     {'name': 'Joe', 'age': 25},
#     {'name': 'Andy', 'age': 31},
#     {'name': 'Ralph', 'age': 18},
#     {'name': 'Mark', 'age': 28},
# ]

# # add code here
# def older_than_age(players_list, age_threshold):
#     # Returns True if any players are older than the threshold
#     for player in players_list:
#         if player['age'] > age_threshold:
#             return True
    
#     return False


# print(older_than_age(players, 30)) # True
# print(older_than_age(players, 31)) # False


# d = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }

# lst = list(d.items())
# print(lst)

# lst_keys = list(d.keys())
# lst_values = list(d.values())
# zipped = zip(lst_keys, lst_values)
# print(list(zipped))




# s1 = "Hello"
# print(s1.isalpha())
# s2 = "Hello World"
# print(s2.isalpha())
# s3 = "Hello!"
# print(s3.isalpha())
# s4 = "Hello123"
# print(s4.isalpha())
# s5 = ""
# print(s5.isalpha())
# s6 = "こんにちは"
# print(s6.isalpha())
# s7 = "HelloWorld"
# print(s7.isalpha())
# words = ["apple", "banana", "cherry"]
# print(all(word.isalpha() for word in words))




# players = [
#     {'name': 'Joe', 'age': 25},
#     {'name': 'Andy', 'age': 31},
#     {'name': 'Ralph', 'age': 18},
#     {'name': 'Mark', 'age': 28},
# ]

# def age_players(players):
#     for player in players:
#         value = player['age']
#         print(value is player['age']) # True - value is pointing to the same object in memory
#         value += 1
#         print(value is player['age']) # False - value was reassigned to point to a new object in memory

# age_players(players)
# print(players)


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# keys = my_dict.keys()
# print(keys)
# for key in keys:
#     print(key)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# values = my_dict.values()
# print(values)
# for value in values:
#     print(value)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# items = my_dict.items()
# print(items)
# for key, value in items:
#     print(key, value)





# var = 10

# def function1():
#     var = 20
#     print(var)

# function1()

# try:
#     print(var)
# except NameError:
#     print("Error occurred")

# def function2():
#     var += 5
#     print(var)

# try:
#     function2()
# except UnboundLocalError:
#     print("Error occurred")

# def function3():
#     global var
#     var += 5
#     print(var)

# function3()
# print(var)




# def function1():
#     x = 10

#     def function2():
#         y = 20
#         print(x)

#     function2()
#     print(x)

# function1()
# print(x)
# print(y)


# def reassign_list(a_list):
#     # a_list = a_list + [4, 5] # This is reassignment
#     a_list += [4, 5] # This is mutation
#     print(a_list)
#     print(id(a_list))

# my_list = [1, 2, 3]
# reassign_list(my_list)
# print(id(my_list))
# print(my_list)