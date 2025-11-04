"""
Given the rectangle class from the prior problem (included below),
Write a class called Square that inherits from the Rectangle class. The Square class is used like this:
"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, size):
#         self._width = size
#         self._height = size
        # Instead of repeating self._width and self._height, just use the super init to do that for you
        super().__init__(size, size)
    
square = Square(5)
print(square.area == 25)      # True