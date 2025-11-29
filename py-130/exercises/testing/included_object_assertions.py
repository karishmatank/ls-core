# Write a unittest assertion that will fail if the 'xyz' is not in the list lst.

import unittest

class TestSomething(unittest.TestCase):
    def test_xyz_in_lst(self):
        lst = ['abc', 'xyz']
        # Your code here
        self.assertIn('xyz', lst)

unittest.main()