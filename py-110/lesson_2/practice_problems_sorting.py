# Q1: Sort the following list of numbers first in ascending numeric order, then in descending numeric order. 
# Do not mutate the list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]
sorted_asc = sorted(lst)
sorted_desc = sorted(lst, reverse=True)

print("Q1:")
print(sorted_asc)
print(sorted_desc)

# Q2: Repeat the previous exercise but, this time, perform the sort by mutating the original list.
lst = [10, 9, -6, 11, 7, -16, 50, 8]

print("\nQ2:")

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

# Q3: Repeat problem 2 but, this time, sort the list as string values. 
# Both the list passed to the sorting function and the returned list should contain numbers, not strings.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

print("\nQ3:")

lst.sort(key=str)
print(lst)
lst.sort(key=str, reverse=True)
print(lst)

# Q4: How would you sort the following list of dictionaries based on the year of publication of each book, 
# from the earliest to the most recent?
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def get_year(x):
    return int(x['published'])

print("\nQ4:")

books.sort(key=get_year)
print(books)
