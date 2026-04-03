/*
Write a function that takes two arrays as arguments and returns an array containing the union of the values from the
two. There should be no duplication of values in the returned array, even if there are duplicates in the original
arrays. You may assume that both arguments will always be arrays.
*/

function union(arr1, arr2) {
  let result = [];
  let allElements = arr1.concat(arr2);
  for (let num of allElements) {
    if (!result.includes(num)) {
      result.push(num);
    }
  }
  return result;
}

console.log(union([1, 3, 5], [3, 6, 9]));    // [1, 3, 5, 6, 9]