/*
Write a function that rotates the last n digits of a number. For the rotation, rotate by one digit to the left, moving the first digit to the end.

My questions:
- Is my understanding of rotation below accurate?
- What happens if `n` is 0 or negative?
- Will the inputs always be numbers? What happens if we receive other data types?
- What happens if we receive an NaN, Infinity, -Infinity, or a non-integer number for either input?
- Could the first input be negative too?
- Could the first input have leading zeros? Is that even possible?
- What happens if the first input has fewer digits than the number of the second input? i.e. rotateRightmostDigits(735, 4). Do we just rotate as if we called rotateRightmostDigits(735, 3), or do something else?
- What happens if we receive < 2 or > 2 inputs?



P:
Input: 2 numbers, first to be rotated, second is the number digits to rotate
Output: Rotated number

Rules:
- Given two inputs, rotate the last `n` digits, where `n` is the second input
- Rotate definition
  - Take the last `n` of digits from the first input
  - Of those `n` digits, move the first digit to the end
  - Attach those newly rotated `n` digits to the end of the leftover from the first step
- If `n` is 1, nothing to rotate, just return the input
- Assume `n` will be a positive integer
- Assume both arguments will be *integers*. First argument will be non-negative integer, second argument will be positive integer. Don't need to handle NaN, Infinity, -Infinity
- If `n` is > the number of digits of the first input, re-cast `n` to the length of the first input
- Assume we call with exactly 2 inputs

Data structures:
Store digits of first input -> Array


Algorithm:

HELPER: rotateDigits(numbers) -> array of numbers
- Create a subarray from index 1 to the end
- Attach the first element of `numbers` to the end of the subarray
- Return the new subarray

Main:
- If `n` is > length of first input:
  - (Will need to cast first input to a string to get length)
  - Reassign `n` to be the length of the first input
- Convert first input into an array of digits -> `digits`
- Get the last `n` (second input) digits of `digits`
- Rotate those last `n` digits
  - Use rotateDigits
- Re-attach the rotated digits to the non-rotated digits from the input
  - Create a subarray of the digits that weren't rotated -> from index 0 to -n (exclusive)
- Convert back to one number and return

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


console.log(rotateRightmostDigits(735291, 1));      // 735291
console.log(rotateRightmostDigits(735291, 2));      // 735219
console.log(rotateRightmostDigits(735291, 3));      // 735912
console.log(rotateRightmostDigits(735291, 4));      // 732915
console.log(rotateRightmostDigits(735291, 5));      // 752913
console.log(rotateRightmostDigits(735291, 6));      // 352917

console.log(rotateRightmostDigits(735, 6));      // 357
