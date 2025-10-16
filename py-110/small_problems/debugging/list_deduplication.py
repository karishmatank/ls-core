"""
A developer is trying to remove duplicates from a list. They use a set for deduplication, 
but the order of elements is lost. How can we preserve the order?

I would probably just use a for loop rather than trying to work with sets. As mentioned, with sets, we can't
guarantee order, so it seems risky to rely on a set here. I'm looking forward to learning if there's an easier way
to do this.

"""

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list(set(data))

unique_data = []
for element in data:
    if element not in unique_data:
        unique_data.append(element)

print(unique_data == [4, 2, 1, 3]) # order not guaranteed