"""
Ben and Alyssa are working on a vehicle management system. So far, they have created classes called 
Auto and Motorcycle to represent automobiles and motorcycles. After having noticed common information 
and calculations they were performing for each vehicle type, they decided to break the common behaviors 
into a separate class called WheeledVehicle. This is what their code looks like so far:

Now Syl has asked them to incorporate a new type of vehicle into their system: a Catamaran, defined as follows:

This new class does not fit well with the object hierarchy defined so far. Catamarans don't have tires. 
But we still want a common code to track fuel efficiency and range. Modify the class definitions and 
move code into a mix-in, as necessary, to share code among the Catamaran and the wheeled vehicles.


"""

class FuelMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency
    
class WheeledVehicle(FuelMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]
    
    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Catamaran(FuelMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity
        self.propellers = number_propellers
        self.hulls = number_hulls

"""
EDIT: The instance variables `fuel_efficiency` and `fuel_capacity` are both set in the initializer methods of both
Catamaran and WheeledVehicle. While we can't have `__init__` in a mix-in, we can have methods that set their values,
which we can call from the other `__init__` functions.
"""