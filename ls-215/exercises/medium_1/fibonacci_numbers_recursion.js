/*
Write a recursive function that computes the nth Fibonacci number, where nth is an argument passed to the function.
*/

function fibonacci(num) {
  if (num === 1) {
    return 1;
  } else if (num === 2) {
    return 1;
  }

  return fibonacci(num - 2) + fibonacci(num - 1);
}

console.log(fibonacci(1));       // 1
console.log(fibonacci(2));       // 1
console.log(fibonacci(3));       // 2
console.log(fibonacci(4));       // 3
console.log(fibonacci(5));       // 5
console.log(fibonacci(12));      // 144
console.log(fibonacci(20));      // 6765