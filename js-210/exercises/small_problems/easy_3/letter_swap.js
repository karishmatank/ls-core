/*
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word.
You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or
repeated spaces.
*/

function swap(string) {
  let words = string.split(' ');
  let flipped = [];
  for (let word of words) {
    let newWord;
    if (word.length === 1) {
      newWord = word;
    } else {
      newWord = word.slice(-1) + word.slice(1, -1) + word.slice(0, 1);
    }
    flipped.push(newWord);
  }

  return flipped.join(' ');
}

console.log(swap('Oh what a wonderful day it is'));  // "hO thaw a londerfuw yad ti si"
console.log(swap('Abcde'));                          // "ebcdA"
console.log(swap('a'));                              // "a"


/*
How can you refactor this problem using the Array.prototype.map method instead?
*/

function swap(string) {
  let words = string.split(' ');
  let flipped = words.map((word) => swapCharacters(word));
  return flipped.join(' ');
}

function swapCharacters(word) {
  if (word.length === 1) {
    return word;
  }

  return word.slice(-1) + word.slice(1, -1) + word.slice(0, 1);
}