"""
In the previous question, we had a mix-in called SpeedMixin that contained a go_fast method. 
We add this mix-in to the Car class as shown below:

When we called small_car.go_fast, you may have noticed that the output includes the vehicle type. How is this done?
"""

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}!')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

small_car = Car()
small_car.go_fast()
# I am a super fast Car!

"""
We have done this by getting the name of the class that called the method.

In this case, small_car is of type Car. self references the object that `small_car` is referencing, 
thus self.__class__.__name__ resolves to Car
As a result, we print "I am a super fast Car!"

EDIT:
    - First part is correct
    - self.__class__ references the *`Car` class, which is an object of the `type` class*
    - self.__class__.__name__ *gets the name of the class as a string*

"""