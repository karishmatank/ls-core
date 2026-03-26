/*
Implement a function that determines whether a string begins with another string.
If it does, the function should return true, or false otherwise.

let str = 'We put comprehension and mastery above all else';
startsWith(str, 'We');              // true
startsWith(str, 'We put');          // true
startsWith(str, '');                // true
startsWith(str, 'put');             // false

let longerString = 'We put comprehension and mastery above all else!';
startsWith(str, longerString);      // false

You may use the square brackets ([]) to access a character by index (as shown below),
and the length property to find the string length.
However, you may not use any other properties or methods from JavaScript's built-in String class.
*/

function startsWith(string, searchString) {
  if (string.length < searchString.length) {
    return false;
  }

  for (let idx = 0; idx < searchString.length; idx += 1) {
    if (string[idx] !== searchString[idx]) {
      return false;
    }
  }

  return true;
}

let str = 'We put comprehension and mastery above all else';
let longerString = 'We put comprehension and mastery above all else!';
console.log(startsWith(str, 'We'));              // true
console.log(startsWith(str, 'We put'));          // true
console.log(startsWith(str, ''));                // true
console.log(startsWith(str, 'put'));             // false
console.log(startsWith(str, longerString));      // false