/*
THIS PROBLEM WAS CONSIDERED EASY.



The Luhn formula is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.

The formula verifies a number against its included check digit, which is usually appended to a partial number to generate the full number. This number must pass the following test:

Counting from the rightmost digit and moving left, double the value of every second digit
For any digit that thus become 10 or more, subtract 9 from the result
1111 becomes 2121
8763 becomes 7733 (from 2 x 6 = 12 -> 12 - 9 = 3 and 2 x 8 = 16 -> 16 - 9 = 7)
Add all these digits together
1111 becomes 2121 sums as 2 + 1 + 2 + 1 to give a checksum of 6
8763 becomes 7733, and 7 + 7 + 3 + 3 is 20
If the total (the checksum) ends in 0 (put another way, if the total modulo 10 is congruent to 0), then the number is valid according to the Luhn Formula; else it is not valid. Thus, 1111 is not valid (as shown above, it comes out to 6), while 8763 is valid (as shown above, it comes out to 20).

Write a program that, given a number in string format, check if it is valid per the Luhn formula. This should treat, for example, "2323 2005 7766 3554" as valid. You can ignore all non-numeric characters in the input string.
*/

/*
Given a string with some numeric digits, check if it is valid per the Luhn formula.

Input: string with digits and other characters
Output: Boolean (true / false)

Rules:
- Any non-numeric characters should be disregarded
- We don't need to worry about receiving an empty string
- Assume we will always be passed one string, not zero strings or not multiple strings
- We don't need to worry about receiving a data type other than a string
- There is no minimum / maximum number of digits we'll see. The string can be any length
- If there is one digit, the sum essentially is the value of that digit itself. There is nothing to double.
- Steps for validation:
  - Start from the right most digit. Move one digit to the left. Double that digit. From here on out, double every other digit. Every digit not doubled remains as is.
  - If the result of doubling the digit is >= 10, subtract 9 from the doubled number. This is the new result.
  - After we finish doubling, add all of the resulting digits
  - If the sum ends in a 0, then it is valid. Otherwise, it is not.


Data structures:
Input: String of numbers and other chars
Output: Boolean

Arrays for handling each digit

Algorithm:

High-level:
- Clean the string to remove non-digit chars
- Split the string into digits, convert each digit to number type
- Calculate the Luhn sum based on digits
  - Use calculateLuhnSum
- If result from calculateLuhnSum ends in 0, return true
- Otherwise, return false


HELPER: calculateLuhnSum
- Input: Array of digits
- Output: Number (representing sum)
Steps:
- Create a copy of the array => `digitsCopy`
- Reverse the order of `digitsCopy`
- Starting at index 1 and moving through every other element of array from left to right until the end of the array:
  - Double the digit at the index
  - If doubled result is >= 10, subtract 9
  - Reassign element in `digitsCopy` to the new result
- Calculate the sum of all of the elements of `digitsCopy`
- Return the sum

Main:
- Clean the string to remove non-digit chars
  - Use regex pattern with `replace` => /[^0-9]/g
- Split the string into digits, convert each digit to number type
- Calculate the Luhn sum based on digits
  - Use calculateLuhnSum to get the sum
- If result from calculateLuhnSum ends in 0, return true
- Otherwise, return false

*/

function calculateLuhnSum(digits) {
  let digitsCopy = [...digits];
  digitsCopy.reverse();

  for (let idx = 1; idx < digitsCopy.length; idx += 2) {
    let doubled = digitsCopy[idx] * 2;
    if (doubled >= 10) {
      doubled -= 9;
    }
    digitsCopy[idx] = doubled;
  }

  let sum = digitsCopy.reduce((acc, digit) => acc + digit, 0);
  return sum;
}

function isValid(str) {
  let cleaned = str.replace(/[^0-9]/g, '');
  let digits = cleaned.split('').map(digit => Number(digit));
  let sum = calculateLuhnSum(digits);
  return sum % 10 === 0;
}



