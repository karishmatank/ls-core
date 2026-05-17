/*
Be sure to use Chrome Snippets for this assignment. You can use other browser tools or Node, but we will assume that you're using Chrome. If you do use Node or another browser, you may see different results and even experience errors.
*/

/*
What will the code below output?
*/

function foo() {
  return this;
}

let context = foo();
console.log(context);

/*
We're not in strict mode, so `foo` will return the `window` object or `global` object, which we eventually
print to the console. In node, it's the `global` object
*/

/*
What will the code in the previous question output in strict mode?
*/

/*
In strict mode, we'll print `undefined`
*/

/*
What will the code below output? Explain the difference, if any, between this output and that of problem 1.
*/

let obj = {
  foo() {
    return this;
  },
};

/*let*/ context = obj.foo();

console.log(context);

/*
In this case, when we invoke `foo`, `this` references the `obj` object, `foo` is invoked as: `obj.foo()`.
Therefore, this will return and print the `obj` object to the console.
*/


/*
What will the code below output?
*/

var message = 'Hello from the global scope!';

function deliverMessage() {
  console.log(this.message);
}

deliverMessage();

let bar = {
  message: 'Hello from the function scope!',
};

bar.deliverMessage = deliverMessage;

bar.deliverMessage();

/*
This will print:
Hello from the global scope!
Hello from the function scope!

We technically aren't in strict mode here.
When we declare and assign `message` with the `var` keyword, it is like adding `message` as a property
in the `window` object (assume we are running this in Chrome Snippets).
When we then invoke `deliverMessage`, it will look for the message property in the `window` object,
which means it'll print `'Hello from the global scope!'`.
We then assign an object to `bar` with a `message` property and add on `deliverMessage` property that references
the same function that global variable `deliverMessage` references.
When we invoke `bar.deliverMessage()`, `this` inside `deliverMessage` is referencing the `bar` object.
Thus, the second invocation will print `'Hello from the function scope!'`.

NOTE: If you try to run this in Node, this will print `undefined` for the first print statement.
That is because in Node, the top-level scope is a module, not the global object. `var message = ...` becomes
a variable local to that module.
If we just did `message = ...`, then we would be adding `message` as a property to the `global` object.
*/

/*
What will the code below output? What would happen if we replaced var on line 1 with let?
Can you explain why the output changes?
*/

var a = 10;
let b = 10;
let c = {
  a: -10,
  b: -10,
};

function add() {
  return this.a + b;
}

c.add = add;

console.log(add());
console.log(c.add());

/*
As is, this will print (assuming Google Snippets environment):
20
0

In Node, this will print:
NaN
0

Because we instantiate `a` with the `var` keyword, in Google Snippets, this adds `a` to the `window` object.
(In Node, this just means `a` is local to the module and is not added to the `global` object.)
Later on, we assign the value of `c.add` to the same function that global variable `add` is referencing.
When we invoke `add`, `this` references the `global` or `window` object.
With Google Snippets, this means `window.a`, which has the value 10. With Node, `global.a` is undefined.
`b` just references the variable assigned in the global scope, which is 10. 10 + 10 = 20, or undefined + 10 = NaN.

When we invoke `c.add`, `this` now references the `c` object. Thus, `this.a` has the value -10. `b` still
references the global variable with value 10. Thus, -10 + 10 = 0.

If line 1 used `let` instead, then in Google Snippets we would get NaN and 0. `let` and `const` variables
don't belong to any object.
*/

/*
The problems above all feature implicit function execution context.
What methods have we learned so far that let us explicitly specify what a function's execution context should be?
*/

/*
We've learned about call and apply, which allow us to call functions and pass in context.
*/

/*
In the code below, use call to invoke bar.add as a method but with foo as the execution context.
What will this return?
*/

/*let*/ foo = {
  a: 1,
  b: 2,
};

/*let*/ bar = {
   a: 'abc',
   b: 'def',
   add() {
     return this.a + this.b;
   },
};

console.log(bar.add.call(foo));


/*
Given the code and desired output shown below, should you use call or apply to supply explicit context
and the arguments to outputList?
That is, which method makes the most sense to use?
Implement a solution using your preferred method such that the desired output is logged, and explain your choice.
*/

let fruitsObj = {
  list: ['Apple', 'Banana', 'Grapefruit', 'Pineapple', 'Orange'],
  title: 'A Collection of Fruit',
};

function outputList() {
  console.log(this.title + ':');

  let args = [].slice.call(arguments);

  args.forEach(function(elem) {
    console.log(elem);
  });
}

// invoke outputList here
outputList.apply(fruitsObj, fruitsObj.list);

/*
Desired output:

A Collection of Fruit:
Apple
Banana
Grapefruit
Pineapple
Orange
*/

/*
I think we should use apply here, because the fruits already make up an array.
However, we can easily also just do the below too:

outputList.call(fruitsObj, ...fruitsObj.list);

*/

/*
For an extra challenge, consider this line of code from the previous problem:

let args = [].slice.call(arguments);

Inside of JavaScript functions, arguments is an object that holds all of the arguments passed to the function.
Bearing in mind that the function author wants to iterate over the arguments later in the method using an Array method,
why do you think he or she is invoking call?
*/

/*
This is because we can't invoke `slice` directly on `arguments`, as `arguments` is not a real array.
We can only use `slice` on arrays.
Therefore, we can call `slice` on an empty array but pass in `arguments` as context,
where the inner workings of `slice` probably refer to `this`, which will refer to the context we pass in.
*/
