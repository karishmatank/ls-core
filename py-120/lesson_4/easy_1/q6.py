"""
Without running the following code, can you determine what the following code will do? 
Explain why you will get those results.
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

oracle = Oracle()
print(oracle.predict_the_future())

"""
This code will print "You will " followed by a random choice of the list returned from the choices method within Oracle.
We start by instantiating an instance of the `Oracle` class, which the variable `oracle` references. On the following line,
we invoke the `predict_the_future` instance method. Within the f-string that's returned from that function, we call the
`choices` instance method as well. That method returns a list with 4 elements, of which we are choosing a random element. Thus,
we will return "You will" + one of the choices returned from self.choices().
"""