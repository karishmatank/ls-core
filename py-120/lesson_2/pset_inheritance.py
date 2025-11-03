"""
Q1: Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"
"""

class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!

bulldog = Bulldog()
print(bulldog.sleep())

"""
Q2: Create a new class Cat, which can do everything a dog can, except fetch. Assume the methods do the exact same thing. 
Hint: don't copy and paste any methods from Dog into Cat; come up with a class hierarchy instead.
"""

class Pet:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Pet):
    def fetch(self):
        return 'fetching!'
    

class Cat(Pet):
    pass