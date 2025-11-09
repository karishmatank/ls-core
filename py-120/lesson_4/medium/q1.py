"""
Alyssa asked Ben to code review the following code:

Ben glanced over the code quickly and said - "It looks fine, except that you're trying to access self.balance 
instead of self._balance in the balance_is_positive method."

"Not so fast," Alyssa replied. "What I'm doing here is valid; I can definitely use self.balance there!"

Who is correct, Ben or Alyssa? Why?
"""

class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance
    
"""
Alyssa is correct. It is completely valid to use self.balance as we are defining the property `balance`, which simply
retrieves the value of the `_balance` instance variable tied to `self`. We are initializing this instance variable within
our initializer method, so this instance variable will definitely exist when we get around to invoking the `balance_is_positive`
method.
"""