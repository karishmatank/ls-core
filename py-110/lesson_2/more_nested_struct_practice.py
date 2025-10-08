# Q1: Given the following code, what will the final values of s and arr be? Try to answer without running the code.
s = 'hello'
arr = [1, 2]
container = [s, arr]

container[0] += ' world'
container[1].append(3)

# The final value of s is still 'hello', as strings are immutable. When we reassign container[0], we create a new object
# in memory for container[0] to point to, which leaves s still pointing to an object with value 'hello'.

# The final value of arr will be [1, 2, 3], as we are mutating the list object that arr is pointing to by appending 3 to
# container[1].

# Even though the question didn't ask, the final value of container is ['hello, world', [1, 2, 3]].



# Q2: Given the following code, what will the final values of num and my_list be? Try to answer without running the code.
num = 10
my_list = ['a', 'b']
my_dict = {'x': num, 'y': my_list}

my_dict['x'] *= 2
my_dict['y'][0] = 'Z'

# num will remain 10. We are reassigning the value associated with key 'x' in my_dict, but because integers are immutable,
# this means the value associated with 'x' is now 20, while num is still 10.

# my_list will now be ['Z', 'b'], because we are mutating the list object that my_list is pointing to as a result of mutating
# the list via my_dict['y'][0].

# Even though the question didn't ask, the final value of my_dict is {'x': 20, 'y': ['Z', 'b']}



# Q3: Given the following code, what will the final values of val1 and val2 be? Try to answer without running the code.
val1 = 'cat'
val2 = [10, 20]
struct = {
    'first': val1,
    'second': [val2],
}

struct['first'] = 'dog'
struct['second'][0][1] += 5

# val1 will remain 'cat'. Even though we reassign the value associated with key 'first' in struct, strings are immutable,
# which means that we are creating a new object in memory with value 'dog' that is now associated with key 'first', while
# val1 still has the value 'cat'.

# val2 is now [10, 25]. We are mutating the nested list that is associated with struct['second'], which has one element
# pointing to the same object that val2 is pointing to. We access that by further indexing by 0, and then lastly reassign
# the element at index 1 to add 5, which corresponds to val2[1]. Lists are mutable, so this change mutates the object
# val2 is pointing at.

# Even though the question didn't ask, struct now has value {'first': 'dog', 'second': [[10, 25]]}