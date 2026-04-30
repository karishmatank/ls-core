/*
THIS IS a hard problem that exceeds the level of difficulty you'll see in our assessments or in technical interviews.


You are given a list of numbers in a "short-hand" range where only the significant part of the next number is written because we know the numbers are always increasing (ex. "1, 3, 7, 2, 4, 1" represents [1, 3, 7, 12, 14, 21]). Some people use different separators for their ranges (ex. "1-3, 1-2", "1:3, 1:2", "1..3, 1..2" represent the same numbers [1, 2, 3, 11, 12]). Range limits are always inclusive.

Your job is to return a list of complete numbers.

The possible separators are: ["-", ":", ".."]

"1, 3, 7, 2, 4, 1" --> 1, 3, 7, 12, 14, 21
"1-3, 1-2" --> 1, 2, 3, 11, 12
"1:5:2" --> 1, 2, 3, 4, 5, 6, ... 12
"104-2" --> 104, 105, ... 112
"104-02" --> 104, 105, ... 202
"545, 64:11" --> 545, 564, 565, .. 611



My questions:
- The prompt says we are given a list of numbers. Is it more so that we're given a string that represents a list, including some sort of shorthand?
- How do we treat empty strings?
- How do we treat strings with values other than digits, commas, spaces, or the separators?
- Is my understanding as written below in the rules correct, under "How this works"?
- How do we work with a string that does not have any digits?
- If a string doesn't have any separators or commas, should we just return an array with one element, the number in the input string? i.e. if we get "1042" as input.
- What happens if we receive a string with a non-numeric digit at the start or end? How should that be treated? i.e. ":5" or "-3:5"
- Can we have negative numbers, NaN, or Infinity?
- Are items always separated by ', '?
- For a given range, can we have more than one type of separator present? Such as 1..3-5


P:
Input: String that represents a list using shorthand and separators
Output: Array of numbers
Rules:
- Given a string, we must decipher the numbers that are in the shorthand ranges. The array we return must include all of the numbers included in those ranges
- How it works
  - ', ' as the delimiter means there is more than one item in the list
    - The space around the comma is optional and may be omitted
  - Items can be standalone numbers or ranges
  - If we see a standalone number, that means we need to expand just that number to its "true form" (the full number)
  - If we see a separator (["-", ":", ".."]), then we are seeing a range that we need to expand into individual numbers in their "true form"
  - The expanded form of a number / its range depends on the value of the preceding expanded number
    - The shorthand gives us the "significant part" of the number, or the rightmost part of the expanded number that must still be present after we expand it
- The numbers are always increasing
- If we encounter a range, we include the start and end numbers in our output array
- If we get an empty string, return an empty array
- Assume we'll receive valid strings only
  - Input will only contain digits, commas, spaces, and valid separators
  - We will always get a string with at least one digit
  - We won't get any strings with a separator, comma, or space at the start or end of the input
  - We won't get negative numbers, NaNs, or Infinity
- If a string doesn't have any separators, commas, or spaces, just return an array with one element, which is the numeric representation of the string of digits passed in (i.e. "1042" => [1042])
- A single range expression uses one kind of range separator, not a mix.
- If we have a range with repeating start and end digits, that should resolve into an array with one element representing that digit.


Data structures:
Input: String
Output: Array of numbers

Items: Array of substrings from the input string
Separators: Stored in a const array


Algorithm:

High-level:
- Create a global constant SEPARATORS
- Create an array `result`
- Separate the input into each "item". Comma with / without trailing spaces
- Expand each item into its full number(s), adding all numbers into `result`
- Return `result`

HELPER: getExpandedNumber(strNumber, lastExpandedNumber)
- Coerce `strNumber` to a number -> `number`
- Get the length of strNumber -> `n`
- While number < lastExpandedNumber:
  - Raise a factor of 10 by `n` and add to `number` -> `number`
- Return `number`

HELPER: expandRange(strRange, lastExpandedNumber) => Array of numbers
- Create empty array `range`
- Separate `strRange` based on any of the separators present => `endpoints`
  - For each separator, if it is present in the string, then split the string into an array of digits based on that separator
  - Regex: split by /(-|..|:)/g
- If `lastExpandedNumber` is undefined, then set to 0
- For each element in `endpoints`:
  - Convert it into its full expanded number -> `expanded`
    - Use getExpandedNumber
  - Reset `lastExpandedNumber` to `expanded`
- If length of new endpoints is 1, return the new endpoints array
- For every two adjacent elements in the new endpoints:
  - Find all integers in between the elements and append to `range`, inclusive of each element. Only add in an integer if it isn't already in `range`.
- Return `range`

Main algorithm:
- Create a global constant SEPARATORS
- If the input is an empty string, return an empty array
- Create an array `result` ([])
- Separate the input into each "item". Comma with / without trailing spaces
  - Regex such as /\s*\,\s* /g
- Expand each item into its full number(s), adding all numbers into `result`
  - Use expandRange, pass in the item and the last element of `result` (if it exists)
  - Concatenate result of expandRange with `result`
- Return `result`
*/

const FACTOR  = 10;

function getExpandedNumber(strNumber, lastExpandedNumber) {
  let number = Number(strNumber);

  let n = strNumber.length;
  while (number < lastExpandedNumber) {
    number += 10 ** n;
  }

  return number;
}

function expandRange(strRange, lastExpandedNumber) {
  let range = [];
  let endpoints = strRange.split(/:|\.\.|-/g);
  lastExpandedNumber = lastExpandedNumber || 0;

  let expandedEndpoints = [];
  endpoints.forEach((endpoint) => {
    let expanded = getExpandedNumber(endpoint, lastExpandedNumber);
    expandedEndpoints.push(expanded);
    lastExpandedNumber = expanded;
  });

  if (expandedEndpoints.length === 1) {
    return expandedEndpoints;
  }

  for (let idx = 1; idx < expandedEndpoints.length; idx += 1) {
    let start = expandedEndpoints[idx - 1];
    let end = expandedEndpoints[idx];

    for (let num = start; num <= end; num += 1) {
      if (!range.includes(num)) {
        range.push(num);
      }
    }
  }

  return range;
}

function fullRange(string) {
  if (string === '') {
    return [];
  }
  let result = [];
  let items = string.split(/\s*,\s*/g);

  items.forEach(item => {
    let range = expandRange(item, result[result.length - 1]);
    result = result.concat(range);
  });

  return result;
}



console.log(fullRange("1, 3, 7, 2, 4, 1")); // [1, 3, 7, 12, 14, 21]
console.log(fullRange("1-3, 1-2")); // [1, 2, 3, 11, 12]
console.log(fullRange("1:5:2")); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
console.log(fullRange("104-2")); // [104, 105, 106, 107, 108, 109, 110, 111, 112]
console.log(fullRange("104-02").length === 99);
console.log(fullRange("545, 64:11").length === 49);
console.log(fullRange("104-2-1")); // [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121]
console.log(fullRange("1,3,7,2,4,1")); // [1, 3, 7, 12, 14, 21]

console.log(fullRange('')); // []
console.log(fullRange('1042')); // [1042]
console.log(fullRange('5:5')); // [5]


// "1, 3, 7, 2, 4, 1" --> 1, 3, 7, 12, 14, 21
// "1-3, 1-2" --> 1, 2, 3, 11, 12
// "1:5:2" --> 1, 2, 3, 4, 5, 6, ... 12
// "104-2" --> 104, 105, ... 112
// "104-02" --> 104, 105, ... 202
// "545, 64:11" --> 545, 564, 565, .. 611



// console.log(getExpandedNumber('11', 64));
// console.log(expandRange('104-02', 0));
