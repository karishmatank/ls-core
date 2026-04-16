function sum(integer) {
  let digits = String(integer).split('').map(digit => Number(digit));
  return digits.reduce((acc, digit) => acc + digit, 0);
}

console.log(sum(23));           // 5
console.log(sum(496));          // 19
console.log(sum(123456789));    // 45