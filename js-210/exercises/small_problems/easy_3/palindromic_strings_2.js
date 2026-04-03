/*
Write another function that returns true if the string passed as an argument is a palindrome, or false otherwise.
This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters.
If you wish, you may simplify things by calling the isPalindrome function you wrote in the previous exercise.
*/

function isRealPalindrome(string) {
  let cleanedString = '';
  for (let char of string) {
    char = char.toLowerCase();
    if (isAlphanumeric(char)) {
      cleanedString += char;
    }
  }

  return isPalindrome(cleanedString);

}

function isAlphanumeric(char) {
  return (char >= 'a' && char <= 'z') || (char >= '0' && char <= '9');
}

console.log(isRealPalindrome('madam'));               // true
console.log(isRealPalindrome('Madam'));               // true (case does not matter)
console.log(isRealPalindrome("Madam, I'm Adam"));     // true (only alphanumerics matter)
console.log(isRealPalindrome('356653'));              // true
console.log(isRealPalindrome('356a653'));             // true
console.log(isRealPalindrome('123ab321'));            // false

// From the last exercise
function isPalindrome(string) {
  let reversed = string.split('').reverse().join('');
  return string === reversed;
}