console.log(isValid('1111') == false);
console.log(isValid('8763') == true);
console.log(isValid("2323 2005 7766 3554") == true);
// /*
// 4343400557366514 =>  60 % 10 === 0, valid
// */
console.log(isValid("0") == true);
console.log(isValid("1") == false);
console.log(isValid("12") == false);
console.log(isValid("42") == true);
console.log(isValid("999999") == false);
console.log(isValid("42---") == true);
console.log(isValid("2323aklsdfj 2005 mm7766ajsdkf 3554") == true);
console.log(isValid("999%%^^%%%999") == false);






/*
My questions:
- What happens if the input string is empty?
- What happens if we don't receive any input at all?
- What happens if we receive more than one input?
- Will the input always be a string, or might it be another data type?
- Is there a length requirement to the string? Should there be a certain number of digits?
- What happens if we receive a string with no digits?
- What happens if we receive a string with one digit? Do we just return the value of that digit itself?
- Does every second digit from the right mean that we don't count the right most digit itself? In other words, do we start multiplying by 2 based on the second to right digit?
- Do we count every second digit after cleaning the string of non-numeric digits?
- Do we need to worry about NaN or Infinity inputs?
*/



// console.log(calculateLuhnSum([1, 1, 1, 1]));


/*
FOLLOW UP QUESTION:
Write a function that can add a check digit to make the number valid per the Luhn formula and return the original number plus that digit. This should give "2323 2005 7766 3554" in response to "2323 2005 7766 355".
*/

/*
Input: String
Output: String

Rules:
- Same assumptions about input data type / input contents hold
- If the input is already valid, just return it as is
- We will simply append a new single string digit onto the input such that the output is valid.
- Don't worry about a scenario where we won't get a valid number after appending a digit

Input of 232320057766355 => 262620017563315 => 49. If we just took this sum, took difference vs 50, we would get 1
Adding 1 is wrong! We need to add 4. So we can't just take the sum and find the number that gets us to 50.
That's because we then multiply by the other digits, which changes the math.

Algorithm:

High-level:
- Check whether input is valid => isValid
- If it is valid, return the input.
- If not, append one digit at a time to the input and check whether result is valid.
  - Use a loop to loop through digits from 0 to 9, coercing them to a string and appending them to the end of the input
  - If result after a given digit is appended is valid, return that new string


ANOTHER WAY TO HAVE DONE THIS IS:
- If it isn't valid, then add a '0' to the input string and see what the sum is. Then, from there, all you have to do is
  figure out what # you need to add to that sum to get it to a number that ends in 0. You can use mod for that. More
  efficient than using a for loop.
*/

function addCheckDigit(string) {
  if (isValid(string)) {
    return string;
  }

  for (let digit = 0; digit < 10; digit += 1) {
    let digitStr = String(digit);
    let revisedString = string + digitStr;
    if (isValid(revisedString)) {
      return revisedString;
    }
  }
}



console.log(addCheckDigit('1111') == '11114');
console.log(addCheckDigit('8763') == '8763');
console.log(addCheckDigit("2323 2005 7766 3554") == '2323 2005 7766 3554');
console.log(addCheckDigit("2323 2005 7766 355") == '2323 2005 7766 3554');
console.log(addCheckDigit("0") == '0');
console.log(addCheckDigit("1") == '18');
console.log(addCheckDigit("12") == '125');
console.log(addCheckDigit("42") == '42');
console.log(addCheckDigit("999999") == '9999996');
console.log(addCheckDigit("42---") == "42---");
console.log(addCheckDigit("2323aklsdfj 2005 mm7766ajsdkf 3554") == "2323aklsdfj 2005 mm7766ajsdkf 3554");
console.log(addCheckDigit("999%%^^%%%999") == "999%%^^%%%9996");


/*
My questions:
- Is it okay to make the same assumptions about input data type / input contents as from the prior problem?
- If the input string is already valid, what do I return? =>
- Just to confirm- I should retain any non-numeric chars present in the input string, correct?
- Will there ever be a scenario where I need to include additional non-numeric chars in my output, or is it literally just appending on a single string digit?
- Do we have to worry about a scenario where we may not get a valid number after appending on a digit?
*/