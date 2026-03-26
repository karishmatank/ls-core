/*
Implement a function that takes a string and a number times as arguments.
The function should return the string repeated times number of times.
If times is not a number, return undefined.
If it is a negative number, return undefined also.
If times is 0, return an empty string.
You may ignore the possibility that times is a number that isn't an integer.

You may concatenate strings, but you may not use any other properties or methods from JavaScript's built-in String class.

repeat('abc', 1);       // "abc"
repeat('abc', 2);       // "abcabc"
repeat('abc', -1);      // undefined
repeat('abc', 0);       // ""
repeat('abc', 'a');     // undefined
repeat('abc', false);   // undefined
repeat('abc', null);    // undefined
repeat('abc', '  ');    // undefined
*/

function repeat(string, times) {
  if (typeof times !== 'number' || Number.isNaN(times) || times < 0) {
    return undefined;
  }
  if (times === 0) {
    return '';
  }

  let finalString = ''
  for (let iterations = 0; iterations < times; iterations += 1) {
    finalString += string;
  }

  return finalString;
}

console.log(repeat('abc', 2));       // "abcabc"
console.log(repeat('abc', 1));       // "abc"
console.log(repeat('abc', -1));      // undefined
console.log(repeat('abc', 0));       // ""
console.log(repeat('abc', 'a'));     // undefined
console.log(repeat('abc', false));   // undefined
console.log(repeat('abc', null));    // undefined
console.log(repeat('abc', '  '));    // undefined