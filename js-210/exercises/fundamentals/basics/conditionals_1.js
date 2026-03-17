/*
Go over the following program. What does it log to the console at lines 7, 11, 15, and 19?
Is it what you expected? Why or why not?
*/

const myBoolean = true;
const myString = 'hello';
const myArray = [];
const myOtherString = '';

if (myBoolean) {
  console.log('Hello');
}

if (!myString) {
  console.log('World');
}

if (!!myArray) {
  console.log('World');
}

if (myOtherString || myArray) {
  console.log('!');
}

/*
Line 12: 'Hello' => true is truthy
Line 16: Does not reach => 'hello' is truthy, ! negates to return false
Line 20: 'World' => [] is truthy. ![] is false, !false is true
Line 24: '!' => [] is truthy
*/