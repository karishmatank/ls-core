/*
Write a function that takes a string argument and returns a new string that contains the value of the
original string with all consecutive duplicate characters collapsed into a single character.

Examples:
crunch('ddaaiillyy ddoouubbllee');    // "daily double"
crunch('4444abcabccba');              // "4abcabcba"
crunch('ggggggggggggggg');            // "g"
crunch('a');                          // "a"
crunch('');                           // ""
*/

function crunch(string) {
  let dedupedString = '';
  for (let char of string) {
    // If we are at the beginning or
    // the current char does not match the last deduped char,
    // then add the char to the deduped string
    if (!dedupedString || dedupedString[dedupedString.length - 1] !== char) {
      dedupedString += char;
    }
  }
  return dedupedString;
}

console.log(crunch('ddaaiillyy ddoouubbllee'));    // "daily double"
console.log(crunch('4444abcabccba'));              // "4abcabcba"
console.log(crunch('ggggggggggggggg'));            // "g"
console.log(crunch('a'));                          // "a"
console.log(crunch(''));                           // ""