# Write a unittest assertion that will fail if value is not odd.

import unittest

class TestSomething(unittest.TestCase):
    def test_value_is_odd(self):
        value = 3
        # Your code here
        self.assertTrue(value % 2 == 1, "Expected odd value")

unittest.main()