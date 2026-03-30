/*
In this exercise, you will implement your own versions of the Array.prototype.shift and Array.prototype.unshift methods.
These methods manipulate the contents of an array starting from the first index.

The shift method removes the first element from an array and returns that element; if the array is empty,
shift returns undefined. The unshift method adds one or more elements to the start of an array and returns
the new length of the array. Both methods mutate the original array.
*/

function shift(arr) {
  if (arr.length === 0) {
    return undefined;
  }

  let firstElement = arr[0];

  for (let idx = 1; idx < arr.length; idx += 1) {
    arr[idx - 1] = arr[idx];
  }
  arr.length -= 1;

  return firstElement;
}

function unshift(arr, ...elements) {
  // I am going to make the assumption that the order in which the elements appear in the arguments
  // should be the order in which they'll be in the array
  // In other words, if elements = [1, 2, 3], their order at the start of arr should also be [1, 2, 3, other elements]
  // This matches the behavior of the actual unshift method
  for (let idx = elements.length - 1; idx >= 0; idx -= 1) {
    unshiftSingleElement(arr, elements[idx]);
  }

  return arr.length;

}

function unshiftSingleElement(arr, element) {
  for (let idx = arr.length; idx >= 0; idx -= 1) {
    arr[idx] = arr[idx - 1];
  }
  arr[0] = element;
}



/* Going to try to reimplement shift and unshift using splice */
function shift(arr) {
  if (arr.length === 0) {
    return undefined;
  }

  let firstElement = arr.splice(0, 1)[0];
  return firstElement;
}

function unshift(arr, ...elements) {
  for (let idx = elements.length - 1; idx >= 0; idx -= 1) {
    arr.splice(0, 0, elements[idx]);
  }
  return arr.length;
}


console.log(shift([1, 2, 3]));                // 1
console.log(shift([]));                       // undefined
console.log(shift([[1, 2, 3], 4, 5]));        // [1, 2, 3]

console.log(unshift([1, 2, 3], 5, 6));        // 5
console.log(unshift([1, 2, 3]));              // 3
console.log(unshift([4, 5], [1, 2, 3]));      // 3

const testArray = [1, 2, 3];
console.log(shift(testArray));                // 1
console.log(testArray);                       // [2, 3]
console.log(unshift(testArray, 5));           // 3
console.log(testArray);                       // [5, 2, 3]