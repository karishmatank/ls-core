/*
Write a function that takes a string argument containing one or more words and returns a new string containing the
words from the string argument.
All five-or-more letter words should have their letters in reverse order.
The string argument will consist of only letters and spaces. Words will be separated by a single space.
*/

function reverseWords(string) {
  let result = string.split(' ');

  // Method 1: With for loop
  // for (let idx = 0; idx < result.length; idx += 1) {
  //   let word = result[idx];
  //   if (word.length >= 5) {
  //     result[idx] = word.split('').reverse().join('');
  //   }
  // }
  // return result.join(' ');

  // Method 2: With map
  return result.map(
    (word) => word.length >= 5 ? word.split('').reverse().join('') : word
  ).join(' ');
}

console.log(reverseWords('Professional'));             // "lanoisseforP"
console.log(reverseWords('Walk around the block'));    // "Walk dnuora the kcolb"
console.log(reverseWords('Launch School'));            // "hcnuaL loohcS"