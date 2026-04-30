/*
THIS PROBLEM WAS CONSIDERED EASY.



Write a program that cleans up user-entered phone numbers so that they can be sent as SMS messages.
Other than digits, the number may also contain special character such as spaces, dash, dot, and
parentheses that should be ignored.

The rules are as follows:

If the phone number is less than 10 digits, assume that it is a bad number.
If the phone number is 10 digits, assume that it is good.
If the phone number is 11 digits and the first number is 1, trim the 1 and use the last 10 digits.
If the phone number is 11 digits and the first number is not 1, then it is a bad number.
If the phone number is more than 11 digits, assume that it is a bad number.
For bad numbers, just a return a string of 10 0s.
*/

/*
Given a phone number, return a cleaned up number.

Input: String of digits and other select characters
Output: String of digits (10 digits)

Rules:
- Assume the input is a string.
- Treat any non-digit character as ignorable
- An empty string counts as a bad number.
- A valid phone number has:
  - 10 or 11 digits, **excluding any present non-digit characters**
  - If 11 digits, only valid if first digit is 1
    - In this case, we should trim the first digit and only use the remaining 10 digits
    - First digit references the character at the 0th element of the string after it is cleaned for non-digit chars
- Bad numbers mean:
  - < 10 or > 11 digits
  - 11 digits if the first digit is not a 1
- Assume that we always get one argument and that argument will always be a string.
  - Don't worry about not receiving an input or receiving more than one input
  - Don't worry about receiving inputs that are not strings
- Digit means '0' to '9'




Questions (ultimately answered by LSBot):
- Will the input be a string, a number, or another data type?
- Should the output be a string, a number, or another data type?
- Might the number also contain other types of characters other than the ones we're told to ignore?
- Does an empty string count as a bad number, or should our program behave in another way?
- Does the digit count (10 or 11) exclude all of the non-digit characters that may be present?
- Will we always receive an input?
- What happens if we don't receive an input at all?
- What happens if we receive more than one input?
- What happens if we receive an input that doesn't match the valid data types?
- Confirm that digits consist of 0 to 9.
- Should the output just have digits, or should we include other characters?


Data structures:
Input: string
Output: string of only 10 digits

May want to use array, but can likely get away with just working with strings


Algorithm:

High level:
- Clean up string, removing chars that are not digits
- If length of string is not 10 or 11, return '0000000000'
- If length of string is 11 but first char is not 1, return '0000000000'
- Else, return the cleaned up string

Main algorithm:
- Clean up string, removing chars that are not digits
  - Use regex pattern to detect chars that are not digits
- If length of string is not 10 or 11, return '0000000000'
- If length of string is 11:
  - If the first char is not '1', return '0000000000'
  - Else, return the cleaned up string without the first char

- Else, return the cleaned up string

*/


function cleanedNumber(number) {
  number = number.replace(/[^0-9]/g, '');
  if (number.length < 10 || number.length > 11) {
    return '0000000000';
  }

  if (number.length === 11) {
    if (number[0] !== '1') {
      return '0000000000';
    }
    else {
      return number.slice(1);
    }
  }

  return number;
}


// Test cases
console.log(cleanedNumber('1234567890') == '1234567890');
console.log(cleanedNumber('123-456-7890') == '1234567890');
console.log(cleanedNumber('(123) 456- 7890') == '1234567890');
console.log(cleanedNumber('abcdefg123456hijklmn7890') == '1234567890');

console.log(cleanedNumber('11234567890') == '1234567890');
console.log(cleanedNumber('1123-456-7890') == '1234567890');
console.log(cleanedNumber('(1123) 456- 7890') == '1234567890');

console.log(cleanedNumber('21234567890') == '0000000000');
console.log(cleanedNumber('') == '0000000000');
console.log(cleanedNumber('al;ksdjfa;kldjfkaljfew;io') == '0000000000');
console.log(cleanedNumber('....(())') == '0000000000');
console.log(cleanedNumber('123445') == '0000000000');
console.log(cleanedNumber('12344585728095729058273405') == '0000000000');