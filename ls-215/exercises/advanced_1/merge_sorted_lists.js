/*
Write a function that takes two sorted arrays as arguments and returns a new array that contains all the elements
from both input arrays in sorted order.

You may not provide any solution that requires you to sort the result array.
You must build the result array one element at a time in the proper order.

Your solution should not mutate the input arrays.
*/

function merge(arr1, arr2) {
  let result = [];
  let left = [...arr1];
  let right = [...arr2];

  while (left.length !== 0 || right.length !== 0) {
    let nextFrom;
    if (left.length === 0) {
      nextFrom = right;
    } else if (right.length === 0) {
      nextFrom = left;
    } else if (right[0] < left[0]) {
      nextFrom = right;
    } else {
      nextFrom = left;
    }

    result.push(nextFrom.shift());
  }

  return result;
}

console.log(merge([1, 5, 9], [2, 6, 8]));      // [1, 2, 5, 6, 8, 9]
console.log(merge([1, 1, 3], [2, 2]));         // [1, 1, 2, 2, 3]
console.log(merge([], [1, 4, 5]));             // [1, 4, 5]
console.log(merge([1, 4, 5], []));             // [1, 4, 5]


/*
EDIT: I wasn't too happy with how repetitive my solution felt. I saw the official solution and decided to try
their way:
*/

function merge(arr1, arr2) {
  let result = [];
  let left = [...arr1];
  let right = [...arr2];

  while (left.length > 0 && right.length > 0) {
    let nextElement = right[0] < left[0] ? right.shift() : left.shift();
    result.push(nextElement);
  }

  result = result.concat(left.length > 0 ? left : right);
  return result;
}