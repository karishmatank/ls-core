"""
Consider the following code:

class Cat:
    def __init__(self, type):
        self.type = type

print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>

The output here isn't very useful. It only tells us that we've got an instance of the Cat class, 
and it's memory address. It would be better if the output were more meaningful. 
For instance, maybe it can print I am a hairball instead. Update the code to produce that result.
"""

class Cat:
    def __init__(self, type):
        self.type = type
    
    def __str__(self):
        return f"I am a {self.type}"

print(Cat('hairball'))
