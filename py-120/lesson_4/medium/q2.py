"""
Alan created the following code to keep track of items for a shopping cart application he's writing:

Without changing any of the above lines of code, update the InvoiceEntry class so it functions as shown.
"""

class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        if not isinstance(new_quantity, int):
            return TypeError("Quantity must be integer.")
        
        self._quantity = new_quantity

entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)         # 5000

entry.quantity = 10_000
print(entry.quantity)         # 10000