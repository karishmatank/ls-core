"""
Let's practice creating an object hierarchy.

Create a class called Animal with a single instance method called speak that takes a string argument and prints 
that argument to the terminal.

Now create two other classes that inherit from Animal, one called Cat and one called Dog. The Cat class should 
have a meow instance method that takes no arguments and prints Meow!. The Dog class should have a bark instance 
method that says Woof! Woof! Woof! (dogs never bark just once). Make use of the Animal class's speak method 
when implementing the Cat and Dog classes. Don't invoke the print function in either of the subclasses.
"""

class Animal:
    def speak(self, string):
        print(string)

class Cat(Animal):
    def meow(self):
        self.speak("Meow!")

class Dog(Animal):
    def bark(self):
        self.speak("Woof! Woof! Woof!")

"""
EDIT: This works, but we should probably have created the message in `bark` as 'Woof! ' * 3 and then remove the trailing space
with strip()
"""