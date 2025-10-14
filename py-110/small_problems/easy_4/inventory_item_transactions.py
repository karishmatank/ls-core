"""
Write a function that takes two arguments, an inventory item ID and a list of transactions, 
and returns a list containing only the transactions for the specified inventory item.

P:
Input: Integer and list
Output: List
Rules:
    - Explicit
        - The first argument represents an inventory item ID
        - The second argument represents a list of transactions
        - Our output list should contain only the transactions for the specified inventory item
    - Implicit
        - Assume we will always have an integer value for our first argument
        - Assume the list of transactions will all be dictionaries with keys "id", "movement", and "quantity"

E: Confirmed

D: No intermediary structures anticipated

A:
    - Return a list where the transaction IDs, as per the "id" key in each transaction dictionary, in the second input 
      matches the value of the first input

"""

def transactions_for(tx_id, tx_list):
    return [tx for tx in tx_list if tx["id"] == tx_id]

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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True