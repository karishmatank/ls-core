/*
Q1

false || (true && false); => false
true || (1 + 2); => true
(1 + 2) || true; => 3
true && (1 + 2); => 3
false && (1 + 2); => false
(1 + 2) && true; => true
(32 * 4) >= 129; => false
false !== !true; => false !== (!true) => false
true === 4; => false
false === (847 === '847'); => false === false => true
false === (847 == '847'); => false === true => false
(!true || (!(100 / 5) === 20) || ((328 / 4) === 82)) || false;
    => need to evaluate (!true || (!(100 / 5) === 20) || ((328 / 4) === 82)) first
    => Of that, first evaluate !true, which is false. No short circuit
    => Next, evaluate (!(100 / 5) === 20) => (!(20) === 20) => (false === 20) => false. No shirt circuit
    => Next, evaluate ((328 / 4) === 82) => (82 === 82) => true. Short circuit!
    => true
*/

/*
Q2
Write a function, evenOrOdd, that determines whether its argument is an even number.
If it is, the function should log 'even' to the console; otherwise, it should log 'odd'.
For now, assume that the argument is always an integer.
*/

function evenOrOdd(num) {
  if (num % 2 === 0) {
    console.log('even');
  } else {
    console.log('odd');
  }
}

/*
Q3
Let's improve our previous implementation of evenOrOdd.
Add a validation check to ensure that the argument is an integer.
If it isn't, the function should issue an error message and return.

Hint: Use Number.isInteger()
*/

function evenOrOdd(num) {
  if (!Number.isInteger(num)) {
    console.log('Argument must be number.');
    return;
  }

  if (num % 2 === 0) {
    console.log('even');
  } else {
    console.log('odd');
  }
}

/*
Q4
What does the following code log to the console, and why?
*/

function barCodeScanner(serial) {
  switch (serial) {
    case '123':
      console.log('Product1');
    case '113':
      console.log('Product2');
    case '142':
      console.log('Product3');
    default:
      console.log('Product not found!');
  }
}

barCodeScanner('113');

/*
This will log 'Product2' first. However, because we aren't breaking out, it will keep going
and also log 'Product3' and 'Product not found!'.
*/

/*
Q5

Refactor this statement to use an if statement instead.

return foo() ? 'bar' : qux();

*/

/*
if (foo()) {
  return 'bar';
} else {
  return qux();
}
*/


/*
Q6
What does this code output to the console?

*/

function isArrayEmpty(arr) {
  if (arr) {
    console.log('Not Empty');
  } else {
    console.log('Empty');
  }
}

isArrayEmpty([]);

/*
This will log 'Not Empty'. That is because in JavaScript, an empty array is not falsy.
Therefore, it will pass the if condition and log 'Not Empty'.
*/


/*
Q7

Write a function that takes a string as an argument and returns an all-caps version of
the string when the string is longer than 10 characters.
Otherwise, it should return the original string.
Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.
*/

function capLongStrings(string) {
  return string.length > 10 ? string.toUpperCase() : string;
}

console.log(capLongStrings("Sue Smith"));     // => Sue Smith
console.log(capLongStrings("Sue Robertson")); // => SUE ROBERTSON
console.log(capLongStrings("Joe Thomas"));    // => Joe Thomas
console.log(capLongStrings("Joe Stevens"));   // => JOE STEVENS

/*
Q8

Write a function that logs whether an integer is between 0 and 50 (inclusive),
between 51 and 100 (inclusive), greater than 100, or less than 0.

*/

function numberRange(num) {
  if ((num >= 0) && (num <= 50)) {
    console.log(`${num} is between 0 and 50`);
  } else if (num > 50 && num <= 100) {
    console.log(`${num} is between 51 and 100`);
  } else if (num > 100) {
    console.log(`${num} is greater than 100`);
  } else {
    console.log(`${num} is less than 0`);
  }
}

numberRange(25);
numberRange(75);
numberRange(125);
numberRange(-25);

/* Expected Output
25 is between 0 and 50
75 is between 51 and 100
125 is greater than 100
-25 is less than 0
*/

/*
Q9
Without running this code, what will it print?
*/

console.log(false ?? null);
console.log(true ?? (1 + 2));
console.log((1 + 2) ?? true);
console.log(null ?? false);
console.log(undefined ?? (1 + 2));
console.log((1 + 2) ?? null);
console.log(null ?? undefined);
console.log(undefined ?? null);


// false
// true
// 3
// false
// 3
// 3
// undefined
// null

/*
Q10
Without running this code, what will it print?
*/

function show(foo = undefined, bar = null) {
  console.log(`foo is ${foo ?? 3}, bar is ${bar ?? 42}`);
}

show(5, 7);
show(0, 0);
show(4);
show();

/*
foo is 5, bar is 7
foo is 0, bar is 0
foo is 4, bar is 42
foo is 3, bar is 42
*/