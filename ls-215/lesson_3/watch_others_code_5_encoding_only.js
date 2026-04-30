/*
Implement encoding and decoding for the rail fence cipher.

The Rail Fence cipher is a form of transposition cipher that gets its name from the way in which it's encoded. It was already used by the ancient Greeks.

In the Rail Fence cipher, the message is written downwards on successive "rails" of an imaginary fence, then moving up when we get to the bottom (like a zig-zag). Finally the message is then read off in rows.

For example, using three "rails" and the message "WE ARE DISCOVERED FLEE AT ONCE", the cipherer writes out:

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
Then reads off:

WECRLTEERDSOEEFEAOCAIVDEN
To decrypt a message you take the zig-zag shape and fill the ciphertext along the rows.

? . . . ? . . . ? . . . ? . . . ? . . . ? . . . ?
. ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
The first row has seven spots that can be filled with "WECRLTE".

W . . . E . . . C . . . R . . . L . . . T . . . E
. ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
Now the 2nd row takes "ERDSOEEFEAOC".

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
Leaving "AIVDEN" for the last row.

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
If you now read along the zig-zag shape you can read the original message.
*/

/*
STARTING WITH ENCODING FIRST!!!


My questions:
- I'm confused on how to think about input / output here
- Which types of characters should we consider from the input string? For example, clearly we encode alphabetical chars. What about spaces, digits, or other chars?
- Should the encoded string "remember" the placement of any non-encoded chars?
- What do we return if we see an empty string?
- Should we always expect to receive 2 inputs? What should we do if we receive fewer / more?
- Will the first argument always be a string, whereas the latter will always be a number? What do we do if the data types don't match?
- Does case matter? In other words, if the original message is a mix of uppercase and lowercase, do we need to retain that case, or should the output be just lowercase / uppercase?
- How should we treat rail numbers that are 0 or negative?
- How should we handle rail numbers that are NaN or Infinity / -Infinity?
- If the rail number is 1, do we just return the original string?
- Is there a minimum or maximum number of rails we should consider? I guess min would be 1? Is there a max length to the input string that we should know about?

P:
Input: String with message, number of rails
Output: String with encoded message

Rules:
- How it works
  - The message is encoded by creating the specified number of "rails", which we can think of as rows.
  - We start at the top left, where we place the first letter.
  - We then move to the next row and one column to the right, where we place the next letter
  - Keep going all the way down to the last rail, one column to the right each time.
  - Once we place a letter at the last rail, we then move back up to the secod to last rail and next column and place a letter there
  - We keep going until we reach the first rail and repeat the entire process over again until we are done placing letters
  - The final encoded string then takes all letters placed in the first rail, ordered from left to right, appends on all letters placed in the second rail from left to right, and so on until we get all letters placed on the last rail from left to right.
- Assume the input strings are all just letters and spaces. Don't worry about digits or other characters
- Ignore spaces when encoding (don't place them on the rails). Return just the encoded letters as one continuous string
- An empty input string returns an empty output string
- Assume the function is called correctly- 2 inputs always, first is a string and second is a number
- We don't need to preserve case. We may normalize the output to all uppercase or all lowercase
- If rails number <= 0 or NaN or Infinity / -Infinity or not an integer, return an empty string

Data structures:
Input: String
Output: String

Each rail: Array
All rails: Nested array of arrays for each rail
Letters of the string: Array


Algorithm:

High-level:
- Check that rails number is valid. If not, return empty string
- Clean up string to remove spaces and convert to uppercase
- If cleaned up string is empty, return empty string
- Parse elements of string into rails
- Merge rails into one big string and return

HELPER: isRailNumValid(number) => boolean
- Return true if rails number > 0 and is an integer and is not NaN or Infinity or -Infinity

HELPER: getRails(string, numRails) => Nested array
- Create nested array structure
  - Create outer array `rails`
  - Add `numRails` number of nested arrays inside `rails`
- Initialize `currentRailIdx` to 0
- Initialize `railIdxIncreasing` to true
- For each letter in the input string:
  - Add letter to the array at the `currentRailIdx` element of `rails`
  - If `railIdxIncreasing` is true:
    - Increment `currentRailIdx` by 1
  - Else:
    - Decrement `currentRailIdx` by 1
  - Check if we need to change the direction of `railIdxIncreasing`.
    - If `railIdxIncreasing` is true and `currentRailIdx` equals `numRails` - 1, then switch `railIdxIncreasing` to false
    - If `railIdxIncreasing` is false and `currentRailIdx` equals 0, then switch `railIdxIncreasing` to true
- Return `rails`

HELPER: mergeRails(rails) => string
- Combine each nested array into one string
- Combine the outer array into one string
- Return final string

Main:
- Clean up string to remove spaces and convert to uppercase
  - Regex: /\s+/g
- If cleaned up string is empty or rails number is not valid, return empty string
  - Use isRailNumValid
- If numRails = 1, return cleaned up string
- Parse elements of string into rails
  - Use getRails
- Merge rails into one big string and return
  - Use mergeRails

*/

