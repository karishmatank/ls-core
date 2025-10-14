"""
Building on the previous exercise, write a function that returns True or False based on whether or not 
an inventory item (an ID number) is available. As before, the function takes two arguments: an item ID 
and a list of transactions. The function should return True only if the sum of the quantity values of the 
item's transactions is greater than zero. Notice that there is a movement property in each transaction object. 
A movement value of 'out' will decrease the item's quantity.

You may (and should) use the transactions_for function from the previous exercise.

P:
Input: Integer, list of dictionaries
Output: Boolean (True or False)
Rules:
    - Explicit
        - The first argument represents an item ID
        - The second argument represents a list of transactions
        - We should return True if the sum of the quantity values of the item's transactions is greater than 0
        - If a transaction's movement value is "out", this decreases the item's quantity
    - Implicit
        - Each transaction is a dictionary
        - Assume that each transaction will always have keys "id", "movement", and "quantity"
        - Assume that each transaction ID and quantity will always be an int
        - Assume each value associated with a transaction's "movement" key will be a string, either "in" or "out"
        - If a transaction's movement value is "in", this increases the item's quantity

E: Confirmed

D: We'll use an intermediary list to store the dictionary objects associated with the given transaction ID

A:
    - Get the transactions associated with the given transaction ID (first argument value)
    - Assign a variable 'total_quantity' to 0
    - For each of the remaining transactions:
        - If the value associated with the "movement" key is "in", add the value associated with the "quantity" key
          to 'total_quantity'
        - Else, subtract the "quantity" value from 'total_quantity'
    - If 'total_quantity' > 0, return True. Else, return False

"""

def transactions_for(tx_id, tx_list):
    return [tx for tx in tx_list if tx["id"] == tx_id]

def is_item_available(transaction_id, transactions):
    relevant_transactions = transactions_for(transaction_id, transactions)
    total_quantity = 0
    for transaction in relevant_transactions:
        if transaction['movement'] == 'in':
            total_quantity += transaction['quantity']
        else:
            total_quantity -= transaction['quantity']
    return total_quantity > 0

# Test cases
transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True