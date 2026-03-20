// Q1

let a = 'outer';

function testScope() {
  let a = 'inner';
  console.log(a);
}

console.log(a);
testScope();
console.log(a);

/*
This will print:

outer
inner
outer

During the creation phase, we declare a variable `a` using the `let` keyword but leaves it uninitialized,
as well as a function `testScope` with the function body shown in the problem.
During the execution phase, we assign `'outer'` first to the global variable `a`.
We then log the value of `a` to the console, which prints `'outer'`.
We then invoke the `testScope` function, which declares a local variable `a` with the value 'inner' and shadows the
global variable `a`. We then log the value of the local variable `a` to the console, which prints 'inner'.
Lastly, we log the value of `a` to the console from the global scope. Since the global variable `a` is in scope,
we print 'outer'.
*/


// Q2

let a = 'outer';

function testScope() {
  a = 'inner';
  console.log(a);
}

console.log(a);
testScope();
console.log(a);

/*
This will print:

outer
inner
inner

We start out by declaring a global variable `a` with an uninitialized value during the creation phase, as well as
declaring a function `testScope` with the function body shown in the code.
During the execution phase, we assign the string `'outer'` to `a`.
We then print `a` to the console, which prints `'outer'`.
We then invoke `testScope`, which reassigns the global variable `a` to the string `'inner'`. We also log the value
of `a` to the console, which prints `'inner'`.
Lastly, we exit the function and log the value of `a` to the console again, which prints `'inner'` as we reassigned `a`
to the value `'inner'` previously.
*/


// Q3

let basket = 'empty';

function goShopping() {
  function shop1() {
    basket = 'tv';
  }

  console.log(basket);

  let shop2 = function() {
    basket = 'computer';
  };

  const shop3 = () => {
    let basket = 'play station';
    console.log(basket);
  };

  shop1();
  shop2();
  shop3();

  console.log(basket);
}

goShopping();

/*
This will print:

empty
play station
computer

During the creation phase, JavaScript hoists the let variable declaration for `basket` but leaves it uninitialized.
We also register the definition for the `goShopping` function, whose body matches what we have in the code.
During the execution phase, we assign the value `'empty'` to `basket` and then invoke the `goShopping` function.
Within the `goShopping` function:
- `shop1`, `shop2`, and `shop3` declarations are hoisted. `shop1` is hoisted and initialized.
  `shop2` and `shop3` were declared with `let` and `const`, respectively, so they are hoisted but
  left uninitialized and in the temporal dead zone.
- We then execute the code in the function body.
- We log basket first, which prints `'empty'`
- We invoke `shop1`, which reassigns the global variable `basket` to `'tv'`.
- We invoke `shop2`, which reassigns the global variable `basket` to `'computer'`.
- We invoke `shop3`, which creates a local variable `basket` that shadows the global `basket`, sets the local variable
  value to `play station`, and prints that to the console.
- Lastly, we print the value of the global variable `basket` to the console, which will be `'computer'`
*/


// Q4

function hello() {
  a = 'hi';
}

hello();
console.log(a);

/*
We see that we're initializing a variable `a` inside the `hello` function without using a specific keyword.

EDIT: I wasn't sure what would happen. Turns out something different in Node vs Coderpad:
- In strict mode (Coderpad), you can't assign to an undeclared variable. We never declare `a` anywhere, so it throws
  a ReferenceError
- In non-strict mode, Node runs `a = 'hi'` and creates an implicit global variable `a`. That's why `console.log(a)` works
  and would thus print `'hi'`
*/


// Q5

function hello() {
  let a = 'hello';
}

hello();
console.log(a);

/*
We declare and initialize a function `hello` in the creation phase.
We then invoke it in the execution phase, which creates a local variable `a` with the value `hello`.
This is a local variable as variables declared with `let` are block scoped.
When the function `hello` finishes executing, `a` is no longer available.
While we then try to log the value of `a` to the console`, we'll get a ReferenceError, as there are no
variables `a` defined in the outer scope.
*/


// Q6

console.log(a);

var a = 1;

/*
We hoist the declaration of `a`, which initializes it to `undefined` as we've used the `var` keyword.
When we log `a` to the console, it'll print `undefined`.
We then assign the value `1` to `a` afterwards.
*/


// Q7

console.log(a);

let a = 1;

/*
We'll get a ReferenceError.

We hoist the declaration of `a`, but it's unintialized and in a temporal dead zone as we used the `let` keyword
to declare `a`.
We'll then try to log `a` to the console, which doesn't work as we are trying to reference an uninitialized value.
*/


// Q8

console.log(a);

function hello() {
  a = 1;
}

/*
We'll get a ReferenceError.

In the creation phase, we hoist the declaration of `hello`, which is also initialized.
However, we then try to log the value of an `a` variable, which doesn't exist.
*/