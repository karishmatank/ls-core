/*
Modify the wordSizes function from the previous exercise to exclude non-letters when determining word size.
For instance, the word size of "it's" is 3, not 4.
*/

function wordSizes(string) {
  let words = string.split(' ').map((word) => cleanedWord(word));
  let counts = {};
  for (let word of words) {
    if (!word) {
      continue;
    }

    counts[word.length] = counts[word.length] || 0;
    counts[word.length] += 1;
  }
  return counts;
}

function cleanedWord(word) {
  return word.replace(/[^a-zA-Z]/g, '');
}

console.log(wordSizes('Four score and seven.'));                       // { "3": 1, "4": 1, "5": 2 }
console.log(wordSizes('Hey diddle diddle, the cat and the fiddle!'));  // { "3": 5, "6": 3 }
console.log(wordSizes("What's up doc?"));                              // { "5": 1, "2": 1, "3": 1 }
console.log(wordSizes(''));                                            // {}
