"""
If we have a Car class and a Truck class and we want to be able to go_fast, how can we add the ability for 
them to go_fast using the mix-in SpeedMixin? How can you check whether your Car or Truck can now go fast?
"""

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car:
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck:
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')

"""
We should have Car and Truck inherit from SpeedMixin as follows. We can check that these work by then invoking the `go_fast`
method from any Car or Truck instances that we've instantiated, which will print either "I am a super fast Car" or 
"I am a super fast Truck". If it didn't work, Python would raise an AttributeError instead.
"""

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck(SpeedMixin):
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')

car = Car()
truck = Truck()
car.go_fast()
truck.go_fast()