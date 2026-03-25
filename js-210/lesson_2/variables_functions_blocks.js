// Prompt for each: What will the following code log to the console and why? Don't run it until you have tried to answer.

// Q1
let color = 'yellow';
let colors = ['red', 'green', 'blue'];

function updateColors(colors) {
  colors.push(color);
}

updateColors(colors);
console.log(colors);

/*
This will print: ['red', 'green', 'blue', 'yellow']
We pass in an array when we invoke `updateColors`, which means that the parameter `colors` and the global variable
`colors` reference the same array. We then mutate that array by appending 'yellow', which is the value of `color`
accessible within the function `updateColors`, coming from the global variable `color`.
As a result, we log the mutated array.
*/


// Q2

let color = 'yellow';
let colors = ['red', 'green', 'blue'];

function updateColors(colors, color) {
  colors.push(color);
}

updateColors(colors);
console.log(colors);

/*
This will print:
['red', 'green', 'blue', undefined]

Here, we are passing in two arguments, represented by parameters `colors` and `color`. However, when we invoke
`updateColors`, we only explicitly pass in the array that global variable `colors` points to. This means that
parameter `colors` references the array we passed in but parameter `color`, which shadows global variable `color`,
is assigned `undefined`. We then mutate the array with `updateColors`.
*/


// Q3

let color1 = 'purple';
let color2 = 'pink';
let colors = ['red', 'green', 'blue'];

function updateColors(colors, color) {
  colors.push(color);
}

updateColors(colors, color1);
updateColors(colors, color2);
console.log(colors);

/*
This will print ['red', 'green', 'blue', 'purple', 'pink'].
When we invoke `updateColors`, we pass in a reference to the array that global variable `colors` references first,
followed by passing in the value that `color1` or `color2` reference, respectively. Since `color1` and `color2`
reference strings, this feels more like "pass by value".
For both invocations, we mutate the array passed in, which is why we see an array with 5 elements logged.
*/


// Q4
let color1 = 'purple';
let color2 = 'pink';
let colors = ['red', 'green', 'blue'];

function updateColors(colors, color) {
  colors.push(color);
  return colors;
}

let newColors = updateColors(colors, color1);
updateColors(newColors, color2);
console.log(colors);

/*
This will print:
['red', 'green', 'blue', 'purple', 'pink']

We start by declaring and initializing variables `color1`, `color2`, `color3`, and `updateColors`. I'm glossing over
the creation phase vs execution phase here as it's not material to the outcome.
We then invoke `updateColors`, passing in a reference to the `colors` array, as arrays are mutable and thus Javascript
acts more like "pass by reference". We also pass in the `color1` value, which is a string, thus behaving more like
"pass by value". Thus, the parameter `colors` points to the same array as does global variable `colors`, whereas
the parameter `color` is assigned the value `'purple'`.
Within `updateColors`, we mutate the array and return the reference to the array. This reference is assigned to
the global variable `newColors`.
We invoke `updateColors` once again, passing in the reference to the array that now `newColors` and `colors` point to.
Once again, parameter `colors` will point to this same array as well. We mutate the array once more.
When we log colors, we'll log the mutated array, which includes 'purple' and 'pink'
*/


// Q5
let color = 'purple';
let colors = ['red', 'green', 'blue'];

function addColor(colors, color) {
  colors.push(color);
  return colors;
}

function removeColor(colors) {
  color = colors.pop();
  return colors;
}

let newColors = removeColor(colors);
addColor(colors, color);
console.log(newColors);

/*
This will print:
['red', 'green', 'blue']

We invoke `removeColor`, passing in the reference to an array given arrays are mutable. From there, we mutate
the array by invoking the `pop` method. That method removes the last element, `'blue'` and reassigns the
global variable `color` to `'blue'`, since `pop` returns the element that it removes. We return the reference to
the local variable `colors` and assign it to `newColors`, which is the same array global variable `colors` references.
We then invoke `addColor`, which mutates the array passed in to add on the value of `color`. This essentially gets us back
to `['red', 'green', 'blue']` and is the value we get when we log on the last line.
*/


// Q6
function capitalize() {
  return word[0].toUpperCase() + word.slice(1);
}

function exclaim() {
  return word += '!!!';
}

let word = 'hello';
let capitalizedWord = capitalize(word);
let exclaimedWord = exclaim(capitalizedWord);

console.log(word);
console.log(capitalizedWord);
console.log(exclaimedWord);

/*
I think this will print:
hello!!!
Hello
hello!!!

We first declare and initialize a variable `word` to the string `'hello'`. While we pass `word` as an argument to
`capitalize`, we see `capitalize` doesn't actually have any parameters as per its definition, so the argument passed in
is essentially ignored. `word` referenced inside refers to the global variable `word`.
Within `capitalize`, we first take the first letter of `word`, which is `'h'`, call the `toUpperCase` method, which returns
`'H'`, and concatenate that with the substring formed from `word` that starts at index 1, which is `'ello'`. Thus,
we return `'Hello'` and assign that to `capitalizedWord`.
We then invoke `exclaim`, which similarly does not take any arguments, thus the argument we pass in is ignored. `exclaim`
references global variable `word` and reassigns global variable word to a string that appends on `'!!!'` to the end of
`word`'s value. The result of that expression is the newly formed string itself, which is returned and assigned to
`exclaimedWord`.
Thus, when we reference `word`, `capitalizeWord`, and `exclaimedWord`, we reference the strings
`'hello!!!'`, `'Hello'`, and `'hello!!!'`.
*/

// Q7
function capitalize(word) {
  return word[0].toUpperCase() + word.slice(1);
}

function exclaim(word) {
  return word += '!!!';
}

let word = 'hello';
let capitalizedWord = capitalize(word);
let exclaimedWord = exclaim(capitalizedWord);

console.log(word);
console.log(capitalizedWord);
console.log(exclaimedWord);

/*
This will print:
hello
Hello
Hello!!!

The difference this time is we have parameters defined in the function definitions, which means that we aren't
referencing global variable `word` inside any of the function bodies anymore- we are referencing the values passed in.
When we invoke `capitalize`, local variable `word` references `'hello'`. We passed in global variable `word` as an argument,
which behaves like "pass-by-value" in this instance since `word` has a string value. The behavior here matches
the behavior from the last problem, which means we return `'Hello'` from `capitalize` and assign it to `capitalizedWord`.
We then invoke `exclaim`, passing in the value of `capitalizedWord`. Thus, local variable `word` is assigned the value
`'Hello'`. Inside the body of `exclaim`, while we use the += operator, we are reassigning the local variable `word`
this time, which doesn't have any impact on the global variable `word`. We then return the result of that expression,
which is `'Hello!!!'`.
Thus, `word`, `capitalizedWord`, and `exclaimedWord` reference `'hello'`, `'Hello'`, `'Hello!!!'`.
*/