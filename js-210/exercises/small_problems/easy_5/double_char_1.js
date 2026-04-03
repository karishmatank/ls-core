/*
Write a function that takes a string, doubles every character in the string, and returns the result as a new string.
*/

function repeater(string) {
  let result = '';
  for (let char of string) {
    result += char + char;
  }
  return result;
}

console.log(repeater('Hello'));        // "HHeelllloo"
console.log(repeater('Good job!'));    // "GGoooodd  jjoobb!!"
console.log(repeater(''));             // ""