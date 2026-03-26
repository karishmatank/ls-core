/*
Write a function that takes two arguments:

1. a string to be split
2. a delimiter character

The function logs the split strings to the console, as shown below:

function splitString(string, delimiter) {
  // …
}

splitString('abc,123,hello world', ',');
// logs:
// abc
// 123
// hello world

splitString('hello');
// logs:
// ERROR: No delimiter

splitString('hello', '');
// logs:
// h
// e
// l
// l
// o

splitString('hello', ';');
// logs:
// hello

splitString(';hello;', ';');
// logs:
//  (this is a blank line)
// hello

You may use the square brackets ([]) to access a character by index (as shown below),
and the length property to find the string length.
However, you may not use any other properties or methods from JavaScript's built-in String class.
*/

function splitString(string, delimiter) {
  if (delimiter === undefined) {
    console.log('ERROR: No delimiter');
    return;
  }

  let substring = '';
  for (let idx = 0; idx < string.length; idx += 1) {
    if (delimiter === '') {
      console.log(string[idx]);
    } else if (string[idx] !== delimiter) {
      substring += string[idx];
    } else {
      console.log(substring);
      substring = '';
    }
  }

  if (substring) {
    console.log(substring);
  }
}

splitString('abc,123,hello world', ',');
// logs:
// abc
// 123
// hello world

splitString('hello');
// logs:
// ERROR: No delimiter

splitString('hello', '');
// logs:
// h
// e
// l
// l
// o

splitString('hello', ';');
// logs:
// hello

splitString(';hello;', ';');
// logs:
//  (this is a blank line)
// hello