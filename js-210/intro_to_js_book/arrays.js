/*
Q1:
In the following code, what are the final length values for array1, array2, array3, array4, and array5?
*/

let array1 = [1, 2, undefined, 4];

let array2 = [1];
array2.length = 5;

let array3 = [];
array3[-1] = [1];

let array4 = [1, 2, 3, 4, 5];
array4.length = 3;

let array5 = [];
array5[100] = 3;

/*
array1: 4
array2: 5 => We have an element with value 1 at index 0 and 4 empty items
array3: 0 => Properties don't count as part of the length
array4: 3 => Array gets truncated to length 3
array5: 101 => We have 100 empty items and a value of 3 at index 100
*/

/*
Q2
Log all of the even values from myArray to the console.
*/

let myArray = [1, 3, 6, 11, 4, 2,
               4, 9, 17, 16, 0];

myArray.forEach(function(element) {
  if (element % 2 === 0) {
    console.log(element);
  }
});

// If we cared about gathering all the even elements into a separate array
let evenValues = myArray.filter(element => element % 2 === 0);
console.log(evenValues);

/*
Q3:
Let's make the problem a little harder.
In this problem, we're again interested in even numbers,
but this time the numbers are in nested arrays in a single outer array.
*/

myArray = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
];

// Option 1
for (let outerIndex = 0; outerIndex < myArray.length; outerIndex += 1) {
  let subArray = myArray[outerIndex];
  for (let innerIndex = 0; innerIndex < subArray.length; innerIndex += 1) {
    if (subArray[innerIndex] % 2 === 0) {
      console.log(subArray[innerIndex]);
    }
  }
}

// Option 2
myArray.forEach(function(element) {
  element.forEach(function(subElement) {
    if (subElement % 2 === 0) {
      console.log(subElement);
    }
  });
});

/*
Q4:
Let's try another variation on the even-numbers theme.
We'll return to the simpler one-dimensional array.
In this problem, we want to use the map function to create a new array that
contains one element for each element in the original array.
If the element is an even value, then the corresponding element in the new array
should contain the string 'even'; otherwise, the element in the new array should contain 'odd'.
*/

myArray = [
  1, 3, 6, 11,
  4, 2, 4, 9,
  17, 16, 0,
];

let transformedArray = myArray.map(function(element) {
  if (element % 2 === 0) {
    return 'even';
  } else {
    return 'odd';
  }
});

console.log(transformedArray);

/*
Q5:
Write a findIntegers function that takes an array argument and
returns an array that contains only the integers from the input array.
Use the filter method in your function.
*/

function findIntegers(arr) {
  return arr.filter(element => Number.isInteger(element));
}

let things = [1, 'a', '1', 3, NaN, 3.1415, -4, null, false];
let integers = findIntegers(things);
console.log(integers); // => [1, 3, -4]

/*
Q6:
Use map and filter to first determine the lengths of all the elements in an array of string values,
then discard the even values (keep the odd values).
*/

function oddLengths(stringArray) {
  let stringLengths = stringArray.map(element => element.length);
  return stringLengths.filter(element => element % 2 !== 0);
}

let arr = ['a', 'abcd', 'abcde', 'abc', 'ab'];
console.log(oddLengths(arr)); // => [1, 5, 3]

/*
Q7
Use reduce to compute the sum of the squares of all of the numbers in an array:

Note that 83 is 3*3 + 5*5 + 7*7.
*/

function sumOfSquares(array) {
  return array.reduce((accumulator, current) => {
    return accumulator + current ** 2;
  }, 0);
}

let array = [3, 5, 7];
console.log(sumOfSquares(array)); // => 83

/*
Q8:
Write a function similar to the oddLengths function from Exercise 6, but don't use map or filter.
Instead, try to use the reduce method.
*/

function oddLengths(stringArray) {
  return stringArray.reduce((accumulator, current) => {
    if (current.length % 2 !== 0) {
      accumulator.push(current.length);
    }
    return accumulator;
  }, []);
}

arr = ['a', 'abcd', 'abcde', 'abc', 'ab'];
console.log(oddLengths(arr)); // => [1, 5, 3]

/*
Q9:
Without using a for, while, or do/while loop, write some code that checks
whether the number 3 appears inside these arrays:
*/

let numbers1 = [1, 3, 5, 7, 9, 11];
let numbers2 = [];
let numbers3 = [2, 4, 6, 8];

console.log(numbers1.includes(3));
console.log(numbers2.includes(3));
console.log(numbers3.includes(3));

/*
Q10:
Write some code to replace the value 6 in the following array with 606:
You don't have to search the array. Just write an assignment that replaces the 6.
*/

arr = [
  ["hello", "world"],
  ["example", "mem", null, 6, 88],
  [4, 8, 12]
];

arr[1][3] = 606;