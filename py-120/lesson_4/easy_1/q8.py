"""
Suppose you have an object named my_obj and that you want to call a method named foo using my_obj as the caller. 
How can you see where Python will look for the method. You don't need to determine the actual method location; 
just identifying the search sequence is sufficient.

Python will use the MRO to search for the `foo` method. We can use the mro method on `my_obj`'s class, so `my_obj.__class__`,
which will tell us the order of the classes in which Python will search for `foo`.

"""

class MyObj:
    def foo(self):
        pass

my_obj = MyObj()

print(my_obj.__class__.mro())