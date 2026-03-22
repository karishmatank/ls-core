// Q1

function say() {
  if (false) {
    var a = 'hello from inside a block';
  }

  console.log(a);
}

say();

/*
This will print:
undefined

When we invoke `say`, we'll create a separate function scope where `a` is hoisted and initialized to `undefined`.
This is because we declare `a` with the `var` keyword, which has function scope, not block scope.
As a result, even though the if block doesn't run, since `false` is always falsy, JavaScript will print
`undefined` to the console.
*/


// Q2

function say() {
  if (false) {
    let a = 'hello from inside a block';
  }

  console.log(a);
}

say();

/*
In this case, we'll get a ReferenceError.

When we invoke `say`, we first see an if block. The if block never runs as `false` is always falsy,
which means that we never declare the variable `a`. `a` is block scoped because it is declared using the `let`
keyword.

As a result, JavaScript will throw a ReferenceError when we try to log `a` to the console.
*/


// Q3

function hello() {
  a = 'hello';
  console.log(a);

  if (false) {
    var a = 'hello again';
  }
}

hello();
console.log(a);

/*

This will print 'hello' followed by a ReferenceError.

When we invoke `hello`, we first hoist `a` within the function scope, which will be initialized to `undefined`.
We then assign the value 'hello' to `a`. When we log `a` to the console, we'll log `hello`. The if block doesn't
run as `false` is always falsy.

However, `a` is function scoped, meaning it's not accessible in the global scope as we've declared it within
the `hello` function. Therefore, we'll get a ReferenceError in the last line.
*/


// Q4

function hello() {
  a = 'hello';
  console.log(a);

  if (false) {
    let a = 'hello again';
  }
}

hello();
console.log(a);

/*
I think what this behavior depends on is whether we're in strict mode or non-strict mode.

In strict mode, we'll see a ReferenceError because when we try to assign `'hello'` to `a`, `a` isn't defined.
In non-strict mode, JavaScript creates an implicit global variable `a` and assign it `'hello'`. We'll then
print "hello" to the console. The if block never runs as `false` is always falsy. We then will print "hello"
again to the console as per the last line, as `a` is an implicit global variable available to the last line.
*/


// Q5

var a = 'hello';

for (var index = 0; index < 5; index += 1) {
  var a = index;
}

console.log(a);

/*
We'll print 4.
We start by hoisting the declaration of `a`, which is assigned the value `undefined`.
In the execution phase, we then reassign `a` to "hello".
We then iterate through a for loop. Variables defined with the keyword
`var` are function scoped, not block scoped. Therefore, we'll keep reassigning `a` to the values of the indices
we're looping through.

At the end of the loop, `a` will have the value `4`.
That's what will be printed to the console.
*/


// Q6

let a = 'hello';

for (let index = 0; index < 5; index += 1) {
  let a = index;
}

console.log(a);

/*
This will print 'hello'. We declare and initialize a variable `a` using the `let` keyword. We then declare and
initialize a local variable `a` that is block scoped within the for loop. The loop will run, but the global variable `a`
is not affected as the local variable `a` shadows it. Therefore, when we print to the console, we'll print 'hello'.

The `let a = index` declaration isn't an issue because each loop gets a fresh block environment, so the multiple `let`
statements won't raise errors in Javascript.
*/


// Q7

let a = 1;

function foo() {
  a = 2;
  let bar = function() {
    a = 3;
    return 4;
  };

  return bar();
}

console.log(foo());
console.log(a);

/*
We will print:
4
3

During the creation phase, we'll hoist the declaration of `a`, which is declared using the `let` keyword but
remains uninitialized and in the temporal dead zone. We also hoist the declaration and initialization of `foo`.
During the execution phase, we'll immediately assign the value `1` to `a` and then invoke `foo` and log its return
value to the console.

Within `foo`, we first hoist the declaration of `bar`, which starts uninitialized and in the temporal dead zone as it
was declared using the `let` keyword. We then assign the value `2` to the global variable `a`, as we aren't shadowed
by any local variables. We then assign a function to the variable `bar` and immediately invoke it on the following line.

Within `bar`, we assign the value `3` to the global variable `a` as we still have no variables shadowing that global
variable. We then return the value `4`, which is subsequently returned from `foo` as well.

Thus, we print `4` to the console on the `console.log(foo())` line.
Lastly, we print `3` to the console as `a` has the value `3`.
*/


// Q8

var a = 'global';

function checkScope() {
  var a = 'local';
  const nested = function() {
    var a = 'nested';
    let superNested = () => {
      a = 'superNested';
      return a;
    };

    return superNested();
  };

  return nested();
}

console.log(checkScope());
console.log(a);

/*
This will print:
superNested
global

Within each nested function, with the ecxeption of superNested, we declare a variable `a` using `var`, which
is function scoped. That means that the `a` variables that are declared inside the functions are shadowing
the global variable `a`. The only exception is inside superNested, where we reassign the `a` within the `nested`
function scope to `'superNested'`.

Ultimately, we return the string `'superNested'` from `checkScope`. Global variable `a` still has the value
`'global'`.
*/


// Q9

let a = 'outer';
let b = 'outer';

console.log(a);
console.log(b);
setScope(a);
console.log(a);
console.log(b);

function setScope(foo) {
  foo = 'inner';
  b = 'inner';
}

/*
This will print:
outer
outer
outer
inner

During the creation phase, we "hoist" the declarations for `a`, `b`, and `setScope`. `a` and `b` are declared using
the `let` keyword, meaning they remain uninitialized and in the temporal dead zone. Since `setScope` is a function, we
declare and initialize the function.

During the execution phase, we immediately initialize `a` to `'outer'` and `b` to `'outer'`, which are then subsequently
logged to the console. We then invoke `setScope`, passing in `a` as an argument, which parameter `foo` references within
the function body. Since `foo` is a local variable, reassigning the value of `foo` to `'inner'` on the first line
of the function does not impact the global variable `a`. However, we do reassign the global variable `b` to `'inner'`
on the next line.

Thus, when we log the values of `a` and `b` afterwards, we'll print `'outer'` first, as global variable `a` still has
the value `'outer'`, and `'inner'` subsequently, as global variable `b` was reassigned to `'inner'`.
*/


// Q10

let total = 50;
let increment = 15;

function incrementBy(increment) {
  total += increment;
}

console.log(total);
incrementBy(10);
console.log(total);
console.log(increment);

/*
This will print:
50
60
15

The creation phase / hoisting seems straightforward for this one, so I'll gloss over that for now.
We first log `50` as that's the value that `total` was initialized to. When we invoke `incrementBy`, we pass in
a value `10`, which local variable `increment` is assigned to. This local variable shadows the global `increment`
value. We then reassign the global `total` by adding the amount of the local `increment`, which means `total`
is reassigned to `60`. Thus, we print `60` next. Lastly, we print `15` as the local `increment` variable is not
accessible in the global scope- only the global `increment` variable with value `15` is.
*/


// Q11

let a = 'outer';

console.log(a);
setScope();
console.log(a);

var setScope = function () {
  a = 'inner';
};

/*
This will print `'outer'` before JavaScript raises a TypeError.

We'll first "hoist" the declaration for `a`, and `setScope`. `a` starts uninitialized and in the temporal dead zone.
`setScope` is initialized to `undefined` given it was declared using the `var` keyword.

We then initialize `a` to the value `'outer'` and log its value. We try to invoke `setScope`, but `setScope` has
value `undefined`, so that won't work and should raise an error, since we can't invoke `undefined`
*/