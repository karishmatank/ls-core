"""
Implement a binary_search function that takes a list and a search item as arguments, and returns the index of the 
search item if found, or -1 otherwise. You may assume that the list argument will always be sorted.

"""

def binary_search(lst, search_item, offset=0):
    if not lst:
        return -1
    
    halfway = len(lst) // 2
    if lst[halfway] == search_item:
        return offset + halfway
    elif lst[halfway] > search_item:
        return binary_search(lst[:halfway], search_item, offset=offset)
    else:
        return binary_search(lst[halfway + 1:], search_item, offset=offset + halfway + 1)


# Test cases
# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']

print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)