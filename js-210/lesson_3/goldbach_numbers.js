/*
Write a function named checkGoldbach that uses Goldbach's Conjecture to log every pair of primes
that sum to the number supplied as an argument.
The conjecture states that "you can express every even integer greater than 2 as the sum of two primes".
The function takes as its only parameter, an integer expectedSum, and logs all combinations of two prime numbers
whose sum is expectedSum. Log the prime pairs with the smaller number first.
If expectedSum is odd or less than 4, your function should log null.

Your checkGoldbach function may call the isPrime function you wrote for a previous practice problem.

checkGoldbach(3);
// logs: null

checkGoldbach(4);
// logs: 2 2

checkGoldbach(12);
// logs: 5 7

checkGoldbach(100);
// logs:
// 3 97
// 11 89
// 17 83
// 29 71
// 41 59
// 47 53

*/

/* From prime_check.js */
function isPrime(number) {
  if (number <= 1) {
    return false;
  }

  for (let factor = 2; factor < number; factor += 1) {
    if (number % factor === 0) {
      return false;
    }
  }

  return true;
}

function checkGoldbach(expectedSum) {
  if (expectedSum < 4 || expectedSum % 2 !== 0) {
    console.log(null);
    return;
  }

  for (let num1 = 2; num1 <= expectedSum / 2; num1 += 1) {
    if (isPrime(num1) && isPrime(expectedSum - num1)) {
      console.log(num1, expectedSum - num1);
    }
  }
}

checkGoldbach(3);
checkGoldbach(4);
checkGoldbach(12);
checkGoldbach(100);