// Prompt for each question:
// What will the following code log to the console and why? Don't run it until you have tried to answer.


// Q1
function changeMyWord(word) {
  console.log(word);
  word = word.toUpperCase();
}

let myWord = 'Hello';
changeMyWord(myWord);
console.log(myWord);

/*
This will print:
Hello
Hello

We pass in `myWord` as an argument to `changeMyWord`, where the value `'Hello'` is referenced by the parameter `word`.
We print the value of `word`, which matches the value passed in of `'Hello'`.
While we reassign `word` to be the upper-case version of `'Hello'`, `word` is only a local variable, and
we do not return that value from the function.
Therefore, `myWord` is unchanged, as we didn't reassign the global variable `myWord`.
*/


// Q2
function changeMyWord(word) {
  console.log(word);
  word = word.toUpperCase();
  return word;
}

let myWord = 'Hello';
myWord = changeMyWord(myWord);
console.log(myWord);

/*
This will print:
Hello
HELLO

We pass in the value of `myWord`, which is `'Hello'` to the function `changeMyWord`. As we're working with an immutable
type, this behaves as if it were "pass-by-value", meaning that the parameter `word` references a value `'Hello'` that is
separate from the value of `myWord`.
We then log the value of `word` to the console, which is `'Hello'`.
We subsequently reassign `word` to the result of calling `toUpperCase` on `word`, which returns a new string object
with value `'HELLO'`. Lastly, we return `word` from the function and reassign the global variable `myWord` to
`'HELLO'`. This means we print `'HELLO'` to the console last.
*/


// Q3

function changeMyWord(word) {
  console.log(word);
  word = word.toUpperCase();
  return word;
}

let myWord = 'Hello';
let myOtherWord = changeMyWord(myWord);
console.log(myWord);
console.log(myOtherWord);

/*
This will print:
Hello
Hello
HELLO

Similar story as with the last question, except this time, we don't reassign `myWord` to the return value of
`changeMyWord(myWord)`, we simply declare and initialize a new variable `myOtherWord`.
*/


// Q4

function changeMyWords(words) {
  console.log(words);
  words[0] = 'Hi';
}

let myWords = ['Hello', 'Goodbye'];
changeMyWords(myWords);
console.log(myWords);

/*
This will print:
['Hello', 'Goodbye']
['Hi', 'Goodbye']

With mutable objects, Javascript behaves more like "pass by reference", where the parameter `words` references
the same array as global variable `myWords`. Within `changeMyWords`, we first print the value of the array
passed in to the console. We then mutate that array.
Since we mutated the array, the change is present when we log `myWords` to the console on the last line.
*/


// Q5

function changeMyWords(words) {
  console.log(words);
  words = ['Hi', 'Goodbye'];
}

let myWords = ['Hello', 'Goodbye'];
changeMyWords(myWords);
console.log(myWords);

/*
This will print:
['Hello', 'Goodbye']
['Hello', 'Goodbye']

The difference here vs Q4 is that we are now reassigning the local variable `words` rather than mutating the array
it points to. Thus, myWords still references the array ['Hello', 'Goodbye'], which is why we print that to the
console as per the last line.
*/