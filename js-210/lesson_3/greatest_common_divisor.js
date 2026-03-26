/*
Create a function that computes the Greatest Common Divisor of two positive integers.

gcd(12, 4);   // 4
gcd(15, 10);  // 5
gcd(9, 2);    // 1

*/

/*
Simple algorithm can be:
- Start from the minimum of the two numbers
- Iterate downward
- If each argument is divisible evenly by the num we are iterating on, return that num
*/

function gcd(num1, num2) {
  let startNum = Math.min(num1, num2);
  for (let candidate = startNum; candidate >= 1; candidate -= 1) {
    if (num1 % candidate === 0 && num2 % candidate === 0) {
      return candidate;
    }
  }
}

console.log(gcd(12, 4));
console.log(gcd(15, 10));
console.log(gcd(9, 2));
console.log(gcd(2, 9));
console.log(gcd(12, gcd(4, 8)));
console.log(gcd(gcd(12, 4), 8));