foo = 'bar'

def set_foo():
    foo = 'qux'
    return foo

set_foo()
print(foo)
foo = set_foo()
print(foo)