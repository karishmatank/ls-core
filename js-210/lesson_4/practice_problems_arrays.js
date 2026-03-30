/*
Q1:
With arrays, you can access the first element's value with [0], but how do you access the last value?
Write a function named lastInArray that returns the value of the last element in the array provided by the
function's argument. You may use the length property and the [] operator, but do not use any other methods or properties.
*/

function lastInArray(arr) {
  return arr[arr.length - 1];
}

/*
Q2:
Create a function named rollCall that takes an array of first names as an argument and
logs all the names to the console, one name per line.
You should log the names in the same sequence that they appear in the array. Use a for loop to process the array.
*/

let names = ['A', 'B', 'C'];

function rollCall(firstNames) {
  for (let name of firstNames) {
    console.log(name);
  }
}

rollCall(names);

/*
Q3:
Create a function that returns the contents of the array it receives as an argument,
but with the values in reversed order. Your function should use a for loop that iterates over the elements
in the array from the end of the array to the beginning, and pushes each element's value to a new result array.
Be sure to start your loop with the element whose index is one less than the input array's length.
*/

let newArray = [1, 2, 3, 4, 5];

function reverseArray(arr) {
  let result = [];
  for (let idx = arr.length - 1; idx >= 0; idx -= 1) {
    result.push(arr[idx]);
  }
  return result;
}

console.log(reverseArray(newArray));

/*
Q4:
Write a function that returns a string of all the values in an array with no intervening content.
For example, your function should return '1a4' if the argument is [1, 'a', 4].
Use a for loop to process the array elements in sequence, and coerce each value in the array to a String
before concatenating it to the result string.
*/

arr = [1, 'a', 4];

function stringifyArray(arr) {
  let result = '';
  for (let element of arr) {
    result += String(element);
  }
  return result;
}

console.log(stringifyArray(arr));