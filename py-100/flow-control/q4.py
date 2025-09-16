def foo():
    return

def qux():
    return

def baz():
    #return ('bar' if foo() else qux())
    if foo():
        return 'bar'
    return qux()