# Write a unittest assertion that will fail unless employee.hire() 
# raises a NoExperienceError exception when an employee only has 2 years of experience.

class NoExperienceError(Exception):
    pass

class Employee:
    def __init__(self, experience):
        self.experience = experience
        self.hired = False

    def hire(self):
        if self.experience < 3:
            raise NoExperienceError
        else:
            self.hired = True


import unittest

class TestEmployee(unittest.TestCase):
    def test_hire_exception_with_low_experience(self):
        employee = Employee(2)
        # Your code here
        with self.assertRaises(NoExperienceError):
            employee.hire()

unittest.main()