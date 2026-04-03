/*
Write a function that takes a string consisting of one or more space separated words and
returns an object that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

Examples:
*/

function wordSizes(string) {
  let words = string.split(' ');
  let counts = {};
  for (let word of words) {
    if (!word) {
      continue;
    }

    let wordLength = String(word.length);

    if (Object.keys(counts).includes(wordLength)) {
      counts[wordLength] += 1;
    } else {
      counts[wordLength] = 1;
    }

  }
  return counts;
}

// We can do this without using Object.keys, as that returns an array of strings, which is why
// we need to cast the word length to string:
function wordSizes(string) {
  let words = string.split(' ');
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

console.log(wordSizes('Four score and seven.'));                       // { "3": 1, "4": 1, "5": 1, "6": 1 }
console.log(wordSizes('Hey diddle diddle, the cat and the fiddle!'));  // { "3": 5, "6": 1, "7": 2 }
console.log(wordSizes("What's up doc?"));                              // { "2": 1, "4": 1, "6": 1 }
console.log(wordSizes(''));                                            // {}