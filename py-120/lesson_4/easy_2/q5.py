"""
Modify the code from the previous question so that calling Hello.hi() on the class 
(rather than an instance) still uses Greeting's instance method greet() to print "Hi".
"""

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    @classmethod
    def hi(cls):
        cls().greet('Hi')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

