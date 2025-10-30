class Car:
    def __init__(self, model, model_year, color):
        self._model = model
        self._model_year = model_year
        self.color = color
        self.current_speed = 0
        self.is_engine_on = False
    
    @classmethod
    def avg_gas_mileage(cls, distance_travelled, fuel_burned):
        miles_per_gal = distance_travelled / fuel_burned
        print(f"Average gas mileage is: {miles_per_gal:.1f} miles per gallon.")
    
    @property
    def current_speed(self):
        return self._current_speed
    
    @current_speed.setter
    def current_speed(self, speed):
        if not isinstance(speed, int):
            raise TypeError("Speed provided must be an integer.")
        
        self._current_speed = max(0, speed)
    
    def turn_engine_on(self):
        if self.is_engine_on:
            print("Engine is already on.")
        else:
            self.is_engine_on = True
            print("Engine turned on!")

    def turn_engine_off(self):
        if not self.is_engine_on:
            print("Engine is already off.")
        else:
            if self.current_speed > 0:
                self.slow_down(self.current_speed)
            self.is_engine_on = False
            print("Engine turned off!")

    def accelerate(self, mph):
        if not isinstance(mph, int):
            raise TypeError("Speed provided must be an integer.")
        self.current_speed += mph
        print(f"Accelerating.")
        self.print_current_speed()

    def slow_down(self, mph):
        if not isinstance(mph, int):
            raise TypeError("Speed provided must be an integer.")
        self.current_speed -= mph
        print("Slowing down.")
        self.print_current_speed()

    def print_current_speed(self):
        print(f"Current speed is {self.current_speed}mph.")

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError("Color must be a string.")
        self._color = new_color  

    @property
    def model(self):
        return self._model
    
    @property
    def model_year(self):
        return self._model_year
    
    def spray_paint(self, color):
        self.color = color # Use the setter we already created
        print(f"You've spray painted your car {color}!")

car = Car("A", 2025, "black")

### Q1
# car.print_current_speed()

# car.turn_engine_on()
# car.accelerate(60)
# car.turn_engine_on()

# # car.accelerate("sixty") # TypeError

# car.slow_down(80)
# car.accelerate(30)

# car.turn_engine_off()

### Q2
# print(car.color)
# car.color = 'white'
# print(car.color)
# # car.color = 42 # TypeError

# print(car.model)
# print(car.model_year)

# car.model = 'B' # AttributeError

### Q3

# print(car.color)
# car.spray_paint("gold")
# print(car.color)

### Q4
# Car.avg_gas_mileage(100, 50)



class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def _name_error_check(name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name.isalpha():
            raise ValueError("Name must be alphabetic.")

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        Person._name_error_check(name)
        self._first_name = name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        Person._name_error_check(name)
        self._last_name = name
    
    @property
    def name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
    
    @name.setter
    def name(self, name_tuple):
        first_name, last_name = name_tuple
        self.first_name = first_name
        self.last_name = last_name

# actor = Person('Mark', 'Sinclair')
# print(actor.name)              # Mark Sinclair
# actor.name = ('Vin', 'Diesel')
# print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# # ValueError: Name must be alphabetic.

# character = Person('annIE', 'HAll')
# print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.



