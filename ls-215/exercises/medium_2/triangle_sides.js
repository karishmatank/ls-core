/*
A triangle is classified as follows:

Equilateral: All three sides are of equal length.
Isosceles: Two sides are of equal length, while the third is different.
Scalene: All three sides are of different lengths.

To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.


My questions:
- Will we always get numbers as input? What happens if we get anything that isn't a number?
- What happens if we get fewer or greater than 3 inputs? What should our program do?
- Confirm that we might get a number < 0 as an input
- Will we always get integers? Are non-integer inputs still valid to work with?
- Do we have to worry about getting NaN values as input, or Infinity / -Infinity?
- Confirm that the order in which we receive inputs doesn't matter
- Confirm that if the sum of 2 shortest = longest, that still isn't a valid triangle


Input: 3 numbers
Output: String (one of 'equilateral', 'isosceles', 'scalene', or 'invalid')
Rules:
- Valid triangle = sum of 2 shortest > longest, all sides > 0
- Equilateral means all 3 sides are equal length
- Isosceles means 2 sides equal, 3rd is not
- Scalene means all 3 different
- Assume inputs always numbers
- Assume exactly 3 arguments will be provided
- We might receive negative inputs
- We might receive non-integer inputs as well
- Don't worry about NaNs or Infinity / -Infinity
- Order in which we get the inputs does not matter


Data structures:
- Sides -> array
- Count the unique side values -> object, or array


Algorithm:

High-level:
- Check if the numbers create a valid triangle
- If not, return "invalid"
- If so, figure out if triangle is equilateral, isosceles, or scalene and return the appropriate string

HELPER: isValidTriangle(sides) -> boolean
- Create a copy of input array -> `sidesCopy`
- Sort `sidesCopy` from smallest side to largest
- If 0th element of `sidesCopy` <= 0
  - Return false
- If sum of 0th and 1st elements are > 2nd element
  - Return true
- else
  - Return false

HELPER: determineTriangle(sides) -> string
- Create an empty array `unique`
- Iterate through `sides` -> `side`
  - If `side` is not in `unique`, add it
- If `unique` length is 1:
  - Return 'equilateral'
- Else if `unique` length is 2:
  - Return 'isosceles'
- Else
  - Return 'scalene'


Main:
- Put numbers into array -> `sides`
- Check if the numbers create a valid triangle
  - Use isValidTriangle
- If not, return "invalid"
- If so, figure out if triangle is equilateral, isosceles, or scalene and return the appropriate string
  - Use determineTriangle

*/

function isValidTriangle(sides) {
  let sidesCopy = [...sides];
  sidesCopy.sort((a, b) => a - b);

  let [ smallest, mid, largest ] = sidesCopy;
  if (smallest <= 0) {
    return false;
  }

  return smallest + mid > largest;
}

function determineTriangle(sides) {
  let unique = sides.reduce((acc, side) => {
    if (!acc.includes(side)) {
      acc.push(side);
    }
    return acc;
  }, []);

  if (unique.length === 1) {
    return 'equilateral';
  } else if (unique.length === 2) {
    return 'isosceles';
  } else {
    return 'scalene';
  }
}

function triangle(...sides) {
  if (!isValidTriangle(sides)) {
    return "invalid";
  }

  return determineTriangle(sides);
}


console.log(triangle(3, 3, 3));        // "equilateral"
console.log(triangle(3, 3, 1.5));      // "isosceles"
console.log(triangle(3, 4, 5));        // "scalene"
console.log(triangle(0, 3, 3));        // "invalid"
console.log(triangle(3, 1, 1));        // "invalid"

console.log(triangle(3, 1, 2));        // "invalid"
console.log(triangle(3, -1, 2));        // "invalid"