// function encode(string, numRails) {

// }


function isRailNumValid(number) {
  return Number.isInteger(number) && number > 0;
}

function getRails(string, numRails) {
  let rails = [];
  for (let idx = 0; idx < numRails; idx += 1) {
    rails.push([]);
  }

  let currentRailIdx = 0;
  let railIdxIncreasing = true;

  string.split('').forEach(letter => {
    rails[currentRailIdx].push(letter);

    if (railIdxIncreasing) {
      currentRailIdx += 1;
    } else {
      currentRailIdx -= 1;
    }

    if (
      (railIdxIncreasing && currentRailIdx === numRails - 1) ||
      (!railIdxIncreasing && currentRailIdx === 0)
    ) {
      railIdxIncreasing = !railIdxIncreasing;
    }
  });

  return rails;

}

function mergeRails(rails) {
  let mergedInnerRails = rails.map(rail => rail.join(''));
  return mergedInnerRails.join('');
}

function encode(string, numRails) {
  let cleanedString = string.replace(/\s+/g, '').toUpperCase();
  if (!isRailNumValid(numRails) || cleanedString === '') return '';
  if (numRails === 1) return cleanedString;

  let rails = getRails(cleanedString, numRails);
  return mergeRails(rails);
}

// console.log(encode('hellow', 3));


console.log(encode('WE ARE DISCOVERED FLEE AT ONCE', 3) === 'WECRLTEERDSOEEFEAOCAIVDEN');
console.log(encode('WEAREDISCOVEREDFLEEATONCE', 3) === 'WECRLTEERDSOEEFEAOCAIVDEN');

// /*
// [[], [], []]
// string idx | rail idx
// 0, 0
// 1, 1
// 2, 2
// 3, 1
// 4, 0
// 5, 1
// 6, 2
// */

console.log(encode('WE ARE DISCOVERED FLEE AT ONCE', 1) === 'WEAREDISCOVEREDFLEEATONCE');
console.log(encode('', 1) === '');
console.log(encode('w', 2) === 'W');
console.log(encode('hello', 3) === 'HOELL');
console.log(encode('hELlo', 3) === 'HOELL');
console.log(encode('hello', 0) === '');
console.log(encode('hello', NaN) === '');
console.log(encode('hello', Infinity) === '');
console.log(encode('hello', -Infinity) === '');
console.log(encode('hello', 1.5) === '');

/*
h   o
 e l
  l
*/

// getRails('HELLOW', 3);
// // [[h, o], [e, l, w], [l]]

// console.log(mergeRails([ [ 'H', 'O' ], [ 'E', 'L', 'W' ], [ 'L' ] ]));



// **********************************************************************
// EDIT: I came up with a better way to keep track of the rail index
// by using closures! See the entire example pasted again below:

