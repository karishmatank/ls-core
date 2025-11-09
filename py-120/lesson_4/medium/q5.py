"""
How could you change the light_status method name below so that the method name is clearer and less repetitive?
"""

class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def light_status(self):
        return (f'I have a brightness level of {self.brightness} '
                f'and a color of {self.color}')

my_light = Light(50, 'Red')
print(my_light.light_status())

"""
You can just change it to `status`. Alternatively, maybe we can change it to `info`, as this prints information about
the current state of the light, or even use `__str__`.
"""