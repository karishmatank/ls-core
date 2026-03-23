// Q1
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWord = 'Hello';
let myOtherWord = myWord;

console.log(myWord);
console.log(myOtherWord);

/*
This will print `'Hello'` twice. At the line `let myOtherWord = myWord;`, we essentially 'copy' the string `'Hello'` from
`myWord` to `myOtherWord`.
*/


// Q2
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWord = 'Hello';
let myOtherWord = myWord;
myWord = 'Goodbye';

console.log(myWord);
console.log(myOtherWord);

/*
This will print:
Goodbye
Hello

Again, we start by copying the value `'Hello'` from `myOtherWord` to `myWord`. We then reassign `myWord`, but that has
no effect on `myOtherWord`.
*/


// Q3
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWords = ['Hello', 'Goodbye'];
let myOtherWords = myWords;
myWords[0] = 'Hi';

console.log(myWords);
console.log(myOtherWords);

/*
In this case, we print ['Hi', 'Goodbye'] twice.

`myOtherWords` will point to the same object in memory as `myWords` given `myWords` references an array, which is
mutable. We then mutate that array. Since both variables are pointing to the same array, the change is reflected
when we log both to the console.
*/


// Q4
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWords = ['Hello', 'Goodbye'];
let myOtherWords = myWords;
myWords = ['Hi', 'Bye'];

console.log(myWords);
console.log(myOtherWords);

/*
This will print:
[ 'Hi', 'Bye' ]
[ 'Hello', 'Goodbye' ]

We initialize `myOtherWords` to reference the same array that `myWords` references. However, we then reassign
`myWords`, which is why we log separate arrays.
*/


// Q5
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWords = ['Hello', 'Goodbye'];
let myWord = myWords[0];
myWords[0] = 'Hi';

console.log(myWords);
console.log(myWord);

/*
This will print:
['Hi', 'Goodbye']
'Hello'

When we assign `myWords[0]` to `myWord`, as we are assigning a string to `myWord`, JavaScript essentially copies
the string 'Hello' to `myWord`. This is a different string at a different memory address.
We then mutate `myWords`, but this has no impact on `myWord`.
*/


// Q6
// What will the following code log to the console and why? Don't run it until you have tried to answer.

let myWords = ['Hello', 'Goodbye'];
let myWord = 'Hi';
myWords[0] = myWord;
myWord = 'Hello';

console.log(myWords);
console.log(myWord);

/*
This will print:
['Hi', 'Goodbye']
'Hello'

We mutate `myWords`, reassigning the element at index 0 to the value of `myWord`. Since this value is a string,
which is a primitive, we copy over the value `'Hi'` to the element at index 0, which is a different string at a
different memory address. We subsequently reassign `myWord` to another string.
*/