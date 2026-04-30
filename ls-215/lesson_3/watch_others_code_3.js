/*
THIS PROBLEM MATCHES THE LEVEL OF DIFFICULTY OF THE LS216 EXAM.


A collection of spelling blocks has two letters per block, as shown in this list:

B:O   X:K   D:Q   C:P   N:A
G:T   R:E   F:S   J:W   H:U
V:I   L:Y   Z:M

This limits the words you can spell with the blocks to only those words that do not use both letters from any given block. You can also only use each block once.

Write a function that takes a word string as an argument, and returns true if the word can be spelled using the set of blocks, or false otherwise. You can consider the letters to be case-insensitive when you apply the rules.


Input: String
Output: Boolean (true / false)
Rules:
- How this works:
  - We have 13 blocks, as shown above
  - To spell a word, we may pick up some of these blocks
  - When we pick up a block, we may only use one letter from that block. We can't use both letter in a block in the same string. (i.e. if we use B, we can't use O)
  - You can't use that same block again for the string (i.e. if we use B, we can't use B again)
- Assume the input will be a single **word** consisting only of letters.
  - Assume we won't have multiple words in an input
- An input string does not need to use all blocks.
- If we get an empty string as input, return true -> using no blocks is okay
- Assume the function will be called with one string only
- Analysis is case-insensitive
- Effectively, any string length > 13 is an automatic false


Data structures:
Input: String of alpha chars
Output: Boolean (true or false)

Blocks: Nested array -> [['b', 'o'], ['x': 'k'], ...]
Chars: Use array to store individual chars, although might get away with just using a string
Object: Keep track of each block we've used (?)


Algorithm:

High-level:
- Create a const `allBlocks` with nested arrays of letter pairs
- If string is empty, return true
- If string has more than 13 chars, return false
- Convert string to lowercase
- Create a shallow copy of `allBlocks` -> `availableBlocks`
- For each letter in the string:
  - Set `isAvailable` to false
  - Check if we have already used its block. For each block in `availableBlocks`:
    - If char exists inside the block, then
      - mutate `availableBlocks` to remove that block
      - Change `isAvailable` to `true`
      - Break out of loop + move on to next letter in the string
  - If it does not exist inside any block (isAvailable is still false):
    - Return false
- If we get here, return true
*/

const ALL_BLOCKS = [
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

function isBlockWord(string) {
  if (string === '') return true;
  if (string.length > 13) return false;

  string = string.toLowerCase();

  let availableBlocks = [...ALL_BLOCKS];

  for (let idx = 0; idx < string.length; idx += 1) {
    let letter = string[idx];
    let isAvailable = false;

    for (let blockIdx = 0; blockIdx < availableBlocks.length; blockIdx += 1) {
      if (availableBlocks[blockIdx].includes(letter)) {
        availableBlocks.splice(blockIdx, 1);
        isAvailable = true;
        break;
      }
    }

    if (!isAvailable) {
      return false;
    }
  }

  return true;
}


// // Test cases
console.log(isBlockWord('BATCH') === true);      // true
console.log(isBlockWord('BUTCH') === false);      // false
console.log(isBlockWord('jest') === true);       // true

console.log(isBlockWord('') === true);
console.log(isBlockWord('abcdefghijklmnopqrstuvwxyz') === false);
console.log(isBlockWord('a') === true);
console.log(isBlockWord('Ac') === true);
console.log(isBlockWord('aN') === false);
console.log(isBlockWord('aa') === false);
console.log(isBlockWord('bgvxrldfzcjnh') === true)
console.log(isBlockWord('bgvxrldfzcjnha') === false)





/*
My questions:
- I don't get this concept of a block. Do we select a block for a given word, and we can't use the letters in that block for that word? Do we select different blocks for different words?

- Can the string have any non-alpha chars?
- What happens if the string doesn't have any non-alpha chars? Do we just return false?
- Do we need to use all blocks in an input string? (Guess is no)
- Can a string have more than one word?

- What happens if we don't receive an input?
- What happens if the input is not a string? Do we need to worry about that?
- What happens if the input is an empty string?
-
*/



/*
HELPER: isCharValid(char) => returns true / false
- Create a copy of `allBlocks`
-
*/