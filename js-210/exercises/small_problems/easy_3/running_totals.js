/*
Write a function that takes an array of numbers and returns an array with the same number of elements,
but with each element's value being the running total from the original array.
*/

function runningTotal(arr) {
  let result = [];
  let rollingSum = 0;
  for (let idx = 0; idx < arr.length; idx += 1) {
    rollingSum += arr[idx];
    result.push(rollingSum);
  }
  return result;
}

console.log(runningTotal([2, 5, 13]));             // [2, 7, 20]
console.log(runningTotal([14, 11, 7, 15, 20]));    // [14, 25, 32, 47, 67]
console.log(runningTotal([3]));                    // [3]
console.log(runningTotal([]));                     // []

/*
Can you rewrite the solution using the Array.prototype.map method?
What types of problems do you think are well-suited for the Array.prototype.map method?
*/

function runningTotal(arr) {
  let rollingSum = 0;
  return arr.map((num) => {
    rollingSum += num
    return rollingSum;
  });
}

/* I think map is actually best when we want to run each number through a function rather than
also create side effects as my code is doing above. The code above doesn't feel super clean.*/