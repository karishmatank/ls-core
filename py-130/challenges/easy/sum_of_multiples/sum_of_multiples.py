"""
P:
Given a natural number and a set of one or more other numbers, return the sum of the multiples of the numbers in the set
that are less than the natural number.

Rules:
    - If a set is not given, assume the set {3, 5}
    - Only include a multiple once if it is a multiple of more than one number in the set
    - Include a class method `sum_up_to` that takes one argument (natural number) and assumes the set {3, 5}
    - We should also allow for an instance to be instantiated, whose arguments specify the numbers in the set (second argument)
      and where we would call the instance method `to`, passing in the natural number as an argument

E:
    20, {3, 5}
    - 3, 5, 6, 9, 10, 12, 15, 18 => sum to 78
    
    10, no set specified => {3, 5}
    - 3, 5, 6, 9 => 23

    20, {7, 13, 17}
    - 7, 13, 14, 17 => 51

    15, {4, 6}
    - 4, 8, 12, 6 => 30

D:
    Input: Integer, optional group of numbers
    Output: Integer (sum)
    Intermediary:
        - Set: Store multiples of second argument that are less than first argument
        - Range: Iterate over all numbers less than first argument, check if it is multiple of number in second argument

High-level strategies:
    - For each element of the second argument, or [3, 5], add multiples to a set if multiple is less than first argument. 
      Sum elements of the set.

A:
    - Constructor __init__
        - Set instance variable `multiples` to a list of the arguments passed in
        - If no numbers passed in, set `multiples` to 3 and 5
    - `sum_up_to` class method
        - Input: Integer
        - Instantiate instance of class, call `to` method, pass in input
    - `to` instance method
        - Input: Integer
        - Create empty set `multiples`
        - For each number in second argument
            - Get all numbers starting from `number` that are multiples, < first input
            - Add to `multiples`
        - Get sum of all numbers in `multiples`
    

"""

class SumOfMultiples:
    def __init__(self, *args):
        self.multiples = args if args else (3, 5)
    
    @classmethod
    def sum_up_to(cls, number):
        return cls().to(number)
    
    def to(self, number):
        multiples = set()
        for base in self.multiples:
            multiples.update(range(base, number, base))
        
        return sum(multiples)