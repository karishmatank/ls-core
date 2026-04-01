/*
In the previous two exercises, you developed functions that convert simple numeric strings to signed integers.
In this exercise and the next, you're going to reverse those functions.

You will learn more about converting strings to numbers by writing a function that takes a positive integer or zero,
and converts it to a string representation.

You may not use any of the standard conversion functions available in JavaScript, such as String(),
Number.prototype.toString, or an expression such as '' + number.
Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.
*/

function integerToString(num) {
  let result = '';

  do {
    let onesDigit = num % 10;
    let onesDigitStr = convertDigit(onesDigit);
    result = onesDigitStr + result;

    num -= onesDigit;
    num /= 10;
  } while (num > 0);

  return result;
}

function convertDigit(digit) {
  // Convert numeric digit to string
  return String.fromCharCode('0'.charCodeAt(0) + digit);
}

console.log(integerToString(4321));      // "4321"
console.log(integerToString(0));         // "0"
console.log(integerToString(5000));      // "5000"