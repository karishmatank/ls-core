# Q1

class Person:
    def __init__(self, name):
        self.name = name

# bob = Person('bob')
# print(bob.name)
# bob.name = 'Robert'
# print(bob.name)


# Q2
class Person:
    def __init__(self, first_name, last_name=''):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def name(self):
        if not self.last_name:
            return self.first_name
        return f"{self.first_name} {self.last_name}"
    
# bob = Person('Robert')
# print(bob.name)
# print(bob.first_name)
# print(repr(bob.last_name))
# bob.last_name = 'Smith'
# print(bob.name)


# Q3
class Person:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        # if not self._last_name:
        #     return self._first_name
        # return f"{self._first_name} {self._last_name}"
    
        return f"{self.first_name} {self.last_name}".strip()

    @name.setter
    def name(self, given_name):
        names = given_name.split()
        self.first_name = names[0]
        if len(names) > 1:
            self.last_name = names[1]
        else:
            self.last_name = ''
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        self._last_name = name

# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'
# print(bob.name)             # Robert Smith

# bob.name = 'Prince'
# print(bob.first_name)       # Prince
# print(repr(bob.last_name))  # ''

# bob.name = 'John Adams'
# print(bob.first_name)       # John
# print(bob.last_name)        # Adams


# Q4
bob = Person('Robert Smith')
rob = Person('Robert Smith')
is_same_name = bob.name == rob.name
# print(is_same_name)


# Q5
bob = Person('Robert Smith')
print(f"The person's name is: {bob}") # This will replace bob with the "nonsense" that references its place in memory

class Person:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        # if not self._last_name:
        #     return self._first_name
        # return f"{self._first_name} {self._last_name}"
    
        return f"{self.first_name} {self.last_name}".strip()

    @name.setter
    def name(self, given_name):
        names = given_name.split()
        self.first_name = names[0]
        if len(names) > 1:
            self.last_name = names[1]
        else:
            self.last_name = ''
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    def __str__(self):
        return self.name

bob = Person('Robert Smith')
print(f"The person's name is: {bob}") # This now prints Robert Smith where we want it