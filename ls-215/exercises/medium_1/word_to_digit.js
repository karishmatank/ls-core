/*
Write a function that takes a sentence string as an argument and returns that string with every occurrence of a "number word" — 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' — converted to its corresponding digit character.


My questions:
- Can you clarify what "word" means? Is it separated by one space? More than one space? Other characters potentially?
  - Is a word a series of non-whitespace chars, or something more narrow?
- Will our string always have at least one word? Will the iput ever be empty?
- Are number words limited to those you listed in the problem?
  - Can we have number words like "ten", "eleven", etc? Or do they just correspond to digits 0 to 9?
- Does case matter?
- If our input doesn't have any number words, do we just return the same string as was passed in?
- Do we retain everything else as is about the other words of the string, includign punctuation, case, etc?
- If there is more than one space as a delimiter, do we retain that as well, or should the output string just have one space as a delimiter between all words?
- Will we always receive a string as input?
- Will we ever get more than one argument?
- What do we do if we get no arguments?
- If we receive an empty string, should we return an empty string?
- Are there any chars that don't count as part of a word?



P:
Input: String of words
Output: String of words
Rules:
- A "word" is a series of non-whitespace chars separated by one or more whitespace characters
- A "numeric" word is a word that is one of the words shown in the problem statement (words for 0 to 9 only)
- If we receive an empty string as input, return an empty string
- Analysis should be case insensitive -> "ONe" -> 1
- Retain everything else about the string, including other words, punctuation, whitespaces, as the same.
- Assume we will always receive a string as input. Don't worry about non-strings, 0 arguments, more than 1 argument, etc.

Data structures:
- Words -> array
- Delimiters -> array
- Object -> Map numeric words to their digits



Algorithm:


HELPER: convertToDigits(words)
- Create a constant object `NUMERIC_MAP`: {'zero': '0', ...}
- For each word in the `words` array:
  - Convert word to lowercase
  - If the word is a key within `NUMERIC_MAP`, then replace the word in the array with the value in `NUMERIC_MAP`
- Return transformed array

HELPER: reconstructString(words, delimiters)
- Create an empty array `combined`
- For an index from 0 to the length of words
  - Get the word at that index, push to `combined`
  - Get the delimiter from that index. If not undefined, push to `combined`
- Join `combined` together and return


- If input is empty string, return empty string
- Get words
  - Regex: /\S+/g
- Store delimiters
  - Regex: /\s+/g
- Convert the appropriate words to digits
  - Use convertToDigits
- Reconstruct the string with the new words and return
  - Use reconstructString
*/


function convertToDigits(words) {
  const NUMERIC_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
  }
  return words.map((word) => NUMERIC_MAP[word.toLowerCase()] ?? word);
}

function reconstructString(words, delimiters) {
  let combined = [];
  for (let idx = 0; idx < words.length; idx += 1) {
    combined.push(words[idx]);
    if (delimiters[idx] !== undefined) {
      combined.push(delimiters[idx]);
    }
  }
  return combined;
}

function wordToDigit(text) {
  if (text === '') return '';

  let words = text.match(/\S+/g);
  console.log(words);
}

console.log(wordToDigit('Please call me at five five five one two three four. Thanks.') === "Please call me at 5 5 5 1 2 3 4. Thanks.");
// console.log(wordToDigit('Please   call me at five five five one two three four. Thanks.') === "Please   call me at 5 5 5 1 2 3 4. Thanks.");
// console.log(wordToDigit('Please call me at Five five FIVE ONe twO three four. Thanks.') === "Please call me at 5 5 5 1 2 3 4. Thanks.");
// console.log(wordToDigit('') === "");
// console.log(wordToDigit('hello there!') === "hello there!");



/*
THIS PROBLEM IS INCOMPLETE.
I realized too late that the way I set up my algorithm actually doesn't work. For example, it won't replace 'four.' because
of that period. There's no elegant way for me to do this as I have it laid out.

I really wish I had gone through the examples in much more detail to see that punctuation issue.
*/

/*
The correct solution is below:
*/

function wordToDigit(text) {
  if (text === '') return '';

  const NUMERIC_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
  }

  for (let numericWord in NUMERIC_MAP) {
    const regex = new RegExp('\\b' + numericWord + '\\b', 'ig');
    text = text.replace(regex, NUMERIC_MAP[numericWord.toLowerCase()]);
  }

  return text;

}