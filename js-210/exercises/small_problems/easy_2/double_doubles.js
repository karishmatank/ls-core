/*
A double number is an even-length number whose left-side digits are exactly the same as its right-side digits.
For example, 44, 3333, 103103, and 7676 are all double numbers, whereas 444, 334433, and 107 are not.

Write a function that returns the number provided as an argument multiplied by two, unless the argument is a
double number, in which case, return the double number as-is.

Examples:
twice(37);          // 74
twice(44);          // 44
twice(334433);      // 668866
twice(444);         // 888
twice(107);         // 214
twice(103103);      // 103103
twice(3333);        // 3333
twice(7676);        // 7676
*/

function twice(number) {
  if (isDoubleNumber(number)) {
    return number;
  }
  return number * 2;
}

function isDoubleNumber(number) {
  let strNumber = String(number);
  if (strNumber.length % 2 !== 0) {
    return false;
  }

  let idxHalf = strNumber.length / 2;
  return strNumber.slice(0, idxHalf) === strNumber.slice(idxHalf);
}

console.log(twice(37));          // 74
console.log(twice(44));          // 44
console.log(twice(334433));      // 668866
console.log(twice(444));         // 888
console.log(twice(107));         // 214
console.log(twice(103103));      // 103103
console.log(twice(3333));        // 3333
console.log(twice(7676));        // 7676