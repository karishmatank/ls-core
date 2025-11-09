"""
The designers of the vehicle management system now want to make an adjustment for how the range of vehicles is calculated. 
For the seaborne vehicles, due to prevailing ocean currents, they want to add an additional 10km of range even if 
the vehicle is out of fuel.

Alter the code related to vehicles so that the range for autos and motorcycles is still calculated as before, 
but for catamarans and motorboats, the range method will return an additional 10km.
"""

class FuelMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency
    

class SeaborneFuelMixin(FuelMixin):
    def range(self):
        return super().range() + 10

    
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


class Watercraft(SeaborneFuelMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity
        self.propellers = number_propellers
        self.hulls = number_hulls


class Catamaran(Watercraft):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(number_propellers, 
                         number_hulls, 
                         kilometers_per_liter, 
                         liters_of_fuel_capacity)

class Motorboat(Watercraft):
    def __init__(self, 
                 kilometers_per_liter, 
                 liters_of_fuel_capacity):
        super().__init__(1, 
                         1, 
                         kilometers_per_liter, 
                         liters_of_fuel_capacity)