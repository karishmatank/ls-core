function fibonacci(n) {
  if (n <= 2) {
    return 1;
  }

  let lastTwo = [1, 1];

  for (let count = 3; count <= n; count += 1) {
    let next = lastTwo[0] + lastTwo[1];
    lastTwo.push(next);
    lastTwo.shift();
  }

  return lastTwo[1];
}

console.log(fibonacci(20));       // 6765
console.log(fibonacci(50));       // 12586269025
console.log(fibonacci(75));       // 2111485077978050