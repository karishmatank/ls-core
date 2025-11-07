"""
Q1:
Define a Dog class that has a breed instance variable. 
Instantiate two objects from this class, one with the breed 'Golden Retriever' and another with the breed 'Poodle'. 
Print the breed of each dog.

Q2:
Add a get_breed method to the Dog class from your answer to the previous problem. 
The method should return the dog's breed. Use the method to print the breeds of the two dog objects
you created in the previous problem. You should also mark the breed instance variable for internal use only.
"""

class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

dog1 = Dog("Golden Retriever")
dog2 = Dog("Poodle")

print(dog1.get_breed())
print(dog2.get_breed())

"""
Q3: Create a Cat class that has a single method named get_name that returns the name instance variable. 
Without initializing name, try to instantiate a Cat object and call get_name. Print Name not set! when the error occurs.
"""

class Cat:
    def __init__(self):
        pass

    def get_name(self):
        try:
            return self._name
        except AttributeError:
            return "Name not set!"
    
cat = Cat()
print(cat.get_name())


"""
Q4: Create an instance of the Dog class from your answer to Problem 2. 
Set its breed directly from outside the class, then print the resulting breed.
"""

dog3 = Dog('')
dog3._breed = "breed"
print(dog3.get_breed())

"""
Q5: Define a Student class that has a class variable named school_name. 
You should initialize the school name to 'Oxford'. After defining the class, instantiate an instance of the Student 
class and print the school name using that instance.

Q6: Modify the Student class from your answer to the previous problem. 
The modified class should have an instance variable called name that gets initialized during instantiation. 
Create two Student objects with different names but the same school, then print the name and school for both students.

Q7: Modify the Student class from your answer to the previous problem. 
The modified class should have a class method that returns the school's name. 
Without instantiating any Student objects, print the school's name in two different ways: once with the class method, 
and once by accessing the class variable directly.
"""

class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

# student = Student()
# print(student.__class__.school_name)  # Oxford

student1 = Student("A")
student2 = Student("B")

print(f"{student1.name = }")
print(f"{student1.school_name = }")
print(f"{student2.name = }")
print(f"{student2.school_name = }")

print(Student.get_school_name())
print(Student.school_name)

"""
Q8: Create a Car class that has a class variable named manufacturer and an instance variable named manufacturer. 
Initialize these variables to different values. 
Add a show_manufacturer method that prints both the class and instance variables.
"""

class Car:
    manufacturer = "A"

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def show_manufacturer(self):
        print(f"{self.manufacturer = }")
        print(f"{self.__class__.manufacturer = }")

car = Car("B")
car.show_manufacturer()

"""
Q9: Create a Bird class that has an instance attribute, species. 
Create a Sparrow class that inherits from the Bird class. 
Create a Sparrow instance object, then print its species. The expected output is sparrow.
"""

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    pass

sparrow = Sparrow("sparrow")
print(f"{sparrow.species = }")

"""
Q10: What will the following print (without running it) and why?
"""

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        self.color = color

birdie = Sparrow("sparrow", "brown")
# print(birdie.species)               # What will this output?

"""
This will result in an AttributeError. When we instantiate the Sparrow object, we use Sparrow's initializer method to do so.
The initializer method only sets an attribute for color.
Therefore, when we try to print `birdie`'s `species` attribute value, we find it doesn't exist.
"""

"""
Q11: Create a Mammal class that always sets an attribute called legs to a value of 4. 
Create a Human class that inherits from Mammal, but instead sets the value of legs to 2. 
Print the number of legs for a human to verify correct operation.
"""

class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        self.legs = 2

print(f"{Human().legs = }")

"""
Q12: Without running the below, what will this output and why?
"""

class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound())

"""
This will print "roar". When we define the classes, we define a `sound` class variable for Cat with value "meow" and
a `sound` class variable for Lion with value "roar". Then, calling `Lion.make_sound()` will end up walking through the MRO
to the method within Cat. The function returns `cls.sound`, where cls resolves to `Lion`, as we called the method on the class
`Lion`. Therefore, we end up returning `Lion.sound`, where `Lion` does have a class variable named sound whose value is "roar".
"""

"""
Q13: Without running the code: when an instance of Pine is created, what value will its type attribute have? Why?
"""

class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

"""
Its type attribute will have a value of "Pine Tree". When we create an instance of Pine, we are calling the initializer method
within Pine. This method in turn calls the initialier method in Tree first, as Pine inherits from Tree and we see a reference
to `super`'s initializer method. `Tree`'s initializer method creates an instance variable `type` whose value is "Generic Tree".
However, we reassign `type`'s value in the very next line to "Pine Tree".
"""

"""
Q14: Without running it, what happens to the code below?
"""

class A:
    def __init__(self):
        self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

"""
This will raise an AttributeError. When we initialize an object of type B, we run class B's initializer method, which 
creates an instance variable named `var_b`. If we then try to find an attribute named `var_a`, we don't see one that exists
within the object that `b` is pointing to. We walk through the MRO, but we don't find an attribute of `var_a` either, whether
that's a class variable or method. So we raise an AttributeError.
"""