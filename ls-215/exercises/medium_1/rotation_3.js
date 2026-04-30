/*
Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotateRightmostDigits function from the previous exercise.
*/

function rotateDigits(digits) {
  let subArray = digits.slice(1);
  subArray.push(digits[0]);
  return subArray;
}

function rotateRightmostDigits(number, n) {
  n = n > String(number).length ? String(number).length : n;

  let digits = String(number).split('').map(Number);
  let toRotate = digits.slice(-n);
  let rotated = rotateDigits(toRotate);

  let newDigits = digits.slice(0, -n).concat(rotated);
  return Number(newDigits.join(''));
}

/*
My questions:
- Does fully rotated mean what I said it does below?
- (I'll assume the same assumptions of the prior 2 parts of this question hold to keep from re-asking the same things)


P:
Input: number
Output: Fully rotated number
Rules:
- Fully rotated means, for a number with `n` digits:
  - Rotate the last `n` digits of the number
  - Rotate the last `n - 1` digits of the resulting number
  - ...
  - Rotate the last 2 digits of the resulting number
  - No need to rotate the last 1 digit, that doesn't do anything


Data structure:
- (We do a lot of what we need already in rotateRightmostDigits)
- Convert input into string to be able to work with length



Algorithm:
- Convert input into string, get its length
- Set `result` to the value of the input
- For an `n` from the string length to 1 (exclusive):
  - Get the new rotated number
    - Use rotateRightmostDigits, pass in `result` and `n`
  - Reassign `result` to the newly rotated number
- Return `result`

*/

function maxRotation(number) {
  const strLen = String(number).length;
  let result = number;
  for (let n = strLen; n > 1; n -= 1) {
    result = rotateRightmostDigits(result, n);
  }
  return result;
}

console.log(maxRotation(735291));          // 321579
console.log(maxRotation(3));               // 3
console.log(maxRotation(35));              // 53
console.log(maxRotation(105));             // 15 -- the leading zero gets dropped
console.log(maxRotation(8703529146));      // 7321609845


/* EDIT: COULD HAVE BEEN MORE PRECISE HERE WITH LEADING ZEROS
For example, what should happen if we call maxRotation(1005)? Our current code returns 51, is
that what we want? That's what we need to ask questions on.
*/