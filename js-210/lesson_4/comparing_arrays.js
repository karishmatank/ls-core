/*
Write a function named arraysEqual that takes two arrays as arguments.
The function should return true if the arrays contain the same values, or false if they do not.

Test the function with arrays that contain number, string, and boolean values.
Don't worry about handling arrays that contain other Arrays or Objects.
*/

function arraysEqual(arr1, arr2) {
  if (arr1.length !== arr2.length) return false;

  for (let idx = 0; idx < arr1.length; idx += 1) {
    if (arr1[idx] !== arr2[idx]) return false;
  }

  return true;
}

console.log(arraysEqual([1], [1]));                               // true
console.log(arraysEqual([1], [2]));                               // false
console.log(arraysEqual([1, 2], [1, 2, 3]));                      // false
console.log(arraysEqual([1, 'hi', true], [1, 'hi', true]));       // true
console.log(arraysEqual([1, 'hi', true], [1, 'hi', false]));      // false
console.log(arraysEqual([1, 'hi', true], [1, 'hello', true]));    // false
console.log(arraysEqual([1, 'hi', true], [2, 'hi', true]));       // false