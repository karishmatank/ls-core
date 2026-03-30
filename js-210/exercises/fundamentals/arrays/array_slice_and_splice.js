/*
In this exercise, you will implement your own versions of the Array.prototype.slice and Array.prototype.splice
methods according to the following specifications.

The slice function takes three arguments: an array, and two integers representing a begin and an end index.
The function returns a new array containing the extracted elements starting from begin up to but not including end.
slice does not mutate the original array.

The splice function changes the contents of an array by deleting existing elements and/or adding new elements.
The function takes the following arguments: an array, a start index, a deleteCount, and zero or more elements to be added.
The function removes deleteCount number of elements from the array, beginning at the start index.
If any optional element arguments are provided, splice inserts them into the array beginning at the start index.
The function returns a new array containing the deleted elements, or an empty array ([]) if no elements are deleted.
splice mutates the original array.

Additional specifications:

slice:

- The values of begin and end will always be integers greater than or equal to 0.
- If the value of begin or end is greater than the length of the array, set it to equal the length.

splice:

- The values of start and deleteCount will always be integers greater than or equal to 0.
- If the value of start is greater than the length of the array, set it to equal the length.
- If the value of deleteCount is greater than the number of elements from start up to the end of the array,
set deleteCount to the difference between the array's length and start.
- Takes optional arguments for elements to add to the array; denoted by the rest parameter ...args.
If no elements to add are provided, splice only removes elements from the array.

*/

function slice(array, begin, end) {
  begin = Math.min(begin, array.length);
  end = Math.min(end, array.length);

  if (begin > end) {
    return [];
  }

  let result = [];
  for (let idx = begin; idx < end; idx += 1) {
    result.push(array[idx]);
  }

  return result;
}

console.log(slice([1, 2, 3], 1, 2));               // [2]
console.log(slice([1, 2, 3], 2, 0));               // []
console.log(slice([1, 2, 3], 5, 1));               // []
console.log(slice([1, 2, 3], 0, 5));               // [1, 2, 3]

const arr1 = [1, 2, 3];
console.log(slice(arr1, 1, 3));                     // [2, 3]
console.log(arr1);                                  // [1, 2, 3]

function splice(array, start, deleteCount, ...args) {
  start = Math.min(start, array.length);
  deleteCount = Math.min(deleteCount, array.length - start);

  // Remove elements
  let elementsDeleted = array.slice(start, start + deleteCount);

  for (let idx = start; idx < array.length; idx += 1) {
    array[idx] = array[idx + deleteCount];
  }
  array.length -= deleteCount;

  // Add elements, if passed in
  let numToAdd = args.length;
  if (numToAdd > 0) {
    // Shift over existing elements to the right first
    for (let idx = array.length + numToAdd - 1; idx >= start; idx -= 1) {
      array[idx] = array[idx - numToAdd];
    }

    // Add in new elements
    for (let idx = start; idx < start + numToAdd; idx += 1) {
      array[idx] = args[idx - start];
    }
  }

  return elementsDeleted;

}

console.log(splice([1, 2, 3], 1, 2));              // [2, 3]
console.log(splice([1, 2, 3], 1, 3));              // [2, 3]
console.log(splice([1, 2, 3], 1, 0));              // []
console.log(splice([1, 2, 3], 0, 1));              // [1]
console.log(splice([1, 2, 3], 1, 0, 'a'));         // []

const arr2 = [1, 2, 3];
console.log(splice(arr2, 1, 1, 'two'));             // [2]
console.log(arr2);                                  // [1, "two", 3]

const arr3 = [1, 2, 3];
console.log(splice(arr3, 1, 2, 'two', 'three'));    // [2, 3]
console.log(arr3);                                  // [1, "two", "three"]

const arr4 = [1, 2, 3];
console.log(splice(arr4, 1, 0));                    // []
console.log(splice(arr4, 1, 0, 'a'));               // []
console.log(arr4);                                  // [1, "a", 2, 3]

const arr5 = [1, 2, 3];
console.log(splice(arr5, 0, 0, 'a'));               // []
console.log(arr5);                                  // ["a", 1, 2, 3]