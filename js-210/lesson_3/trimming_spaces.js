/*
Write a function that takes a string as an argument, and returns the string stripped of spaces from both ends.
Do not remove or alter internal spaces.

trim('  abc  ');  // "abc"
trim('abc   ');   // "abc"
trim(' ab c');    // "ab c"
trim(' a b  c');  // "a b  c"
trim('      ');   // ""
trim('');         // ""

You may use the square brackets ([]) to access a character by index (as shown below),
and the length property to find the string length.
However, you may not use any other properties or methods from JavaScript's built-in String class.

'hello'[0];       // "h"
'hello'[4];       // "o"
*/

// This was written before I realized I can't use any built-in string methods...
// I thought I just couldn't use `trim`
function trim(string) {
  // Trim the left side first
  while (string[0] === ' ') {
    string = string.slice(1);
  }

  // Next, trim the right side
  while (string[string.length - 1] === ' ') {
    string = string.slice(0, string.length - 1);
  }

  return string;
}


// Rewrite without using any built-in string methods...
function trim(string) {
  let newString = ''

  // Trim the left side first
  // Following their hint about a `copyMode`
  let copyMode = false;
  for (let idx = 0; idx < string.length; idx += 1) {
    if (string[idx] !== ' ') {
      copyMode = true;
    }
    if (copyMode) {
      newString += string[idx];
    }
  }

  // Trim the right side
  copyMode = false;
  string = newString;
  newString = '';
  
  for (let idx = string.length - 1; idx >= 0; idx -= 1) {
    if (string[idx] !== ' ') {
      copyMode = true;
    }

    if (copyMode) {
      newString = string[idx] + newString;
    }
  }

  return newString;

}

console.log(trim('  abc  '));  // "abc"
console.log(trim('abc   '));   // "abc"
console.log(trim(' ab c'));    // "ab c"
console.log(trim(' a b  c'));  // "a b  c"
console.log(trim('      '));   // ""
console.log(trim(''));         // ""