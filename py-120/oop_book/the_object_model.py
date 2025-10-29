"""
Q1:
How do we create a class and an object in Python?
Write a program that defines a class and creates two objects from that class. The class should have at least one
instance variable that gets initialized by the initializer.
What class you create doesn't matter, provided it satisfies the above requirements.
"""

class Country:
    def __init__(self, name):
        self.name = name
        type_name = self.__class__.__name__
        print(f"{self.name} is a {type_name}")

united_states = Country("United States")
canada = Country("Canada")


"""
Q2:
Given an instance of a Foo object, show two ways to print `I am a Foo object` without hardcoding the word `Foo`.
"""

class Foo:
    def __init__(self):
        pass

obj = Foo()
print(f"I am a {obj.__class__.__name__} object.")
print(f"I am a {type(obj).__name__} object.")