/*
THIS PROBLEM IS HARDER THAN WHAT WE'LL SEE ON THE LS216 EXAM.

Write a function that displays an 8-pointed star in an nxn grid, where n is an odd integer that is supplied as an argument to the function. The smallest such star you need to handle is a 7x7 grid (i.e., when n is 7).

My questions
- Is my understanding of 8-pointed star correct?
  - Looks as if we draw a star as if it were a big asterisk (*) with an additional horizontal line
  - Esseentially, draw a horizontal line, two diagonal lines, and a vertical line
- Will we always receive a number as an input? Or might we receive another data type?
- Will we always receive one input? What do we do if we receive 0 or more than 1 input?
- Is it guaranteed that we will always receive an odd integer as our input? What do we do if we don't receive an integer, or if we receive an even integer?
- Will the integer always be positive? What do we do if we receive a negative integer?
- Confirm that we won't receive NaN or Infinity sorts of values as the input?
- What happens if we receive an integer < 7 as the input?
- Should the output just have * and ' ' chars? Will there be a time when we need other chars?
- Confirm that the spaces that we include in the output are only on the "left" side, meanign we don't fill in spaces after hte last * of each row in order to meet the nxn definition


Input: Number (n)
Output: Print a star to the console
Rules:
- The star we print is an 8-pointed star
  - Looks as if we draw a star as if it were a big asterisk (*) with an additional horizontal line
  - Esseentially, draw a horizontal line, two diagonal lines, and a vertical line
  - Each row always has 3 *s but varying number of spaces
- We want to draw the star over an nxn grid (n rows, n cols)
- Assume exactly 1 number argument, no other data types will be passed in
- Assume `n` is an odd integer >= 7, don't worry about negative integers or smaller positive integers, NaN, or Infinity
- Output will only have * and ' ' chars
- Only need to pad the "left" side of the *s with spaces

Data structures:
- Store each row to be printed -> array (nested array)


Algorithm:

HELPER: createSpaceTracker(`n`) -> Array of numbers
- Set leftPadSpaces to -1
- Set betweenAsteriskSpaces to undefined
- Set const NUM_ASTERISKS_PER_ROW to 3

- Return function:
  - Set leftPadSpaces to its prior value + 1
  - Set betweenAsteriskSpaces to:
    (`n` - NUM_ASTERISKS_PER_ROW - (leftPadSpaces * 2)) / 2
  - Return array with leftPadSpaces, betweenAsteriskSpaces as elements

High-level:
- Set const STAR_SYMBOL to '*'
- Set const SPACE_SYMBOL to ' '
- Invoke createSpaceTracker -> `getSpaces`

- Set `rows` to an empty array with length `n`
- Find the index of the middle row
  - Middle row index = the floor of `n` / 2
  - Set the element at that index in `rows` to a string of `n` STAR_SYMBOLs
- Iterate from indices 0 to middle row index (exclusive) of `rows`:
  - Invoke `getSpaces` -> `spaces`
  - Find the number of left pad spaces
    - first element of `spaces`
  - Find the number of spaces between STAR_SYMBOLs
    - Second element of `spaces`
  - Construct string -> left pad spaces + asterisk + spaces between asterisks + asterisk + spaces between asterisks + asterisk -> `rowOutput`
  - Add `rowOutput` to the specified index in `rows`
  - Add `rowOutput` to the `n` - 1 - index row in `rows`
- For each row in `rows`:
  - Print the row to the console

*/

function createSpaceTracker(n) {
  let leftPadSpaces = -1;
  let betweenAsteriskSpaces;
  const NUM_ASTERISKS_PER_ROW = 3;

  return function() {
    leftPadSpaces += 1;
    betweenAsteriskSpaces = (n - NUM_ASTERISKS_PER_ROW - (leftPadSpaces * 2)) / 2;
    return [leftPadSpaces, betweenAsteriskSpaces];
  }
}

function star(n) {
  const STAR_SYMBOL = '*';
  const SPACE_SYMBOL = ' ';
  let getSpaces = createSpaceTracker(n);

  let rows = [];
  rows.length = n;

  let middleIdx = Math.floor(n / 2);
  rows[middleIdx] = STAR_SYMBOL.repeat(n);

  for (let idx = 0; idx < middleIdx; idx += 1) {
    let [ leftPadSpaces, betweenAsteriskSpaces ] = getSpaces();
    let rowOutput = SPACE_SYMBOL.repeat(leftPadSpaces) + STAR_SYMBOL + SPACE_SYMBOL.repeat(betweenAsteriskSpaces) + STAR_SYMBOL + SPACE_SYMBOL.repeat(betweenAsteriskSpaces) + STAR_SYMBOL;
    rows[idx] = rowOutput;
    rows[n - 1 - idx] = rowOutput;
  }

  rows.forEach(row => console.log(row));
}


/*
NOTES: I definitely did not need the closure here. Closures are nice when we need to keep track of state, perhaps
in a unique way other than what a for loop or other regular-way tracker can provide. Here, the indices
we iterate over end up literally being the leftPadSpaces, and the math then for the spaces between asterisks
ends up being super simple. We could have easily just done:

function getSpaces(idx, n) {
  const NUM_ASTERISKS_PER_ROW = 3;
  return [idx, (n - NUM_ASTERISKS_PER_ROW - (idx * 2)) / 2];
}

Take care to try not to overcomplicate the algorithm just because you like using closures....
However, closures are helpful sometimes, just try not to overcomplicate everything.
*/


star(7);
// logs
/*
*  *  *
 * * *
  ***
*******
  ***
 * * *
*  *  *
*/

star(9);
// logs
/*
*   *   *
 *  *  *
  * * *
   ***
*********
   ***
  * * *
 *  *  *
*   *   *
*/

star(11);
// logs
/*
*    *    *
 *   *   *
  *  *  *
   * * *
    ***
***********
    ***
   * * *
  *  *  *
 *   *   *
*    *    *
*/