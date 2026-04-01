/*
The previous exercise mimics the parseInt function to a lesser extent.
In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer.
The string may have a leading + or - sign;
if the first character is a +, your function should return a positive number;
if it is a -, your function should return a negative number.
If there is no sign, return a positive number.

You may assume the string will always contain a valid number.
*/

function stringToSignedInteger(numericStr) {
  let sign = numericStr[0] === '-' ? '-' : '+';

  let total = 0;
  for (let digit of numericStr) {
    if (digit >= '0' && digit <= '9') {
      digit = convertDigit(digit)
      total = (total * 10) + digit;
    }
  }

  if (sign === '-') {
    total *= -1;
  }

  return total;

}

function convertDigit(digit) {
  // Convert string digit to number
  return digit.charCodeAt(0) - '0'.charCodeAt(0);
}

console.log(stringToSignedInteger('4321'));      // 4321
console.log(stringToSignedInteger('-570'));      // -570
console.log(stringToSignedInteger('+100'));      // 100
