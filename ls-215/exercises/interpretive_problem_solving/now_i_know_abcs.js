// Your code goes here
/*
A collection of spelling blocks has two letters per block, as shown in this list:
B:O   X:K   D:Q   C:P   N:A
G:T   R:E   F:S   J:W   H:U
V:I   L:Y   Z:M

This limits the words you can spell with the blocks to only those words that do not use both letters from any given block. You can also only use each block once.

Write a function that takes a word string as an argument and returns true if the word can be spelled using the set of blocks, false otherwise. You can consider the letters to be case-insensitive when you apply the rules.


My questions:
- Is my understanding correct?
  - We must be able to spell the input word with unique blocks
  - We can't use a block more than once (can't have repeating letters)
  - We can't use the other letter on a block if we've already used the block (can't use B if we've already used an O)
- What happens if we receive an empty string?
- Is it correct to think that our string can only be at most 13 chars long?
  - Actually, might we receive other chars in our input string? If so, do we just ignore them or are there rules for those too?
- Will we always receive exactly 1 argument? Not 0 or > 1?
- Will we always receive a string as input?
- If we receive a string with only one alphabetical char, is that automatically just true?
- If we receive a string with no alphabetic chars, what do we return?
-



Input: String
Output: Boolean
Rules:
- We must be able to spell the input word with unique blocks
  - We can't use a block more than once (can't have repeating letters)
  - We can't use the other letter on a block if we've already used the block (can't use B if we've already used an O)
- Analysis is case-insensitive
- If we receive an empty string, return true
- Input will be an alphabetic string- no digits, spaces, punctuation
- We will receive exactly 1 argument, and it will always be a string


Data structures:
- Blocks -> Nested array
- List of blocks we have available -> Nested array (excludes blocks already used)


Algorithm:

HELPER: getBlockIdx(letter, availableBlocks) -> Index if exists, otherwise -1
- For each subarray in `availableBlocks`:
  - If the letter is in subarray, return index of the subarray
- If we get here, return -1

Main:
- Set const `BLOCKS` to an nested array with the block letters (lowercase letters)
- Convert input to lowercase
- Set `availableBlocks` to a copy of the `BLOCKS` array
- For each char in the input:
  - Check if the char is in any of the arrays in `availableBlocks`
    - Use getBlockIdx
  - If not (result index is -1), return false
  - If so (result index is not -1), remove the relevant block from `availableBlocks` based on index #

- If we get here, return true

*/

const BLOCKS = [
  ['b', 'o'],
  ['x', 'k'],
  ['d', 'q'],
  ['c', 'p'],
  ['n', 'a'],
  ['g', 't'],
  ['r', 'e'],
  ['f', 's'],
  ['j', 'w'],
  ['h', 'u'],
  ['v', 'i'],
  ['l', 'y'],
  ['z', 'm']
]

function getBlockIdx(letter, availableBlocks) {
  for (let idx = 0; idx < availableBlocks.length; idx += 1) {
    let block = availableBlocks[idx];
    if (block.includes(letter)) {
      return idx;
    }
  }
  return -1;
}

function isBlockWord(input) {
  input = input.toLowerCase();

  let availableBlocks = [...BLOCKS];
  for (let char of input) {
    let blockIdx = getBlockIdx(char, availableBlocks);
    if (blockIdx === -1) {
      return false;
    }
    availableBlocks.splice(blockIdx, 1);
  }

  return true;
}

console.log(isBlockWord('BATCH') === true);      // true
console.log(isBlockWord('BUTCH') === false);      // false
console.log(isBlockWord('jest') === true);       // true

console.log(isBlockWord('') === true);
console.log(isBlockWord('bb') === false);
console.log(isBlockWord('bo') === false);
console.log(isBlockWord('b') === true);
console.log(isBlockWord('bXdcngrfjhvlz') === true);
console.log(isBlockWord('bXdcngrfjhvlzx') === false);
console.log(isBlockWord('bXdcngrfjhvlzk') === false);


/*

B:O   X:K   D:Q   C:P   N:A
G:T   R:E   F:S   J:W   H:U
V:I   L:Y   Z:M

BLOCKS = [
  ['b', 'o'],
  ['x', 'k'],
  ['d', 'q'],
  ['c', 'p'],
  ['n', 'a'],
  ['g', 't'],
  ['r', 'e'],
  ['f', 's'],
  ['j', 'w'],
  ['h', 'u'],
  ['v', 'i'],
  ['l', 'y'],
  ['z', 'm']
]

availableBlocks = [
  ['x', 'k'],
  ['d', 'q'],
  ['n', 'a'],
  ['r', 'e'],
  ['f', 's'],
  ['j', 'w'],
  ['v', 'i'],
  ['l', 'y'],
  ['z', 'm']
]

'butch'


*/
