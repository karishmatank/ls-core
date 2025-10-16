"""
You have a function that should check whether a key exists in a dictionary and returns its value. 
However, it's raising an error. Why is that? How would you fix this code?

Within the if condition, the bracket notation we're using isn't checking whether the key exists, it's checking whether
the value associated with the key is 'truthy'. If the key doesn't exist, we're going to get a KeyError.

To solve this, we can just use in keyword. We may want to be more descriptive however than the current function is being
to specify that the key exists or doesn't, rather than just use the get method and return None if the key doesn't exist. 
If we just return None, we won't know whether the key actually exists or whether the value associated with it in 
the dictionary is just None.

"""

def get_key_value(my_dict, key):
    # if my_dict[key]:
    #     return my_dict[key]
    # else:
    #     return None
    if key in my_dict:
        return my_dict[key]
    else:
        return "Key is not in dictionary"

print(get_key_value({"a": 1}, "b"))