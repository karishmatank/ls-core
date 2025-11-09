"""
You are given the following code:

Write additional code for KrispyKreme such that the print invocations will work as shown.
"""

class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing
    
    def __str__(self):
        filling = "Plain" if not self.filling else self.filling
        glazing = "" if not self.glazing else self.glazing
        bridge_word = "" if not self.glazing else "with"

        return f"{filling} {bridge_word} {glazing}".strip()

donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing

"""
EDIT: Works, alternatively we can build up a list of options and join them together with the separator ' with ' using 
the join method.
"""