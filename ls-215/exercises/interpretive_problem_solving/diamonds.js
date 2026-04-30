/*
THIS PROBLEM MATCHES THE LEVEL OF DIFFICULTY OF THE LS216 EXAM.

Write a function that displays a four-pointed diamond in an nxn grid, where n is an odd integer supplied as an argument to the function. You may assume that the argument will always be an odd integer.

My questions:
- What do we do if we don't get any argument?
- Just confirming that alwaysr receiving an odd integer means we won't get NaN or Infinity values or any non-integers or 0? Might we get a negative integer?
- What does an nxn grid mean? Does it mean that the output will be n chars wide and n rows long?
- We'll represent chars of the diamond with * chars
- If we have an input of 1, print a single *
- Does 4 pointed diamond refer to the middle row being the longest one with n *s?
- It looks like there's a consistent column of spaces (1 space before we start each row). Does that need to be output?
- Do we need to output spaces after we print the * chars?
- is there a max integer we should expect to receive? What do we do if we get an input above that?
- What if we receive more than one argument?


P:
Input: Odd integer
Output: Console log
Rules:
- An nxn grid is n chars wide and n rows long
- We'll represent chars of the diamond with * chars
- We should log a "4 pointed diamond" to the console in an nxn grid
  - The first row will have one *
  - Each row will keep incraseing by 2 *s until we get to the input # of stars
  - Then each subsequent row will decreasing by 2 each time until we get back to 1 *
- Assume the argument will always be an odd integer
- Assume we will always get an argument. Extra arguments can be ignored
- Assume we might get negative integers. If so, or if we get 0 as an input, return an empty string
- Don't worry about NaN, Infinity, -Infinity, or non-integers
- If we have an input of 1, print a single *
- We need to start with a consistent leading space for each row, regardless of how many other spaces or *s we need for that row
- No need to print trailing spaces after finishing printing the *s
 (8:30 P)

(9:15 after E)

Data structures:
Input: num
Output: strings to the console
Rules:
- # of stars and # of spaces per row -> each numbers
- String output per row -> array

Algorithm:

HELPER: createStarCounter(n) -> number of stars
- Initialize `numStars`
- Let `increasing` equal true
- Return a closure:
  - If `numStars` is undefined:
    - Reassign `numStars` to 1
  - Else if `increasing` is true:
    - Increment `numStars` by 2
    - If `numStars` now equals `n`:
      - Change `increasing` to false
  - Else:
    - Decrement `numStars` by 2
  - Return `numStars`

Main algorithm
- If `n` is < 1, print an empty string to the console and return
- Create empty array `rows`
- Create const STAR_SYMBOL to '*'
- CREATE const SPACE_SYMBOL to ' '
- Create our star counter -> `getStarCount`
  - Use createStarCounter
- For a range of num from 0 to `n` (input) (exclusive):
  - Get the number of stars for the row -> `numStars`
    - Invoke `getStarCount`
  - Let `numSpaces` equal (`n` - `numStars`) / 2
  - Add one space for the leading space per row -> `numSpaces` add 1
  - Add a string with `numSpaces` number of spaces followed by `numStars` number of stars to `rows`
- For each element of `rows`:
  - Print to the console

*/

function createStarCounter(n) {
  let numStars;
  let increasing = true;
  return function() {
    if (numStars === undefined) {
      numStars = 1;
    }
    else if (increasing) {
      numStars += 2;
      if (numStars === n) {
        increasing = false;
      }
    } else {
      numStars -= 2;
    }

    return numStars;
  }
}

function diamond(n) {
  if (n < 1) {
    console.log('');
    return;
  }

  let rows = [];
  const STAR_SYMBOL = '*';
  const SPACE_SYMBOL = ' ';

  let getStarCount = createStarCounter(n);

  for (let i = 0; i < n; i += 1) {
    let numStars = getStarCount();
    let numSpaces = (n - numStars) / 2 + 1;
    let row = `${SPACE_SYMBOL.repeat(numSpaces)}${STAR_SYMBOL.repeat(numStars)}`;
    rows.push(row);
  }

  rows.forEach(row => console.log(row));
}


diamond(1);
// *

diamond(3);
// logs
//  *
// ***
//  *

diamond(9);
// logs
//     *
//    ***
//   *****
//  *******
// *********
//  *******
//   *****
//    ***
//     *

diamond(9, 11);
// logs
//     *
//    ***
//   *****
//  *******
// *********
//  *******
//   *****
//    ***
//     *

diamond(-1); // (empty str)