/*
Implement encoding and decoding for the rail fence cipher.

The Rail Fence cipher is a form of transposition cipher that gets its name from the way in which it's encoded. It was already used by the ancient Greeks.

In the Rail Fence cipher, the message is written downwards on successive "rails" of an imaginary fence, then moving up when we get to the bottom (like a zig-zag). Finally the message is then read off in rows.

For example, using three "rails" and the message "WE ARE DISCOVERED FLEE AT ONCE", the cipherer writes out:

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
Then reads off:

WECRLTEERDSOEEFEAOCAIVDEN
To decrypt a message you take the zig-zag shape and fill the ciphertext along the rows.

? . . . ? . . . ? . . . ? . . . ? . . . ? . . . ?
. ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
The first row has seven spots that can be filled with "WECRLTE".

W . . . E . . . C . . . R . . . L . . . T . . . E
. ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
Now the 2nd row takes "ERDSOEEFEAOC".

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
Leaving "AIVDEN" for the last row.

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
If you now read along the zig-zag shape you can read the original message.
*/

/*
STARTING WITH ENCODING FIRST!!!


My questions:
- I'm confused on how to think about input / output here
- Which types of characters should we consider from the input string? For example, clearly we encode alphabetical chars. What about spaces, digits, or other chars?
- Should the encoded string "remember" the placement of any non-encoded chars?
- What do we return if we see an empty string?
- Should we always expect to receive 2 inputs? What should we do if we receive fewer / more?
- Will the first argument always be a string, whereas the latter will always be a number? What do we do if the data types don't match?
- Does case matter? In other words, if the original message is a mix of uppercase and lowercase, do we need to retain that case, or should the output be just lowercase / uppercase?
- How should we treat rail numbers that are 0 or negative?
- How should we handle rail numbers that are NaN or Infinity / -Infinity?
- If the rail number is 1, do we just return the original string?
- Is there a minimum or maximum number of rails we should consider? I guess min would be 1? Is there a max length to the input string that we should know about?

P:
Input: String with message, number of rails
Output: String with encoded message

Rules:
- How it works
  - The message is encoded by creating the specified number of "rails", which we can think of as rows.
  - We start at the top left, where we place the first letter.
  - We then move to the next row and one column to the right, where we place the next letter
  - Keep going all the way down to the last rail, one column to the right each time.
  - Once we place a letter at the last rail, we then move back up to the secod to last rail and next column and place a letter there
  - We keep going until we reach the first rail and repeat the entire process over again until we are done placing letters
  - The final encoded string then takes all letters placed in the first rail, ordered from left to right, appends on all letters placed in the second rail from left to right, and so on until we get all letters placed on the last rail from left to right.
- Assume the input strings are all just letters and spaces. Don't worry about digits or other characters
- Ignore spaces when encoding (don't place them on the rails). Return just the encoded letters as one continuous string
- An empty input string returns an empty output string
- Assume the function is called correctly- 2 inputs always, first is a string and second is a number
- We don't need to preserve case. We may normalize the output to all uppercase or all lowercase
- If rails number <= 0 or NaN or Infinity / -Infinity or not an integer, return an empty string

Data structures:
Input: String
Output: String

Each rail: Array
All rails: Nested array of arrays for each rail
Letters of the string: Array


Algorithm:

High-level:
- Check that rails number is valid. If not, return empty string
- Clean up string to remove spaces and convert to uppercase
- If cleaned up string is empty, return empty string
- Parse elements of string into rails
- Merge rails into one big string and return

HELPER: isRailNumValid(number) => boolean
- Return true if rails number > 0 and is an integer and is not NaN or Infinity or -Infinity

HELPER: createRailIdxIncrementer(numRails) => closure
- Set `currentRailIdx`
- Set `railIdxIncreasing`
- Set minIdx to 0
- Set maxIdx to `numRails` - 1
- Create closure. When invoked:
  - If `currentRailIdx` and `railIdxIncreasing` are unset, set them to 0 and true respectively and return `currentRailIdx`
  - If minIdx matches maxIdx, always return minIdx
  - If `railIdxIncreasing` is true:
    - Increment `currentRailIdx` by 1
  - Else:
    - Decrement `currentRailIdx` by 1
  - Check if we need to change the direction of `railIdxIncreasing`.
    - If `railIdxIncreasing` is true and `currentRailIdx` equals `numRails` - 1, then switch `railIdxIncreasing` to false
    - If `railIdxIncreasing` is false and `currentRailIdx` equals 0, then switch `railIdxIncreasing` to true
  - Return `currentRailIdx`


HELPER: getRails(string, numRails) => Nested array
- Create nested array structure
  - Create outer array `rails`
  - Add `numRails` number of nested arrays inside `rails`
- Use `createRailIdxIncrementer` to get our index tracker -> `getNextRailIdx`
- For each letter in the input string:
  - Get the index from `getNextRailIdx`
  - Add letter to the array at that index of `rails`
- Return `rails`

HELPER: mergeRails(rails) => string
- Combine each nested array into one string
- Combine the outer array into one string
- Return final string

Main:
- Clean up string to remove spaces and convert to uppercase
  - Regex: /\s+/g
- If cleaned up string is empty or rails number is not valid, return empty string
  - Use isRailNumValid
- Parse elements of string into rails
  - Use getRails
- Merge rails into one big string and return
  - Use mergeRails

*/

