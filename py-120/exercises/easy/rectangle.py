"""
Create a Rectangle class whose initializer takes two arguments that represent the rectangle's width and height, 
respectively. Use the following code to test your solution:
A rectangle's area is given by its width times its height.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
       
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, new_width):
        if not isinstance(new_width, int):
            raise TypeError("Width must be integer.")
        self._width = new_width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, new_height):
        if not isinstance(new_height, int):
            raise TypeError("Height must be integer.")
        self._height = new_height
    
    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True
