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
THIS IS DECODING NOW.


P:
Input: String (encoded), number of rails
Output: String (decoded). Won't have any spaces or anything
Rules:
- How it works
  - The message is decoded by creating the specified number of "rails", which we can think of as rows.
  - We start at the top left.
  - We first need to figure out how many chars go on each rail.
  - Once we figure that out, we place the input chars in each rail
  - Then, we use the zig zag pattern to dcode the message
- Assume the input strings are all just letters. Don't worry about digits, spaces, or other characters
- An empty input string returns an empty output string
- Assume the function is called correctly- 2 inputs always, first is a string and second is a number
- We don't need to preserve case. We may normalize the output to all uppercase or all lowercase
- If rails number <= 0 or NaN or Infinity / -Infinity or not an integer, return an empty string
- If the rail number is 1, we return the input.


Data structures:

Input: String
Output: String

Rails: Nested arrays, with each rail being an array
Chars of the input: Array

Algorithm:

High-level:
- Check that rails number is valid. If not, or if input is an empty string, return empty string
- Find out how many letters go on each rail
- Separate out input into rails based on number of letters per rail
- Iterate through the rails using the zig zag pattern to reform letters into the real string
- Return the real string

HELPER: getNumLettersPerRail(string, numRails) => Array of numbers
- Initialize an empty array `numPerRail`. Add an element of 0 `numRails` times
- Use the `createRailIdxIncrementer` helper from the encode portion to create a new index tracker -> `getNextRailIdx`
- For a range of numbers from 0 to the length of the input string:
  - Invoke `getNextRailIdx` to get the next index
  - Increment the number at `getNextRailIdx` index in `numPerRail` by 1
- Return `numPerRail`

HELPER: getLettersPerRail(string, numPerRail) => Array of substrings
- Initialize `nextStartIdx` to 0
- Iterate through `numPerRail`.
  - For each element of the result, the end index is `nextStartIdx` + the current element and the start index is `nextStartIdx`
  - Use those indices to get a substring of the input string (start index inclusive, end index not inclusive)
  - Store substrings in a new array `lettersPerRail`
  - Reassign `nextStartIdx` to the current end index
- Return `lettersPerRail`

Main algorithm:
- Check that rails number is valid. If not, or if input is an empty string, return empty string
  - Use isRailNumValid from encoding portion
- Find out how many letters go on each rail
  - Use getNumLettersPerRail
- Separate out input into rails based on number of letters per rail
  - Use getLettersPerRail
- Iterate through the rails using the zig zag pattern to reform letters into the real string
  - Initialize `decodedString` to an empty string
  - Use the `createRailIdxIncrementer` helper from the encode portion to create a new index tracker -> `nextRail`
  - For a range of numbers from 0 to the length of the input string:
    - Invoke `nextRail` to get the next rail we should pull a letter from
    - Get letter at 0th index of element at `nextRail`
    - Reassign element at `nextRail` index to a new string that removes the 0th element string
    - Append letter to `decodedString`
- Convert `decodedString` to upper case
- Return `decodedString`


'hoell'
[2, 2, 1]

['ho', 'el', 'l']


'w'
[1, 0]
['', '']



'WECRLTEERDSOEEFEAOCAIVDEN' -> 25 letters
[7, 12, 6]

lastidx = 7
newEnd = 19
['', '', '']

'WEAREDISCOVEREDFLEEATONCE'
*/

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
      (railIdxIncreasing && currentRailIdx === maxIdx) ||
      (!railIdxIncreasing && currentRailIdx === minIdx)
    ) {
      railIdxIncreasing = !railIdxIncreasing;
    }

    return currentRailIdx;
  }
}

function getNumLettersPerRail(string, numRails) {
  let numPerRail = [];
  for (let i = 0; i < numRails; i += 1) {
    numPerRail.push(0);
  }

  let getNextRailIdx = createRailIdxIncrementer(numRails);
  for (let i = 0; i < string.length; i += 1) {
    numPerRail[getNextRailIdx()] += 1;
  }

  return numPerRail;
}

function getLettersPerRail(string, numPerRail) {
  let nextStartIdx = 0;
  let lettersPerRail = numPerRail.map(num => {
    let startIdx = nextStartIdx;
    let endIdx = startIdx + num;
    nextStartIdx = endIdx;
    return string.slice(startIdx, endIdx);
  });

  return lettersPerRail;
}

function decode(string, numRails) {
  if (!isRailNumValid(numRails) || string === '') {
    return '';
  }

  let lettersPerRail = getLettersPerRail(
    string,
    getNumLettersPerRail(string, numRails)
  );

  let decodedString = '';
  let nextRail = createRailIdxIncrementer(numRails);
  for (let i = 0; i < string.length; i += 1) {
    let nextRailIdx = nextRail();

    decodedString += lettersPerRail[nextRailIdx][0];
    lettersPerRail[nextRailIdx] = lettersPerRail[nextRailIdx].slice(1);
  }

  return decodedString.toUpperCase();
}

console.log(decode('WECRLTEERDSOEEFEAOCAIVDEN', 3) === 'WEAREDISCOVEREDFLEEATONCE');
console.log(decode('WECRLTEERDSOEEFEAOCAIVDEN', 1) === 'WECRLTEERDSOEEFEAOCAIVDEN');
console.log(decode('', 1) === '');
console.log(decode('w', 2) === 'W');
console.log(decode('hoell', 3) === 'HELLO');
console.log(decode('HOELL', 3) === 'HELLO');
console.log(decode('hloel', 2) === 'HELLO');
console.log(decode('hello', 0) === '');
console.log(decode('hello', NaN) === '');
console.log(decode('hello', Infinity) === '');
console.log(decode('hello', -Infinity) === '');
console.log(decode('hello', 1.5) === '');