/*
Write a function called swap that takes a string as an argument, and returns a new string, where the alphabetic characters have taken the place of the numeric characters, and vice versa.


My questions:
- Will the strings only have alphabetical and numeric chars? What about other chars? How do we treat those?
- Will we always receive one string? What about if we receive another data type? What about if we receive 0 or more than 1 argument?
- What happens if we receive an empty input?
- If we receive a string with all alpha or other chars, do we just return the same string? Similar question if we receive a string with all digits or other chars?
- Does "first" imply going from left to right to figure out which the first letters are, and the first numbers are, and then swapping them? Just wanted to check on the ordering
- Does case matter?


P:
Input: string
Output: string
Rules:
- The output swaps alphabetic character placement for those of numeric characters
- We'll take the first alpha char we see and swap its placement with the first digit we see, second alpha char with the second digit, etc.
  - "First" is based on normal left to right ordering
- If we have more alpha char than digits, we may not swap all alpha chars. We only swap the first N alpha chars, where N is the number of digits
  - Similar concept if we have more digits than alpha chars
- Non alpha or digit chars may be present- Add them in the same positions as they were originally
- Assume an argument will always be provided. Don't need to handle missing args, extra args, non-string types
- If we receive an empty string, return an empty string
- If we receive a string with all alpha or other chars, return the same string, Similar concept if we receive a string with all digits or other chars
- Case is preserved- Preserve any uppercase letters, but they are switched as well

Data structures:
Input: string
Output: string

Keep track of indices of alpha chars -> Array, ordered in appearance from left to right
Keep track of indices of digits -> Array, ordered in appearance from left to right


Algorithm:

HELPER: getAlphaIndices(string) -> Array of numbers (indices)
- Convert string to lowercase
- Set `indices` to empty array
- For each character of the string:
  - If it is between 'a' and 'z' inclusive, add its index to `indices`
- Return `indices`

HELPER: getDigitIndices(string) -> Array of numbers (indices)
- Set `indices` to empty array
- For each character of the string:
  - If it is between '0' and '9' inclusive, add its index to `indices`
- Return `indices`

High-level:
- If we get an empty string, return an empty string
- Find all indices of alpha chars (upper and lower case) -> Store in `alphaIndices`
  - Use getAlphaIndices
- Find all indices of digits -> Store in `digitIndices`
  - Use getDigitIndices

- If `alphaIndices` is empty or `digitIndices` is empty, return the input

- Set swappedString to empty string
- Loop through each char of the input:
  - Set new variable `referenceIndices`
  - If the char is alpha:
    - Reassign `referenceIndices` to  `digitIndices`
  - If the char is digit:
    - Reassign `referenceIndices` to  `alphaIndices`
  - If `referenceIndices` is undefined (neither alpha or digit) or `referenceIndices` is empty:
    - Append the char to `swappedString`, move on to next iteration

  - Get the first digit seen -> leftmost element of `referenceIndices`
  - Get the char at that index from input
  - Append that char to end of `swappedString`
  - Mutate `referenceIndices` to remove the leftmost element
- Return `swappedString`

*/

function getAlphaIndices(string) {
  string = string.toLowerCase();
  let indices = [];
  string.split('').forEach((char, idx) => {
    if (char >= 'a' && char <= 'z') {
      indices.push(idx);
    }
  });
  return indices;
}

function getDigitIndices(string) {
  let indices = [];
  string.split('').forEach((char, idx) => {
    if (char >= '0' && char <= '9') {
      indices.push(idx);
    }
  });
  return indices;
}

function swap(str) {
  if (str === '') return '';

  let alphaIndices = getAlphaIndices(str);
  let digitIndices = getDigitIndices(str);

  if (alphaIndices.length === 0 || digitIndices.length === 0) {
    return str;
  }

  let swappedString = '';
  str.split('').forEach(char => {
    let referenceIndices;
    if (char.toLowerCase() >= 'a' && char.toLowerCase() <= 'z') {
      referenceIndices = digitIndices;
    } else if (char >= '0' && char <= '9') {
      referenceIndices = alphaIndices;
    }

    if (referenceIndices === undefined || referenceIndices.length === 0) {
      swappedString += char;
    } else {
      let firstSeen = referenceIndices[0];
      let newChar = str[firstSeen];
      swappedString += newChar;
      referenceIndices.splice(0, 1);
    }
  });

  return swappedString;
}

console.log(swap("1a2b3c") === "a1b2c3"); // true
console.log(swap("abcd123") === "123dabc"); // true
console.log(swap("1234abc") === "abc4123");
console.log(swap("1a-2b-3c") === "a1-b2-c3");
console.log(swap("1a 2b 3c") === "a1 b2 c3");
console.log(swap('') === '');
console.log(swap("abc") === "abc");
console.log(swap("-a1b2") === "-1a2b");
console.log(swap("abc--$") === "abc--$");
console.log(swap("123") === "123");
console.log(swap("123--$") === "123--$");
console.log(swap("1A2b3c") === "A1b2c3");
console.log(swap("1A2B3c") === "A1B2c3");


/*

1a-2b-3c

alpha -> [1, 4, 7]
digits -> [0, 3, 6]


alpha -> [4, 7]
digits -> [3, 6]

'a1'
*/
