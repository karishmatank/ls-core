/*
Write a function that takes a string and returns an object containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
You may assume that the string will always contain at least one character.


My questions
- Should we return an object with all values "0.00" if we have an empty string? EDIT: Irrelevant, re-read the problem
- Confirmed that the values are strings of 2 decimal places representing the percentages * 100
  - i.e. 50% => 50.00
- Will we always get a string input? What if we get another data type?
- Will we always get exactly 1 argument? What happens if we get 0 or more than 1?

Input: String
Output: Object with 3 properties (lowercase, uppercase, neither)
Rules:
- The output will have the % of chars that are lowercase, % of chars that are uppercase, % of chars that are neither
- The output value are strings of 2 decimal places representing the percentages * 100
- Lowercase and uppercase only pertain to alphabetical chars, all other characters are grouped under "neither"
- We won't get an empty string as input because we'll always get a string with at least one character
- Assume we will always get a string input, assume we'll only get 1 argument

Data structures:
- Store counts as we go -> object
- Store chars of input -> array

Algorithm:
- Create an object with 3 properties (lowercase, uppercase, neither), each with value 0 -> `counts`
- Create an array of the chars of the input
- For each character
  - If it is uppercase, increment `uppercase` property by 1
  - If it is lowercase, increment `lowercase` property by 1
  - Else, increment `neither` property by 1
- For each property in `counts`
  - Divide value by the length of the input string and multiply by 100
  - Format into string with 2 decimal places
*/

function letterPercentages(text) {
  let counts = text.split('').reduce((acc, char) => {
    if (char >= 'A' && char <= 'Z') {
      acc.uppercase += 1;
    } else if (char >= 'a' && char <= 'z') {
      acc.lowercase += 1;
    } else {
      acc.neither += 1;
    }
    return acc;
  }, {lowercase: 0, uppercase: 0, neither: 0});

  for (let prop in counts) {
    counts[prop] = (counts[prop] / text.length * 100).toFixed(2);
  }

  return counts;
}

console.log(letterPercentages('abCdef 123'));
// { lowercase: "50.00", uppercase: "10.00", neither: "40.00" }

console.log(letterPercentages('AbCd +Ef'));
// { lowercase: "37.50", uppercase: "37.50", neither: "25.00" }

console.log(letterPercentages('123'));
// { lowercase: "0.00", uppercase: "0.00", neither: "100.00" }

console.log(letterPercentages('ABCDEF')); // { lowercase: "0.00", uppercase: "100.00", neither: "0.00" }
console.log(letterPercentages('a')); // { lowercase: "100.00", uppercase: "0.00", neither: "0.00" }