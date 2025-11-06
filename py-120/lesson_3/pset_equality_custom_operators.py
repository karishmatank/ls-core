"""
Q1: 

> => __gt__
* => __mul__
<= => __le__
!= => __ne__
+= => __iadd__
**= => __ipow__
// => __floordiv__


Q2 - Q3:
Create the methods needed so you can compare Cat objects for equality and inequality by their name value. 
The comparisons should ignore case and should work for the == and != operators. 
If the right-hand operand is not a Cat object, the methods should return NotImplemented.

Be sure to write test cases to demonstrate that your methods work as intended.
"""

class Cat:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() == other.name.lower()
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() != other.name.lower()
    
    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() < other.name.lower()
    
    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() <= other.name.lower()
    
    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() > other.name.lower()
    
    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() >= other.name.lower()

cat1 = Cat('kitty')
cat2 = Cat('Kitty')
print(cat1 == cat2)

cat3 = Cat("Bob")
cat4 = Cat("Lucy")
print(cat3 != cat4)
print(cat3 < cat4)

cat5 = Cat("Bee")
cat6 = Cat("ace")
print(cat5 > cat6)


"""
Q4:
Add addition, subtraction, multiplication to the below class
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
    
    def __isub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __mul__(self, factor):
        if not isinstance(factor, int):
            return NotImplemented
        
        new_x = self.x * factor
        new_y = self.y * factor
        return Vector(new_x, new_y)
    
    def __rmul__(self, factor):
        if not isinstance(factor, int):
            return NotImplemented
        
        new_x = self.x * factor
        new_y = self.y * factor
        return Vector(new_x, new_y)
    
    
    def __imul__(self, factor):
        if not isinstance(factor, int):
            return NotImplemented
        
        self.x *= factor
        self.y *= factor
        return self

print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
print(Vector(5, 12) * 2)              # Vector(10, 24)
print(3 * Vector(5, 12))              # Vector(15, 36)

my_vector = Vector(5, 7)
my_vector += Vector(3, 9)
print(my_vector)                      # Vector(8, 16)

my_vector -= Vector(1, 7)
print(my_vector)                      # Vector(7, 9)

# print(Vector(3, 2) + 5)
# TypeError: unsupported operand type(s) for +: 'Vector'
# and 'int'


"""
Q5:
Add the following:
- If both x and y can be expressed as integers, compute the sum of the integer values of x and y.
- Otherwise, concatenate the string values of x and y.
"""

class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'
    
    # def __add__(self, other):
    #     try:
    #         val1 = int(self.value)
    #         val2 = int(other)
    #     except ValueError:
    #         val1 = str(self.value)
    #         val2 = str(other)

    #     return Silly(val1 + val2)
    
    def __add__(self, other):
        if not isinstance(other, str) and not isinstance(other, int):
            return NotImplemented

        if str(self.value).isdigit() and str(other).isdigit():
            return Silly(int(self.value) + int(other))
        else:
            return Silly(str(self.value) + str(other))

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)