/*
What does this point to in the code below?
*/

function whatIsMyContext() {
  return this;
}

/*
This references `window` in Chrome Snippets in sloppy mode and `undefined` in strict mode.

EDIT: Incorrect! We only know the true context during execution time.
*/

/*
What does this point to in the code below?
*/

function whatIsMyContext() {
  return this;
}

whatIsMyContext();

/*
Now, we're invoking `whatIsMyContext`, so my answer from the prior question stands.
*/

/*
What does this point to in the code below?
*/

function foo() {
  function bar() {
    function baz() {
      console.log(this);
    }

    baz();
  }

  bar();
}

foo();

/*
The `window` object in Chrome Snippets, or `undefined` in strict mode.
*/

/*
What does this point to in the code below?
*/

let obj = {
  count: 2,
  method() {
    return this.count;
  },
};

obj.method();

/*
`this` points to the `obj` object.
*/

/*
In strict mode, what does the following program log to the console?
*/

function foo() {
  console.log(this.a);
}

let a = 2;
foo();

/*
This will raise a TypeError. `this` references `undefined` in strict mode within `foo`.
*/

/*
What does the following program log to the console?
*/

let a = 1;
function bar() {
  console.log(this.a);
}

let obj = {
  a: 2,
  foo: bar,
};

obj.foo();

/*
This will log `2` to the console. `this` references `obj` as we invoked `foo` as a method, which points to
the `bar` function.
*/

/*
What does the following code log to the console?
*/

let foo = {
  a: 1,
  bar() {
    console.log(this.baz());
  },

  baz() {
    return this;
  },
};

foo.bar();
let qux = foo.bar;
qux();

/*
First, we invoke `foo.bar`, which invokes foo.baz() as `this` inside `foo.bar` references `foo`
When we invoke `foo.baz`, we return `this`, which references the `foo` object as it was a method invocation.
That thus returns the `foo` object.

This will raise a TypeError in strict mode. When we invoke `qux`, `this` references `undefined`, which doesn't have
a `baz` method.
In sloppy mode, `this.baz` will be `undefined`, and we can't invoke `undefined`, so I think it'll raise an error there
as well.
*/

/*
What does this point to in the code below, and what does the method return?
*/

let myObject = {
  count: 1,
  myChildObject: {
    myMethod() {
      return this.count;
    },
  },
};

myObject.myChildObject.myMethod();

/*
I believe `this` references `myObject.myChildObject`. Thus, it will look for a `count` property
within that object, but it won't find it. Thus, I think it'll return `undefined`.
*/

/*
In the previous problem, how would you change the context, or the value of this, to myObject?
*/

/*
I would use `call` to call `myMethod` but set the context to `myObject`:
*/

let myObject = {
  count: 1,
  myChildObject: {
    myMethod() {
      return this.count;
    },
  },
};

console.log(myObject.myChildObject.myMethod.call(myObject));

/*
What does the following code log to the console?
*/

let person = {
  firstName: 'Peter',
  lastName: 'Parker',
  fullName() {
    console.log(this.firstName + ' ' + this.lastName +
                ' is the Amazing Spiderman!');
  },
};

let whoIsSpiderman = person.fullName.bind(person);
whoIsSpiderman();

/*
This will log: Peter Parker is the Amazing Spiderman!

We use `bind` to return a new function whose context is permanently the `person` object.
We then invoke that function, where `this` references the `person` object.
*/

/*
What does the following code log to the console?
*/

let computer = {
  price: 30000,
  shipping: 2000,
  total() {
    let tax = 3000;
    function specialDiscount() {
      if (this.price > 20000) {
        return 1000;
      } else {
        return 0;
      }
    }

    return this.price + this.shipping + tax - specialDiscount();
  }
};

console.log(computer.total());

/*
In sloppy mode, `this.price` is `undefined` as `this` wihtin the `specialDiscount` function references
the `window` or `global` object. undefined > 20000 returns `false`, so `specialDiscount` returns 0.

The `total` method returns 30000 + 2000 + 3000 - 0, as `this` within the `total` method references the `computer`
object, so the use of `this` outside of the `specialDiscount` function works as intended.

Thus, `total` returns 35000, which will be printed to the console.

If we were in strict mode, referencing `this.price` inside `specialDiscount` would instead raise a TypeError.
*/

/*
If you want this program to log 34000, how would you fix it?
*/

/*
We can use `call` to call `specialDiscount` by passing in `this` as the context, where `this` correctly
references the `computer` object in that scope:
*/

let computer = {
  price: 30000,
  shipping: 2000,
  total() {
    let tax = 3000;
    function specialDiscount() {
      if (this.price > 20000) {
        return 1000;
      } else {
        return 0;
      }
    }

    return this.price + this.shipping + tax - specialDiscount.call(this);
  }
};

console.log(computer.total());

/*
We can also use another variable and make `specialDiscount` a closure:
*/

let computer = {
  price: 30000,
  shipping: 2000,
  total() {
    let tax = 3000;
    let self = this;

    function specialDiscount() {
      if (self.price > 20000) {
        return 1000;
      } else {
        return 0;
      }
    }

    return this.price + this.shipping + tax - specialDiscount();
  }
};

console.log(computer.total());

/*
We can also turn `specialDiscount` into a function expression and use bind:
*/

let computer = {
  price: 30000,
  shipping: 2000,
  total() {
    let tax = 3000;
    let specialDiscount = function () {
      if (this.price > 20000) {
        return 1000;
      } else {
        return 0;
      }
    }.bind(this);

    return this.price + this.shipping + tax - specialDiscount();
  }
};

console.log(computer.total());

/*
Lastly, we can turn `specialDiscount` into an arrow function instead:
*/

let computer = {
  price: 30000,
  shipping: 2000,
  total() {
    let tax = 3000;
    let specialDiscount = () => {
      if (this.price > 20000) {
        return 1000;
      } else {
        return 0;
      }
    };

    return this.price + this.shipping + tax - specialDiscount();
  }
};

console.log(computer.total());