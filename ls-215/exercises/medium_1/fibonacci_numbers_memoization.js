const storage = {};

function fibonacci(num) {
  if (String(num) in storage) {
    return storage[num];
  }

  if (num <= 2) {
    return storage[num] = 1;
  }

  return storage[num] = fibonacci(num - 2) + fibonacci(num - 1);
}

console.log(fibonacci(20));       // 6765
console.log(fibonacci(50));       // 12586269025
console.log(fibonacci(75));       // 2111485077978050