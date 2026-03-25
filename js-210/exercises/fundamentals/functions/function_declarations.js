// What will the following code log to the console and why? Don't run the code until after you have tried to answer.

logValue();

function logValue() {
  console.log('Hello, world!');
}

/*
This will print "Hello, world".

In Javascript, during the creation phase, we hoist function declarations such that we both declare and initialize
`logValue` to the function definition shown in the code. Therefore, when we call `logValue`, we execute
the function body, which prints "Hello, world".
*/

// Let's refactor the code a bit. What does it log now? What is the hoisted equivalent of this code?

var logValue = 'foo';

function logValue() {
  console.log('Hello, world!');
}

console.log(typeof logValue);

/*
The hoisted equivalent is:

function logValue() {
  console.log('Hello, world!');
}

var logValue; // This is basically redundant

logValue = 'foo';

console.log(typeof logValue);


Function definitions are hoisted before variable declarations.
Therefore, we will print `'string'`. We reassign `logValue` to a string value.
*/