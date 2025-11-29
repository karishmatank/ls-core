# Write a unittest assertion that will fail if value.lower() does not return 'xyz'.

import unittest

class TestSomething(unittest.TestCase):
    def test_value_is_odd(self):
        value = 'XYZ'
        # Your code here
        self.assertEqual('xyz', value.lower())

unittest.main()