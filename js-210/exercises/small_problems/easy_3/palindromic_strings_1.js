/*
Write a function that returns true if the string passed as an argument is a palindrome, or false otherwise.
A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.
*/

function isPalindrome(string) {
  let reversed = string.split('').reverse().join('');
  return string === reversed;
}

console.log(isPalindrome('madam'));               // true
console.log(isPalindrome('Madam'));               // false (case matters)
console.log(isPalindrome("madam i'm adam"));      // false (all characters matter)
console.log(isPalindrome('356653'));              // true
