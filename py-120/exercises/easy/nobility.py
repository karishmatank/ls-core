class WalkMixin:
    def walk(self):
        return f"{self.full_name} {self.gait()} forward"

class Person(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"
    
    @property
    def full_name(self):
        return self.name

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"
    
    @property
    def full_name(self):
        return self.name

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    
    @property
    def full_name(self):
        return self.name

class Noble(WalkMixin):
    def __init__(self, name, title):
        self.name = name
        self.title = title
    
    def gait(self):
        return "struts"
    
    @property
    def full_name(self):
        return self.title + " " + self.name
    
    

mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"



# Further exploration

class WalkMixin:
    def walk(self):
        return f"{self.full_name} {self.gait()} forward"

class Animal(WalkMixin):
    def __init__(self, name):
        self.name = name
    
    @property
    def full_name(self):
        return self.name
    
class Person(Animal):
    def gait(self):
        return "strolls"

class Cat(Animal):
    def gait(self):
        return "saunters"
    
class Cheetah(Cat):
    def gait(self):
        return "runs"

class Noble(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self.title = title
    
    def gait(self):
        return "struts"
    
    @property
    def full_name(self):
        return self.title + " " + super().full_name
    
    

mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"