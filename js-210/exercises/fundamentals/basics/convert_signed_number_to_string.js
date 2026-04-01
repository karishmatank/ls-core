/*
In the previous exercise, you reimplemented a function that converts non-negative numbers to strings.
In this exercise, you're going to extend that function by adding the ability to represent negative numbers.

You may not use any of the standard conversion functions available in JavaScript, such as String(),
Number.prototype.toString, or an expression such as '' + number.
You may, however, use the integerToString function from the previous exercise.
*/

function signedIntegerToString(num) {
  let sign;
  if (num < 0) {
    sign = '-';
  } else if (num > 0) {
    sign = '+';
  } else{
    sign = '';
  }

  let result = integerToString(Math.abs(num));
  result = sign + result;
  return result;

}

console.log(signedIntegerToString(4321));      // "+4321"
console.log(signedIntegerToString(-123));      // "-123"
console.log(signedIntegerToString(0));         // "0"


/* From last question */
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