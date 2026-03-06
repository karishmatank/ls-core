// Q1: Concatenate two or more strings, one with a first name, another one with a last name
let full_name = 'John' + ' ' + 'Doe';
console.log(full_name);

// Q2: Get the individual digits of a number 4936 using arithmetic operators
let num = 4936;
let factor = 10;

while (num != 0) {
  let digit = num % factor;
  console.log(digit);
  num = (num - digit) / 10;
}

/*
Q3: Identify the data type for each of the following:
- 'true': String
- false: Boolean
- 1.5: Number
- 2: Number
- undefined: Undefined
- { foo: 'bar' }: Object
*/

/*
Q4: Explain why this code logs '510' instead of 15:

console.log('5' + 10);

This is because JavaScript sees a string and the + operator, which means it'll do a string concatenation.
Thus, it implicitly coerces 10 into a string first and then concatenates '5' and '10'.
This results in '510'.

*/

// Q5: Refactor the code from Q4 to use explicit coercion so that it logs 15 instead
console.log(Number('5') + 10);

// Q6: Use the template literal syntax along with the expression Number('5') + 10
// to log the following sentence: The value of 5 + 10 is 15.

console.log(`The value of 5 + 10 is ${Number('5') + 10}.`)

// Q7: Will the following code raise an error?
let foo = ['a', 'b', 'c'];
console.log(foo.length); // => 3
console.log(foo[3]); // will this result in an error?

// I want to say that it won't and that it will just silently fail and say either NaN or undefined
// This is a guess based on how JavaScript has had silent failures throughout the chapter.

// Edit: Answer is `undefined`

// Q8: Create an array named `names` that contains a list of pet names
let names = [
  'Asta',
  'Butterscotch',
  'Pudding',
  'Neptune',
  'Darwin'
];

// Q9: Create an object named `pets` that contains pet names and animal type
let pets = {
  Asta: 'dog',
  Butterscotch: 'cat',
  Pudding: 'cat',
  Neptune: 'fish',
  Darwin: 'lizard',
};

// Q10: What does the following evaluate to?
// 'foo' === 'Foo'
// This evaluates to the boolean value false, because of differences in case.

// Q11: What does the following evaluate to?
// parseInt('3.1415')
// This evaluates to the number 3, because we are only parsing the integer.

// Q12: What does the following evaluate to?
// '12' < '9'
// I think this evaluates as true. In Python, it certainly would be true because of
// lexicographical comparison
// Edit: Correct, this is true