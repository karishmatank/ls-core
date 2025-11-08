"""
Which of the following classes would create objects that have an instance variable. How do you know?
"""

class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

"""
The `Pizza` class would create objects that have an instance variable. This is because instance variables are preceded
by `self`, signalling that they belong to the object. We only see this with `Pizza`, as the variable `my_name` within
the initializer function of `Fruit` is only a local variable.
"""