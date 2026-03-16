/*
Q1:
What does this code log to the console? Why?
*/

let array1 = [1, 2, 3];
let array2 = array1;
array1[1] = 4;
console.log(array2);

/*
This prints [1, 4, 3]. `array2` is referencing the same array in memory as is `array1`.
Therefore, when we mutate that array, it's reflected if we were to print `array1` or `array2`.
*/

/*
Q2:
What do the following error message and stack trace tell you?

$ node exercise2.js
/Users/wolfy/tmp/exercise2.js:4
  console.log(greeting);
              ^

ReferenceError: greeting is not defined
    at hello (/Users/wolfy/tmp/exercise2.js:4:15)
    at Object.<anonymous> (/Users/wolfy/tmp/exercise2.js:13:1)
    at Module._compile (internal/modules/cjs/loader.js:721:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:732:10)
    at Module.load (internal/modules/cjs/loader.js:620:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:560:12)
    at Function.Module._load (internal/modules/cjs/loader.js:552:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:774:12)
    at executeUserCode (internal/bootstrap/node.js:342:17)
    at startExecution (internal/bootstrap/node.js:276:5)


This tells us that we are trying to reference a variable `greeting` that doesn't actually exist.
As a result, we see a `ReferenceError` when we try to reference `greeting` within `console.log(greeting)`.

*/

/*
Q3:
Write some code to output the square root of 37.
*/

console.log(Math.sqrt(37));

/*
Q4:
Given a list of numbers, write some code to find and display the largest numeric value in the list.

List	           Max
1, 6, 3, 2	     6
-1, -6, -3, -2	 -1
2, 2	           2

*/
function getMax(array) {
  let maxNum = null;
  array.forEach((num) => {
    if (!maxNum || num > maxNum) {
      maxNum = num;
    }
  });
  return maxNum;
}

console.log(getMax([1, 6, 3, 2]));
console.log(getMax([-1, -6, -3, -2]));
console.log(getMax([2, 2]));

/* EDIT: The above works, but there is also Math.max()
Math.max(1, 6, 3, 2) for example
*/

/*
Q5:
What does the following function do?
*/

function doSomething(string) {
  return string.split(' ').reverse().map((value) => value.length);
}

/*
This function takes as input a string, splits it into an array of elements basd on a single space character,
reverses the order of the resulting words, and then creates a new array where each element is the length
of the word at the corresponding index of the reversed array of words.

We then return that array.
*/

/*
Q6:
Write a function that searches an array of strings for every element that
matches the regular expression given by its argument.
The function should return all matching elements in an array.
*/

function allMatches(stringArray, pattern) {
  return stringArray.filter((word) => pattern.test(word));
}

let words = [
  'laboratory',
  'experiment',
  'flab',
  'Pans Labyrinth',
  'elaborate',
  'polar bear',
];

console.log(allMatches(words, /lab/)); // => ['laboratory', 'flab', 'elaborate']

/*
Q7:
What is exception handling and what problem does it solve?


Exception handling lets us catch and handle errors that may occur in our code
without crashing our code. It solves the problem of unanticipated errors having unforeseen consequences,
such as a data source that we can't connect to for some reason.
*/

/*
Q8:

This exercise has nothing to do with this chapter. Instead, it uses concepts you learned earlier in the book.
If you can't figure out the answer, don't worry: this question can stump developers with more experience than you have.

Earlier, we learned that Number.isNaN(value) returns true if value is the NaN value, false otherwise.
You can also use Object.is(value, NaN) to make the same determination.

Without using either of those methods, write a function named isNotANumber that returns true if the value
passed to it as an argument is NaN, false if it is not.
*/

function isNotANumber(arg) {
  // If the argument is not a number data type, return false
  if (!(typeof arg === 'number')) {
    return false;
  }

  // Let's try to convert the argument to a string
  let stringArg = String(arg);
  return stringArg === 'NaN';
}

console.log(isNotANumber(''));
console.log(isNotANumber({}));
console.log(isNotANumber(3));
console.log(isNotANumber(false));
console.log(isNotANumber(NaN));

/*
The correct solution is below:

function isNotANumber(value) {
  return value !== value;
}

NaN is the only JS value that is not === to itself.

The solution above just does unnecessary string stuff.
*/

/*
Q9:
This exercise has nothing to do with this chapter. Instead, it uses concepts you learned earlier in the book.
If you can't figure out the answer, don't worry: this question can stump developers with more experience than you have.

Earlier, we learned that JavaScript has multiple versions of the numeric value zero.
In particular, it has 0 and -0. While it's mathematically nonsensical to distinguish between 0 and -0,
they are distinct values in JavaScript. We won't get into why JavaScript has a 0 and -0, but it can be useful in some cases.

There's a problem, however: JavaScript itself doesn't seem to realize that the values are distinct:

> 0 === -0
= true

> String(-0)
= '0'

Fortunately, you can use Object.is to determine whether a value is -0:

> let value = -0;
> Object.is(value, 0)
= false

> Object.is(value, -0)
= true

There are other ways to detect a -0 value.
Without using Object.is, write a function that will return true if the argument is -0,
and false if it is 0 or any other number.

HINT: What happens if you divide a non-zero integer by zero? Apply this to the problem of determining whether a value is -0.
*/

function isNegativeZero(num) {
  // I'll take the hint
  let result = 1 / num;
  if (result === -Infinity) {
    return true;
  }
  return false;
}

console.log(isNegativeZero(0));
console.log(isNegativeZero(-0));

/*
Q10:
This exercise has nothing to do with this chapter. Instead, it uses concepts you learned earlier in the book.
If you can't figure out the answer, don't worry: this question can stump developers with more experience than you have.

Consider this code:
> let x = "5"
> x = x + 1
= "51"

Now, consider this code:
> let y = "5"
> y++

What gets returned by y++ in the second snippet, and why?

*/

/*
I think that Javascript will coerce "5" into an integer and return the number 6.
I am guessing this because ++ is only used with integers. It is possible it will raise a TypeError,
but Javascript tends to just coerce things when it can try to instead of raising an error.

EDIT: I just tried it, it just coerces the input into an integer rather than incrementing it.
So it just returns 5. This is why: "the return value is 5 since the post-increment operator (y++)
returns the original value of y, not the incremented value."
*/