/*
Rot13 ("rotate by 13 places") is a letter-substitution cipher that translates a String into a new String:

For each character in the original String:

- If the character is a letter in the modern English alphabet, change it to the character 13 positions
later in the alphabet. Thus, a becomes n. If you reach the end of the alphabet, return to the beginning.
Thus, o becomes b.
- Letter transformations preserve case. A becomes N while a becomes n.
- Don't modify characters that are not letters.

Write a Function, rot13, that takes a String and returns that String transformed by the rot13 cipher.

console.log(rot13('Teachers open the door, but you must enter by yourself.'));
// logs:
Grnpuref bcra gur qbbe, ohg lbh zhfg ragre ol lbhefrys.

It's worth noting that rot13 applied twice results in the original string:
console.log(rot13(rot13('Teachers open the door, but you must enter by yourself.')));
// logs:
Teachers open the door, but you must enter by yourself.
This happens since there are 26 characters in the modern English alphabet: 2 sets of 13.

*/

const PLACES = 13;
const LOWERCASE_MIN = 'a'.charCodeAt(0);
const UPPERCASE_MIN = 'A'.charCodeAt(0);
const ALPHABET_LENGTH = 'z'.charCodeAt(0) - 'a'.charCodeAt(0) + 1;

function isUpperCaseLetter(char) {
  return char >= 'A' && char <= 'Z';
}

function isLowerCaseLetter(char) {
  return char >= 'a' && char <= 'z';
}

function rotateChar(char) {
  // Get index within alphabet (0 to 25). Then get new index (0 to 25) and convert back to char
  let alphabetMinCode = isLowerCaseLetter(char) ? LOWERCASE_MIN : UPPERCASE_MIN;
  let alphabetIndex = char.charCodeAt(0) - alphabetMinCode;
  let newAlphabetIndex = (alphabetIndex + PLACES) % ALPHABET_LENGTH;
  let newChar = String.fromCharCode(newAlphabetIndex + alphabetMinCode);
  return newChar;
}

function rot13(text) {
  let rotatedString = '';
  for (let char of text) {
    if (isUpperCaseLetter(char) || isLowerCaseLetter(char)) {
      rotatedString += rotateChar(char);
    } else {
      rotatedString += char;
    }
  }
  return rotatedString;
}

console.log(rot13('Teachers open the door, but you must enter by yourself.'));
console.log(rot13(rot13('Teachers open the door, but you must enter by yourself.')));
console.log(rot13(''));
console.log(rot13('123-.*'));