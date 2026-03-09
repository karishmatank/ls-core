// Q1: What does this code log to the console? Does executing the foo function affect the output? Why or why not?

let bar = 1;
function foo() {
  let bar = 2;
}

foo();
console.log(bar);

/*
We'll print the number 1 to the console. Executing the foo function does not affect the output
because we use `let` to declare a local `bar` variable within the scope of `foo`, which is not in scope
when we print `bar` to the console afterwards.
*/

/*
Q2:
In the exercises for the previous chapter, you wrote a dynamic greeter program named greeter.js.
Add a function to this program that solicits the user's first and last names in separate invocations;
the function should return the appropriate name as a string.
Use the return values to greet the user with their full name.
*/

function getName(prompt) {
  let rlSync = require('readline-sync');
  let name = rlSync.question(prompt);
  return name;
}

let firstName = getName("What is your first name? ");
let lastName = getName("What is your last name? ");
console.log(`Hello, ${firstName} ${lastName}!`);

/*
Q3:
Write a program that uses a multiply function to multiply two numbers and returns the result.
Ask the user to enter the two numbers, then output the numbers and result as a simple equation.
*/

function multiply(num1, num2) {
  return num1 * num2;
}

function getNumber(prompt) {
  let rlSync = require('readline-sync');
  return Number(rlSync.question(prompt));
}

let num1 = getNumber("Enter a number: ");
let num2 = getNumber("Enter another number: ");
console.log(`${num1} * ${num2} = ${multiply(num1, num2)}`);

/*
Q4: What does the following code log to the console?
*/

function scream(words) {
  words = words + '!!!!';
  return;
  console.log(words);
}

scream('Yipeee');

/*
This was spoiled a bit, but the answer is it doesn't log anything to the console.
We return from the function before we reach the `console.log`.
*/

/*
Q5: What does the following code log to the console?
*/

function scream(words) {
  return words + '!!!!';
}

scream('Yipeee');

/*
This still doesn't log anything to the console, we don't have any `console.log` anywhere.
*/

/*
Q6: In the code shown below, identify the following items:

the function arguments
the function body
the function declaration
the function invocation
the function name
the function parameters
the function return value
the names of all variables in this program

*/

function multiplyNumbers(num1, num2, num3) {
  let result = num1 * num2 * num3;
  return result;
}

let product = multiplyNumbers(2, 3, 4);

/*
the function arguments => 2, 3, 4 on line 104
the function body => lines 100 and 101
the function declaration => lines 99 to 102
the function invocation => multiplyNumbers(2, 3, 4) on line 104
the function name => multiplyNumbers on line 99
the function parameters => num1, num2, num3 on line 99
the function return value => result on line 101
the names of all variables in this program => multiplyNumbers, num1, num2, num3, result, product
*/

/*
Q7: Without running the following code, what do you think it will output?
*/

function foo(bar, qux) {
  console.log(bar);
  console.log(qux);
}

foo('Hello');

/*
This will assign `bar` to the value `'Hello'` and qux to `undefined`.
Therefore, we'll first print Hello and then undefined.
*/

/*
Q8: Without running the following code, what do you think it will output?
*/

function foo(bar, qux) {
  console.log(bar);
  console.log(qux);
}

foo(42, 3.1415, 2.718);

/*
This will print 42 followed by 3.1415. The 2.718 is ignored.
*/

/*
Q9:
Identify all of the variables named on each line of the following code.
You may assume that question is the name of a built-in function in JavaScript
(it is not, so this code won't work as written).

function multiply(left, right) {
  let product = left * right;
  return product;
}

function getNumber(prompt) {
  return parseFloat(question(prompt));
}

let left = getNumber('Enter the first number: ');
let right = getNumber('Enter the second number: ');
console.log(`${left} * ${right} = ${multiply(left, right)}`);

Variables are:
- line 154: multiply, left, right
- line 155: product, left, right
- line 156: product
- line 159: getNumber, prompt
- line 160: parseFloat, question, prompt
- line 163: left, getNumber
- line 164: right, getNumber
- line 165: console, left, right, multiply, left, right
  - log is the name of a method in the built-in Console object. Therefore, it is a property name
*/

/*
Q10:
Using the code from Exercise 9, classify each variable name as either global or local.
For our purposes here, you may assume that the code from Exercise 9 is the entire program.

- Global:
  multiply,
  getNumber,
  parseFloat,
  question,
  left (from line 163),
  right (from line 163),
  console

- Local:
  left (from line 154),
  right (from line 154),
  product,
  prompt
*/

/*
Q11:
Using the code from Exercise 9, are the left and right variables on lines 1 and 2 the same as the
left and right variables on lines 10-12? Explain your reasoning.

No, they are not. The left and right variables on lines 1 and 2 are local variables to the multiply function,
whereas the left and right variables on lines 10-12 are global variables.

*/