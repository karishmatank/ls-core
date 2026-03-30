/*
Write a function named push that accepts two arguments: an Array and any other value.
The function should append the second argument to the end of the Array, and return the new length of the Array.
*/

function push(arr, newElement) {
  let newElementIndex = arr.length;
  arr[newElementIndex] = newElement;
  return arr.length;
}

let count = [0, 1, 2];
console.log(push(count, 3));         // 4
console.log(count);                  // [ 0, 1, 2, 3 ]

/*
Write a function named pop that accepts one argument: an Array.
The function should remove the last element from the array and return it.
*/

function pop(arr) {
  let lastElement = arr[arr.length - 1];
  arr.length -= 1;
  return lastElement;
}

count = [1, 2, 3];
console.log(pop(count));             // 3
console.log(count);                  // [ 1, 2 ]

/*
Write a function named unshift that accepts two arguments: an Array and a value.
The function should insert the value at the beginning of the Array, and return the new length of the array.
You will need a for loop for this problem.
*/

function unshift(arr, val) {
  for (let idx = arr.length; idx > 0; idx -= 1) {
    arr[idx] = arr[idx - 1];
  }
  arr[0] = val;
  return arr.length;
}

count = [1, 2, 3];
console.log(unshift(count, 0));      // 4
console.log(count);                  // [ 0, 1, 2, 3 ]

/*
Write a function named shift that accepts one argument: an Array.
The function should remove the first value from the beginning of the Array and return it.
*/

function shift(arr) {
  let firstElement = arr[0];

  for (let idx = 1; idx < arr.length; idx += 1) {
    arr[idx - 1] = arr[idx];
  }
  arr.length -= 1;
  return firstElement;
}

count = [1, 2, 3];
console.log(shift(count));           // 1
console.log(count);                  // [ 2, 3 ]

/*
Write a function indexOf that accepts two arguments: an array and a value.
The function returns the first index at which the value can be found, or -1 if the value is not present.
*/

function indexOf(arr, val) {
  for (let idx = 0; idx < arr.length; idx += 1) {
    if (arr[idx] === val) {
      return idx;
    }
  }
  return -1;
}

console.log(indexOf([1, 2, 3, 3], 3));         // 2
console.log(indexOf([1, 2, 3], 4));            // -1


/*
Write a function lastIndexOf that accepts two arguments: an array and a value.
The function returns the last index at which the value can be found in the array, or -1 if the value is not present.
*/

function lastIndexOf(arr, val) {
  for (let idx = arr.length - 1; idx >= 0; idx -= 1) {
    if (arr[idx] === val) {
      return idx;
    }
  }
  return -1;
}

console.log(lastIndexOf([1, 2, 3, 3], 3));     // 3
console.log(lastIndexOf([1, 2, 3], 4));        // -1


/*
Write a function named slice that accepts three arguments: an Array, a start index, and an end index.
The function should return a new Array that contains values from the original Array starting with the value
at the starting index, and including all values up to but not including the end index. Do not modify the original Array.

You may use functions that were answers to previous practice problems to complete this problem, but do not use any
built-in Array methods.
*/

function makeCopy(arr) {
  let newArray = [];
  for (let idx = 0; idx < arr.length; idx += 1) {
    newArray[idx] = arr[idx];
  }
  return newArray;
}

/* Attempt 1. Not super direct but works */
function slice(arr, startIdx, endIdx) {
  let newArray = makeCopy(arr);

  // For index 0 up to startIdx, use shift to remove elements
  for (let idx = 0; idx < startIdx; idx += 1) {
    shift(newArray);
    endIdx -= 1;
  }

  // For endIdx to the end, use pop to remove elements
  let newLength = newArray.length;
  for (let idx = endIdx; idx < newLength; idx += 1) {
    pop(newArray);
  }

  return newArray;
}

/* Attempt 2 */
function slice(arr, startIdx, endIdx) {
  let newArray = [];

  for (let idx = startIdx; idx < endIdx; idx += 1) {
    push(newArray, arr[idx]);
  }

  return newArray;
}

console.log(slice([1, 2, 3, 4, 5], 0, 2));                      // [ 1, 2 ]
console.log(slice(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 1, 3));  // [ 'b', 'c' ]


/*
Write a function named splice that accepts three arguments: an Array, a start index, and the number of values to remove.
The function should remove values from the original Array, starting with the start index and removing the specified
number of values. The function should return the removed values in a new Array.

You may use functions that were answers to previous practice problems to complete this problem, but do not use any
built-in Array methods.
*/

/* Initial attempt: Longer way to do it */
function splice(arr, startIdx, removeCount) {
  let endIdx = startIdx + removeCount;
  let removedArray = slice(arr, startIdx, endIdx);

  // Shift elements left
  // ex: for [1, 2, 3, 4, 5, 6, 7, 8] and startIdx = 2, removeCount = 5,
  // we need to get to [1, 2, 8, undefined, undefined, undefined, undefined, undefined]
  // since we need to remove [3, 4, 5, 6, 7]
  for (let idx = startIdx; idx < endIdx; idx += 1) {
    arr[idx] = arr[idx + removeCount];
  }

  // Remove the excess undefined elements
  let firstUndefined = indexOf(arr, undefined);
  let numUndefined = arr.length - firstUndefined;
  while (numUndefined > 0) {
    pop(arr);
    numUndefined -= 1;
  }

  // Could have simplified the above section to just:
  // arr.length -= removedArray.length;

  return removedArray;
}

count = [1, 2, 3, 4, 5, 6, 7, 8];
console.log(splice(count, 2, 5));                   // [ 3, 4, 5, 6, 7 ]
console.log(count);                                 // [ 1, 2, 8 ]


/*
Write a function named concat that accepts two Array arguments.
The function should return a new Array that contains the values from each of the original Arrays.

You may use functions that were answers to previous practice problems to complete this problem,
but do not use any built-in Array methods.

concat([1, 2, 3], [4, 5, 6]);       // [ 1, 2, 3, 4, 5, 6 ]
*/

function concat(arr1, arr2) {
  let result = [];

  for (let element of arr1) {
    push(result, element);
  }

  for (let element of arr2) {
    push(result, element);
  }

  return result;
}

console.log(concat([1, 2, 3], [4, 5, 6]));


/*
Write a function named join that accepts two arguments: an Array and a String.
The function should coerce each value in the Array to a String, and then join those values together
using the second argument as a separator. You may assume that a separator will always be passed.
*/

function join(arr, delimiter) {
  let result = '';

  for (let idx = 0; idx < arr.length; idx += 1) {
    let element = String(arr[idx]);
    result += element;

    if (idx !== arr.length - 1) {
      result += delimiter;
    }
  }

  return result;
}

console.log(join(['bri', 'tru', 'wha'], 'ck '));       // 'brick truck wha'
console.log(join([1, 2, 3], ' and '));                 // '1 and 2 and 3'