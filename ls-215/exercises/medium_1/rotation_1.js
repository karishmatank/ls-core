/*
Write a function that rotates an array by moving the first element to the end of the array. Do not modify the original array.

If the input is not an array, return undefined.
If the input is an empty array, return an empty array.
Review the test cases below, then implement the solution accordingly.


My questions:
- How do we treat more than one input?
- Might the array be sparse? If so, how do we handle?
- Might the array have custom properties? If so, how do we handle?
- If the array has null or undefined, do we handle the same way?
- Is it okay to assume the input may have elements of any data type / any combination of data types?


P:
Input: Array of any type element
Output: Array

Rules:
- We should move the first element of the given array to the end of the array
- Do NOT mutate the original array
- If the input is not an array or we don't receive an input, return undefined
- If the input is empty, return []
- If the input has only one element, return the input -> nothing to rotate
- ONly care about the first argument
- Don't worry about sparse arrays or custom properties

Data structure:
Input: Array of any type element
Output: Array

Store all elements except first in their own Array


Algorithm:
- If the input doesn't exist (undefined) or not an array, return undefined
- If the input is an empty array, return an empty array
- Get a subarray (separate array) of all elements from index 1 to the end
- Append the first element of the input to the end
- Return the new array

*/

function rotateArray(arr) {
  if (arr === undefined || !Array.isArray(arr)) return undefined;
  if (arr.length === 0) return [];

  let subArray = arr.slice(1);
  subArray.push(arr[0]);

  return subArray;
}


console.log(rotateArray([7, 3, 5, 2, 9, 1]));       // [3, 5, 2, 9, 1, 7]
console.log(rotateArray(['a', 'b', 'c']));          // ["b", "c", "a"]
console.log(rotateArray(['a']));                    // ["a"]
console.log(rotateArray([1, 'a', 3, 'c']));         // ["a", 3, "c", 1]
console.log(rotateArray([{ a: 2 }, [1, 2], 3]));    // [[1, 2], 3, { a: 2 }]
console.log(rotateArray([]));                       // []

// return `undefined` if the argument is not an array
console.log(rotateArray());                         // undefined
console.log(rotateArray(1));                        // undefined


// the input array is not mutated
const array = [1, 2, 3, 4];
console.log(rotateArray(array));                    // [2, 3, 4, 1]
console.log(array);                                 // [1, 2, 3, 4]