/*
Q1:
Write a function that creates and returns a new array from its array argument.
The new array should contain all values from the argument array whose positions have an odd index.
*/

function oddElementsOf(arr) {
  let result = [];
  for (let idx = 1; idx < arr.length; idx += 2) {
    result.push(arr[idx]);
  }
  return result;
}

let digits = [4, 8, 15, 16, 23, 42];

console.log(oddElementsOf(digits));    // returns [8, 16, 42]


/*
Q2:
Write a function that takes an array argument and returns a new array that contains all
the argument's elements in their original order followed by all the argument's elements in reverse order.
*/

function arrayAndReversed(arr) {
  let reversedArr = arr.slice();  // shallow copy
  reversedArr.reverse(); // mutates shallow copy only
  return arr.concat(reversedArr);
}

console.log(arrayAndReversed(digits)); // should log [4, 8, 15, 16, 23, 42, 42, 23, 16, 15, 8, 4]


/*
Q3:
Use the array sort method to create a function that takes an array of numbers and
returns a new array of the numbers sorted in descending order. Do not alter the original array.
*/

function sortDescending(arr) {
  let sortedArr = arr.slice();
  sortedArr.sort((a, b) => b - a); // sort numerically in descending order
  return sortedArr;
}

let array = [23, 4, 16, 42, 8, 15];
let result = sortDescending(array);
console.log(result);                 // logs    [42, 23, 16, 15, 8, 4]
console.log(array);                  // logs    [23, 4, 16, 42, 8, 15]

/*
Q4:
Write a function that takes an array of arrays as an argument, and returns a new array that
contains the sums of each of the sub-arrays.
*/

function matrixSums(arr) {
  let sums = [];
  arr.forEach(
    nestedArr => sums.push(nestedArr.reduce((accumulator, element) => accumulator + element, 0))
  );
  return sums;
}

console.log(matrixSums([[2, 8, 5], [12, 48, 0], [12]]));  // returns [15, 60, 12]


/*
Q5:
Write a function that takes an array, and returns a new array with duplicate elements removed.
*/

function uniqueElements(arr) {
  let dedupedArr = [];
  for (let element of arr) {
    if (!dedupedArr.includes(element)) {
      dedupedArr.push(element);
    }
  }
  return dedupedArr;
}

console.log(uniqueElements([1, 2, 4, 3, 4, 1, 5, 4]));  // returns [1, 2, 4, 3, 5]