// function encode(string, numRails) {

// }


function isRailNumValid(number) {
  return Number.isInteger(number) && number > 0;
}

function createRailIdxIncrementer(numRails) {
  let currentRailIdx;
  let railIdxIncreasing;
  const minIdx = 0;
  const maxIdx = numRails - 1;

  return function() {
    if (currentRailIdx === undefined || railIdxIncreasing === undefined) {
      currentRailIdx = 0;
      railIdxIncreasing = true;
      return currentRailIdx;
    }

    if (minIdx === maxIdx) return minIdx;

    if (railIdxIncreasing) {
      currentRailIdx += 1;
    } else {
      currentRailIdx -= 1;
    }

    if (
      (railIdxIncreasing && currentRailIdx === numRails - 1) ||
      (!railIdxIncreasing && currentRailIdx === 0)
    ) {
      railIdxIncreasing = !railIdxIncreasing;
    }

    return currentRailIdx;
  }
}

function getRails(string, numRails) {
  let rails = [];
  for (let idx = 0; idx < numRails; idx += 1) {
    rails.push([]);
  }

  let getNextRailIdx = createRailIdxIncrementer(numRails);

  string.split('').forEach(letter => {
    rails[getNextRailIdx()].push(letter);
  });

  return rails;

}

function mergeRails(rails) {
  let mergedInnerRails = rails.map(rail => rail.join(''));
  return mergedInnerRails.join('');
}

function encode(string, numRails) {
  let cleanedString = string.replace(/\s+/g, '').toUpperCase();
  if (!isRailNumValid(numRails) || cleanedString === '') return '';

  let rails = getRails(cleanedString, numRails);
  return mergeRails(rails);
}

// console.log(encode('hellow', 3));


console.log(encode('WE ARE DISCOVERED FLEE AT ONCE', 3) === 'WECRLTEERDSOEEFEAOCAIVDEN');
console.log(encode('WEAREDISCOVEREDFLEEATONCE', 3) === 'WECRLTEERDSOEEFEAOCAIVDEN');

// // /*
// // [[], [], []]
// // string idx | rail idx
// // 0, 0
// // 1, 1
// // 2, 2
// // 3, 1
// // 4, 0
// // 5, 1
// // 6, 2
// // */

console.log(encode('WE ARE DISCOVERED FLEE AT ONCE', 1) === 'WEAREDISCOVEREDFLEEATONCE');
console.log(encode('', 1) === '');
console.log(encode('w', 2) === 'W');
console.log(encode('hello', 3) === 'HOELL');
console.log(encode('hELlo', 3) === 'HOELL');
console.log(encode('hello', 0) === '');
console.log(encode('hello', NaN) === '');
console.log(encode('hello', Infinity) === '');
console.log(encode('hello', -Infinity) === '');
console.log(encode('hello', 1.5) === '');

/*
h   o
 e l
  l
*/

// getRails('HELLOW', 3);
// // [[h, o], [e, l, w], [l]]

// console.log(mergeRails([ [ 'H', 'O' ], [ 'E', 'L', 'W' ], [ 'L' ] ]));