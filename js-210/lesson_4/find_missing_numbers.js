/*
Write a function that takes a sorted array of integers as an argument,
and returns an array that includes all the missing integers (in order) between the
first and last elements of the argument.

Examples:
missing([-3, -2, 1, 5]);                  // [-1, 0, 2, 3, 4]
missing([1, 2, 3, 4]);                    // []
missing([1, 5]);                          // [2, 3, 4]
missing([6]);                             // []
*/

/* Approach 1: Compare each element to the one before, and fill in the gaps */
function missing(sortedArr) {
  let missingNums = [];
  for (let idx = 1; idx < sortedArr.length; idx += 1) {
    let start = sortedArr[idx - 1] + 1;
    let end = sortedArr[idx];
    for (let missingNum = start; missingNum < end; missingNum += 1) {
      missingNums.push(missingNum);
    }
  }
  return missingNums;
}

/* Approach 2: Loop through all integers starting from the first element all the way to the last,
only add the ones that are not in the original array */
function missing(sortedArr) {
  let missingNums = [];

  let firstNum = sortedArr[0];
  let lastNum = sortedArr[sortedArr.length - 1];
  for (let num = firstNum + 1; num < lastNum; num += 1) {
    if (!sortedArr.includes(num)) {
      missingNums.push(num);
    }
  }
  return missingNums;
}

console.log(missing([-3, -2, 1, 5]));                  // [-1, 0, 2, 3, 4]
console.log(missing([1, 2, 3, 4]));                    // []
console.log(missing([1, 5]));                          // [2, 3, 4]
console.log(missing([6]));                             // []