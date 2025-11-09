"""
What would happen if you ran the following code? Don't run it until you've checked your answer:
"""

class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())
print(tv.model())

print(Television.manufacturer())
print(Television.model())

"""
We'll print:

Amazon
Omni Fire
Amazon
(raise AttributeError)

Even though it isn't recommended, the first print statement will still print Amazon, as there is no instance method named
`manufacturer`, so Python will look to the class method and pass in the class of the object `tv` references.

The second print statement is straightforward and will call the object's `model` method.

The third print statement works because `manufacturer` is a class method, and we are implicitly passing in `Television` as 
the first argument.

I don't think the fourth print statement will work, as `model` is an instance method, not a class method.

EDIT: Correct that 4th one didn't work, and correct on the others. But error is a TypeError, not an AttributeError

"""