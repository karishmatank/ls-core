/*
Merge sort is a recursive sorting algorithm that works by breaking down an array's elements into nested sub-arrays,
then combining those nested sub-arrays back together in sorted order.
It is best explained with an example.

Given the array [9, 5, 7, 1, 8, 2, 0, 6], let's walk through the process of sorting it with merge sort.
We'll start off by breaking the array down into nested sub-arrays:

[9, 2, 7, 6, 8, 5, 0, 1] -->              // initial list
[[9, 2, 7, 6], [8, 5, 0, 1]] -->          // divide into two lists
[[[9, 2], [7, 6]], [[8, 5], [0, 1]]] -->  // divide each sub-array in two
// repeat until each sub-array contains only 1 value
[[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]]

In the first step, we partition the array into an array of two sub-arrays,
so that each sub-array contains approximately half of the entries.
In the next step, we partition each sub-array in the same way.
This process repeats until each of the innermost sub-arrays contains exactly one element.

We then work our way back to a flat array by merging each pair of nested sub-arrays back together in the proper order:

[[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]] -->
[[[2, 9], [6, 7]], [[5, 8], [0, 1]]] -->
[[2, 6, 7, 9], [0, 1, 5, 8]] -->
[0, 1, 2, 5, 6, 7, 8, 9]

For example, on the 2nd line, we merge [2, 9] with [6, 7], which becomes `[2, 6, 7, 9].

Write a function that takes an array argument and returns a new array that contains the values
from the input array in sorted order.
The function should sort the array using the merge sort algorithm as described above.
You may assume that every element of the array will be of the same data type—either all numbers or all strings.

Feel free to use the merge function you wrote in the previous exercise.

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

function mergeSort(arr) {
  if (arr.length === 1) {
    return arr;
  }

  let halfway = Math.round(arr.length / 2);
  let left = arr.slice(0, halfway);
  let right = arr.slice(halfway);

  return merge(mergeSort(left), mergeSort(right));
}


console.log(mergeSort([9, 5, 7, 1]));               // [1, 5, 7, 9]
console.log(mergeSort([5, 3]));                     // [3, 5]
console.log(mergeSort([6, 2, 7, 1, 4]));            // [1, 2, 4, 6, 7]
console.log(mergeSort([9, 2, 7, 6, 8, 5, 0, 1]));   // [0, 1, 2, 5, 6, 7, 8, 9]

console.log(mergeSort(['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']));
// ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]

console.log(mergeSort([7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46]));
// [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54]
