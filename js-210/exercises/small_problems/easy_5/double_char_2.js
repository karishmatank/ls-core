/*
Write a function that takes a string, doubles every consonant character in the string, and
returns the result as a new string.
The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.
*/

const VOWELS = ['a', 'e', 'i', 'o', 'u'];

function doubleConsonants(string) {
  let result = '';
  for (let char of string) {
    result += char;
    result += (isConsonant(char) ? char : '');
  }
  return result;
}

function isConsonant(char) {
  return isLetter(char) && !VOWELS.includes(char.toLowerCase());
}

function isLetter(char) {
  return (char >= 'A' && char <= 'Z') || (char >= 'a' && char <= 'z');
}

console.log(doubleConsonants('String'));          // "SSttrrinngg"
console.log(doubleConsonants('Hello-World!'));    // "HHellllo-WWorrlldd!"
console.log(doubleConsonants('July 4th'));        // "JJullyy 4tthh"
console.log(doubleConsonants(''));                // ""
