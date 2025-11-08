"""
Suppose you have the Oracle class from above and a RoadTrip class that inherits from the Oracle class, as shown below:

What will happen when you run the following code?
"""

import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

class RoadTrip(Oracle):
    def choices(self):
        return [
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
        ]
    
trip = RoadTrip()
print(trip.predict_the_future())

"""
We start out by defining a class Oracle, which has 2 instance methods `predict_the_future` and `choices`. We also define a
class RoadTrip, which inherits from Oracle and defines its own instance method `choices`, which overrides the `choices` method
from Oracle.

We then instantiate an instance of class RoadTrip, which variable `trip` references. As neither RoadTrip nor Oracle define 
initializer methods, the object referenced by `trip` has no instance variables.

We then call the `predict_the_future` method on the object referenced by `trip`. The class RoadTrip does not have a 
`predict_the_future` method, so we use the MRO to then find the attribute within the `Oracle` class. The parameter `self`
references the object referenced by `trip`, which means that when we subsequently invoke the `choices` method on `self`,
we should use the `choices` method defined within the `RoadTrip` class. This means that we will return the list with 5
elements, choose one of those elements at random, and ultimately return a phrase that starts with "You will" + one of 
those 5 elements. This will ultimately be printed.  
"""