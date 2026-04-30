/*
Q1:
A distinct string is a string that is present only once in an array.

Given an array of strings, arr, and an integer, k, return the kth distinct string present in arr.
If there are fewer than k distinct strings, return an empty string "".

Note that the result string is the one encountered earliest in the array.

Example:
distinctString(["d","b","c","b","c","a"], 2); // "a"



My questions:
- Should we count # of distinct strings from left to right? What's the order?
  - Similarly, does "earliest" mean the leftmost seen?
- Will we always get an array as the first argument? If not, how should we think about return value?
- Will our array always have at least k strings? => (I guess if not, we just return '').
- Will each element always be a string? If not, how should we treat non-strings?
  - For example, do we have to do any coercions?
- Should the comparison be case insensitive?
- Does an empty string count as a distinct string, or must the string have a certain # of characters?
- Should we worry about the types of characters in the strings? Should we only count strings with alphabetic characters?
- Will we always get an integer as the second argument? If not, is there a specific default value or return value?
- Should the entire strings be compared to each other? Does "present only once" also include substrings
  present within other elements?
- Does "distinct" mean that the string is present more than once in the array?
- [MISSED] What should we do if we get more than 2 arguments?
- [MISSED] Will the second argument ever be 0? If so, how should we treat it?
- [MISSED] Will the second argument ever be negative? If so, how should we treat it?
- [MISSED] Will the input array ever be sparse? If so, how should we treat it?
- [MISSED] Can the array be empty?
*/

/*
Q2:
Given an array of integers, nums, return the third largest number in the array.
If the third largest number does not exist, return the greatest number.

You are not allowed to sort the array.

Example:
thirdMax([3, 2, 1]); // 1



My questions:
- Will an array always be passed in? If not, what should we return?
- Will the first argument always be an array?
- Will the elements always be integers? If not, how should we handle them?
- Is comparison based on numerical value, or something else? (Sort of nonsensical but threw it in anyway)
- Will there always be elements in the array? What should we return if we receive an empty array?
- Can the arrays be sparse? If so, do we just skip over empty slots?
- Can the array have NaNs? How should we handle those?
- Can the array have Infinities? If so, does that count as the largest number?
- Can the array have duplicate elements? Do we count duplicates as separate numbers,
  or do we only count one occurrence towards the "third largest number" designation?
- How should we treat any custom properties on the array? Do they count as elements?
  - If so, do we just count their values towards the comparison?
- Can the array have fractional numbers, or will they always just be integers?
- [MISSED] What should we do if we get more than 1 argument?
- [MISSED] Does the order of the elements in the array as initially presented matter at all?
- [MISSED] Can the elements be 0 or negative?
*/

/*
Q3:
Write a function, primeNumberPrinter, that prints all prime numbers present as substrings in a given string.

Example
primeNumberPrinter("a4bc2k13d"); // [2, 13]



My questions:
- Will the string always have digits? What should we return if the string doesn't?
- Do we treat consecutive digits as one number? (Seems like we do based on the example)
- Is a number defined as consecutive digits with letters on either side?
- Can the string have other types of characters other than letters, such as punctuation, spaces, etc?
- Are the numbers base 10 numbers?
- Can there be numbers such as NaN, Infinity, or -Infinity present?
- What happens if we don't receive a string as input?
- What happens if we receive an empty string as input?
- Can the numbers be negative? Will there ever be '-' characters present in the string?
- Is there a minimum or maximum number that we may see in the string?
- If the string contains only digits, is that then treated as the only number in the string?
- Should we parse the string for numbers from left to right?
- Might there be both uppercase and lowercase letters in the string?
- Is a prime number defined as only divisible by 1 and itself?
- If we don't have any prime numbers in our string, should we just return an empty array?
- Are we returning an array, as implied by the example, or are we just printing to the console?
- Should we print / return the numbers in any particular order?
  - For example, the order in which they appear? In order from lowest to highest?
- What happens if we receive no arguments?
- What happens if we receive more than one argument?
*/

/*
Q4:
​Write a function that takes a two-dimensional array as the argument and turns it into a flat array
with all duplicated elements removed.
Treat numbers and number strings (e.g., 1 and '1') as duplicates, and keep the one that comes first in the result.

flattenAndUnique([]); // []
flattenAndUnique([[1, 2, 3], ['3', 4, 5, 'a']]); // [1, 2, 3, 4, 5, 'a']


My questions:
- Will we always receive a 2D array as an argument? Is it possible we receive a 1D array? If so, how should we proceed?
- What do we do if we don't receive any arguments?
- What do we do if we receive more than one argument?
- Is there a minimum / maximum number of subarrays that we'll get in as an argument?
- What data types should we expect for the elements?
- Do duplicates also account for the obvious matches in both type and value?
- Besides numbers and number strings, what other types of duplicates should we account for?
- What does "first" entail? Does it mean the element that appears leftmost / with the lower index value or in a subarray with a lower index value?
- What happens if we receive an empty array? => Return an empty array
- Is there a particular order that the elements in the final array should be in? I.e. ordered based on when we encounter them in the subarrays?
- Will we get any NaN values in our input? What about Infinity or -Infinity?
- [MISSED] What if we receive a non-array as an argument?
- [MISSED] Can the nested arrays contain other arrays / objects as elements?
  - If so, what does "duplicate" mean for those?
- [MISSED] Can the array be sparse? If so, do I skip over missing elements?
- [MISSED] What happens if the subarrays are empty?
- Can the arrays / subarrays have custom properties? If so, do those have to be duplicated too?
*/