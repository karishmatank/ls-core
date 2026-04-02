/*
The getSelectedColumns function selects and extracts specific columns to a new array.
Currently, the function is not producing the expected result.
Go over the function and the sample runs shown below. What do you think the problem is?
*/

function getSelectedColumns(numbers, cols) {
  var result = [];

  for (var i = 0, length = numbers.length; i < length; i += 1) {
    for (var j = 0, length = cols.length; j < length; j += 1) {
      if (!result[j]) {
        result[j] = [];
      }

      result[j][i] = numbers[i][cols[j]];
    }
  }

  return result;
}

// given the following arrays of number arrays
const array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
const array2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]];

// `array1` in row/column format
// [[1, 2, 3],
//  [4, 5, 6],
//  [7, 8, 9]]

console.log(getSelectedColumns(array1, [0]));     // [[1]];            expected: [[1, 4, 7]]
console.log(getSelectedColumns(array1, [0, 2]));  // [[1, 4], [3, 6]]; expected: [[1, 4, 7], [3, 6, 9]]
console.log(getSelectedColumns(array2, [1, 2]));  // [[2, 2], [3, 3]]; expected: [[2, 2, 2], [3, 3, 3]]

/*
The issue lies with how we define `length`.
Since we use `var` to declare `length`, `length` is function scoped, not block scoped.
We assign `length` to the value of numbers.length to start, but then reassign it
to cols.length soon after. These are reassignments because there are no block-scoped variables to each for loop
named `length` to shadow the `length` variable at a non-local scope.

Therefore, we don't actually iterate through each nested array within the `numbers` array.
*/