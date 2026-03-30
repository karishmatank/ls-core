/*
Q1:
Write a function that returns the first element of an array passed in as an argument.
*/

function firstElementOf(arr) {
  return arr[0];
}

console.log(firstElementOf(['U', 'S', 'A']));  // returns "U"

/*
Q2:
Write a function that returns the last element of an array passed in as an argument.
*/

function lastElementOf(arr) {
  return arr[arr.length - 1];
}

console.log(lastElementOf(['U', 'S', 'A']));  // returns "A"

/*
Q3:
Write a function that accepts two arguments, an array and an integer index position, and
returns the element at the given index.
Can you predict what happens if the index is greater than the length of the array?
What about if it is a negative integer?
*/

function nthElementOf(arr, index) {
  return arr[index];
}

let digits = [4, 8, 15, 16, 23, 42];

console.log(nthElementOf(digits, 3));   // returns 16
console.log(nthElementOf(digits, 8));   // what does this return?
console.log(nthElementOf(digits, -1));  // what does this return?

/* If the index is greater than the length of the array, or negative, the function will return undefined */

/*
Q4:
Can we insert data into an array at a negative index? If so, why is this possible?
*/

/*
Javascript technically allows this because it will create a new property, where the key is the negative integer
and the value is the value supplied. However, this doesn't work as it does in Python. In Python,
if we supply a negative index, Python will count backwards from the end of the array.
*/

/*
Q5:
Write a function that accepts an array as the first argument and an integer value, count, as the second.
It should return a new array that contains the first count elements of the array.
*/

function firstNOf(arr, count) {
  return arr.slice(0, count);
}

// let digits = [4, 8, 15, 16, 23, 42];
console.log(firstNOf(digits, 3));    // returns [4, 8, 15]

/*
Q6:
Write a function like the previous one, except this time return the last count elements as a new array.
*/

function lastNOf(arr, count) {
  return arr.slice(arr.length - count);
}

// let digits = [4, 8, 15, 16, 23, 42];
console.log(lastNOf(digits, 3));    // returns [16, 23, 42]


/*
Q7:
Using the function from the previous problem, what happens if you pass a count greater than the
length of the array? How can you fix the function so it returns a new instance of the entire array
when count is greater than the array length?
*/

/*
What will happen is that we'll pass in a negative number as an argument to slice.
I believe if that happens, slice will just return the entire array.
EDIT: Not quite- it just returns the last # of elements from the array, as specified by the input.
So, if the input to slice is -1, it'll return the last element, if -2, the last two elements, etc.
*/
console.log(lastNOf(digits, 7)); // prints [42] -> arr.length = 6, 6 - 7 = -1, gets last element

function lastNOfV2(arr, count) {
  return arr.slice(Math.max(arr.length - count, 0));
}

console.log(lastNOfV2(digits, 7)); // prints the entire array now

/*
Q8:
Write a function that accepts two arrays as arguments and returns an array with the first element
from the first array and the last element from the second array.
*/

function endsOf(beginningArr, endingArr) {
  return [beginningArr[0], endingArr[endingArr.length - 1]];
}

console.log(endsOf([4, 8, 15], [16, 23, 42]));  // returns [4, 42]
