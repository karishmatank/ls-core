/*
Write a function that computes the difference between the square of the sum of the first n positive integers and
the sum of the squares of the first n positive integers.
*/

function sumSquareDifference(n) {
  let range = [];
  for (let i = 1; i <= n; i += 1) {
    range.push(i);
  }

  let squareOfSum = range.reduce((acc, num) => acc + num, 0) ** 2;
  let sumOfSquares = range.map(num => num ** 2).reduce((acc, num) => acc + num, 0);
  return squareOfSum - sumOfSquares;
}

console.log(sumSquareDifference(3));      // 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
console.log(sumSquareDifference(10));     // 2640
console.log(sumSquareDifference(1));      // 0
console.log(sumSquareDifference(100));    // 25164150
