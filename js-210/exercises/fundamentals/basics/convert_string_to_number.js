/*
For this exercise we're going to learn more about type conversion by implementing our own parseInt function that
converts a string of numeric characters (including an optional plus or minus sign) to a number.

The function takes a string of digits as an argument, and returns the appropriate number.
Do not use any of the built-in functions for converting a string to a number type.

For now, do not worry about leading + or - signs, nor should you worry about invalid characters;
assume all characters will be numeric.
*/



function parseInt(numericStr) {
  // Get each digit from the string
  let digitsStr = numericStr.split('');

  let number = 0;
  let factor = 10 ** (digitsStr.length - 1);
  for (let digit of digitsStr) {
    digit = convertDigit(digit);
    number += (digit * factor);
    factor /= 10;
  }

  return number;

}

function convertDigit(digit) {
  // Convert string digit to number
  return digit.charCodeAt(0) - '0'.charCodeAt(0);
}

console.log(parseInt('4321'));
console.log(parseInt('570'));