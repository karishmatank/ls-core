class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    # Don't need this here if we're just going to have "pass"
    # Instead, we can raise a NotImplementedError
#     def get_wheels(self):
#         pass
    def get_wheels(self):
        raise NotImplementedError("Subclasses to implement")
    
    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_wheels(self):
        return 4

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_wheels(self):
        return 2

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def get_wheels(self):
        return 6