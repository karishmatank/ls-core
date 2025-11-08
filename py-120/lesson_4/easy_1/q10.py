"""
Explain what the _cats_count variable is, what it does in this class, and how it works. Write some code to test your theory.
"""

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count
    
"""
The `_cats_count` variable is a class variable. When we initialize an instance of class Cat, we increment this variable by 1,
as shown by `self.__class__._cats_count += 1`, where self.__class__ resolves to Cat, and thus we find the class variable
named `_cats_count` within the Cat class to increment its value. When we call the class metnod `cats_count` on the `Cat` class,
we will get the number of instances initialized of class Cat, as this variable effectively acts as a counter for how many 
Cat objects we've instantiated.
"""

cat1 = Cat('A')
cat2 = Cat('B')
print(Cat.cats_count()) # Should print 2

cat3 = Cat('C')
print(Cat.cats_count()) # Should print 3