// Q1
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWord = 'Hello';
myWord.concat(' there.');

console.log(myWord);

/*
This will print `'Hello'` to the console. When we call the `concat` method on `myWord`, we don't mutate the string value
of `myWord` because strings are immutable. `concat` returns a new string, which we aren't storing in any variable.
*/


// Q2
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWord = 'Hello';
myWord.repeat(3);
console.log(myWord);
myWord.replace('H', 'J');
console.log(myWord);
myWord.split(' ');
console.log(myWord);

/*
This will print:
Hello
Hello
Hello

None of these methods mutate myWord. Again, strings are immutable. In addition, we don't store the return values of any
of the method calls.
*/


// Q3
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWords = ['Hello'];
myWords.push('Goodbye');

console.log(myWords);

/*
This will print: `['Hello', 'Goodbye']`. `push` is a method that mutates the array it is called on.
*/


// Q4
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWords = ['Hello'];
myWords.concat(['Goodbye']);

console.log(myWords);

/*
This will print ['Hello']. `concat` does not mutate arrays, and we aren't storing the return value of `concat`, thus
the initial array is unaffected.
*/


// Q5
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWords = ['Hello'];
myWords[0].toUpperCase();

console.log(myWords);

/*
This will print ['Hello']. We are calling `toUpperCase` on the string at index 0 of myWords. We can't mutate strings,
and `toUpperCase` returns a new string object that we aren't storing anywhere.
*/


// Q6
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWords = ['Hello'];
myWords[0] = myWords[0].toUpperCase();

console.log(myWords);

/*
This will print ['HELLO']. We are mutating the list by reassigning the string at index 0 to the return value after
invoking `toUpperCase`.
*/