/*
Write a function that returns true if its integer argument is palindromic, or false otherwise.
A palindromic number reads the same forwards and backwards.
*/

function isPalindromicNumber(number) {
  let numericStr = String(number);
  return isPalindrome(numericStr);
}

isPalindromicNumber(34543);        // true
isPalindromicNumber(123210);       // false
isPalindromicNumber(22);           // true
isPalindromicNumber(5);            // true


// From prior exercise:

function isPalindrome(string) {
  let reversed = string.split('').reverse().join('');
  return string === reversed;
}