"""
Without running the above code, what would each snippet do were you to run it?
"""

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

# Snippet 1
hello = Hello()
hello.hi()

"""
For snippet 1, we first instantiate an instance of class `Hello`, which the variable `hello` now references. Because none of 
Hello or Greeting have an explicit initializer method, the object referenced by `hello` doesn't have any instance variables
attached to it. We then invoke the `hi` method on the `hello` object. `Hello` has a `hi` method, which in turn calls 
the `greet` method on the object, passing in an argument `'Goodbye'`. `Hello` doesn't have a `greet` method, so we'll walk through
the MRO to check `Greeting` next. We see that `Greeting` does in fact have a `greet` method, which we'll invoke. This method
simply prints the message that we've passed in as argument, so we'll print "Hello".
"""

# Snippet 2
hello = Hello()
hello.bye()

"""
This snippet performs similarly, with the exception that we invoke the `bye` method on the `hello` object. This method
invokes the `greet` method on the `hello` object, which is found once again within the `Greeting` class. This will print
"Goodbye"

EDIT: Went too quickly! `hello` references an object of type `Hello`, which does *not* have a `bye` method, as only the
`Goodbye` class has this method! `Hello` does not inherit from `Goodbye`, so we don't have access to the `bye` method.
Therefore, we'll get an AttributeError.
"""

# Snippet 3
hello = Hello()
hello.greet()

"""
In this example, we invoke the `greet` method on the `hello` object. However, we are actually missing an argument
that we should have passed in. As a result, Python will raise an error

EDIT: Correct, error is a TypeError for missing the required positional argument
"""

# Snippet 4
hello = Hello()
hello.greet('Goodbye')

"""
We invoke the `greet` method on the `hello` object, passing in an argument of value `'Goodbye'`. While `Hello` doesn't have
a `greet` method defined within its class, it inherits from `Greeting`, which means the MRO will next look in `Greeting` and
find that method defined there. The result is that we'll print "Goodbye"
"""

# Snippet 5
Hello.hi()

"""
The class `Hello` doesn't have a class method called `hi`, so this will result in an AttributeError

EDIT: Not AttributeError, but TypeError: Hello.hi() missing 1 required positional argument: 'self'
"""