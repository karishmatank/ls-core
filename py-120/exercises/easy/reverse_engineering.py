"""
Write a class such that the following code prints the results indicated by the comments:

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz
"""

class Transform:
    def __init__(self, text):
        self.text = text

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, new_text):
        if not isinstance(new_text, str):
            raise TypeError("Text must be string.")
            
        self._text = new_text
    
    def uppercase(self):
        return self.text.upper()
    
    @classmethod
    def lowercase(cls, text):
        return text.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz
