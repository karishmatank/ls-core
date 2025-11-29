# Write a unittest assertion that will fail if value is not an instance of the Numeric class or one of its subclasses.

import unittest

class Numeric:
    pass

class Integer(Numeric):
    pass

class TestNumeric(unittest.TestCase):
    def test_value_is_instance_of_numeric(self):
        value = Integer()
        # Your code here
        self.assertIsInstance(value, Numeric)

unittest.main()