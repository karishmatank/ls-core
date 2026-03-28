/*
Given a string that consists of some words and an assortment of non-alphabetic characters,
write a function that returns that string with all of the non-alphabetic characters replaced by spaces.
If one or more non-alphabetic characters occur in a row, you should only have one space in the result
(i.e., the result string should never have consecutive spaces).

Example:
cleanUp("---what's my +*& line?");    // " what s my line "
*/

function cleanUp(text) {
  let result = '';
  for (let char of text) {
    if (char.toLowerCase() >= 'a' && char.toLowerCase() <= 'z') {
      result += char;
    } else if (result[result.length - 1] !== ' ') {
      // Case whether last char in result is non-existent (undefined) or anything other than ' '
      result += ' ';
    }
  }
  return result;
}

console.log(cleanUp("---what's my +*& line?") === ' what s my line '); // " what s my line "