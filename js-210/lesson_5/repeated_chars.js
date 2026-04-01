/*
Implement a function that takes a String as an argument and returns an object that contains a count
of the repeated characters.

Note that repeatedCharacters does a bit more than simply count the frequency of each character:
it determines the counts, but only returns counts for characters that have a count of 2 or more.
It also ignores the case.
*/

function repeatedCharacters(str) {
  let allCharCounts = {};
  let lowerCaseStr = str.toLowerCase();

  for (let char of lowerCaseStr) {
    if (Object.keys(allCharCounts).includes(char)) {
      allCharCounts[char] += 1;
    } else {
      allCharCounts[char] = 1;
    }
  }

  let filteredCharCounts = {};
  for (let char in allCharCounts) {
    if (allCharCounts[char] >= 2) {
      filteredCharCounts[char] = allCharCounts[char];
    }
  }

  return filteredCharCounts;

}

console.log(repeatedCharacters('Programming'));    // { r: 2, g: 2, m: 2 }
console.log(repeatedCharacters('Combination'));    // { o: 2, i: 2, n: 2 }
console.log(repeatedCharacters('Pet'));            // {}
console.log(repeatedCharacters('Paper'));          // { p: 2 }
console.log(repeatedCharacters('Baseless'));       // { s: 3, e: 2 }
