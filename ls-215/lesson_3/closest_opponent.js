/*
Write a function that returns the position of the closest active opponent. If two opponents are equidistant, return the opponent with the higher position on the board.



My questions:
- Can we confirm that we'll always get an object as the first argument, whereas the second argument will be a number with our current position?
- Will the object argument always have numbers as its values, representing its position?
- If the opponent is active, will their position in the object always be an integer?
- What about positions of 0? Is there a min / max value that the positions can be?
- Also, are there a min / max number of opponents that we'll see in the object?
- Does "closest" mean the absolute value of the difference between my position and the opponent's position?
- What happens if we receive an object with no active opponents?
- What happens if we receive an object with 1 active opponent?
- What happens if we have two opponents with the closest distance that are each at the same position? Is that possible?
- Do we need to worry about NaN/ Infinity?


P:
Input: Object representing positions of opponents, number representing our position
Output: Number representing position of closest opponent
Rules:
- We should return the position of the closest active opponent
- Active means the opponent has a valid integer position
- Closest means the absolute value of the difference between my position and the opponent's position
- If two opponents are "closest", return the position that is the higher absolute number (higher position value)
- The first argument will always be an object, the second will always be an integer. Don't worry about handling missing arguments or wrong-typed arguments
- In the object, the values (positions of opponents) can either be 1) numbers if an opponent is active or 2) null if the opponent is not active
  - If the opponent is active, their position in the object will always be a positive integer
- Positions won't be 0, just positive integers
- If the object we receive is empty, we should return null
- Assume that at least one opponent will be active
- If we receive only one active opponent, we just return their position
- It is not possible to have two opponents with the same position
- No significance of the names of the opponents

Data structures:
Input: Object, number
Output: Number or null

Opponent positions: Array of numbers (positions)


Algorithm:

HELPER: getClosestPosition(oppPositions, myPosition) -> number
- Set `smallestDiff` to Infinity
- Set `largestPosition` to null
- For each position in `oppPositions`:
  - Calculate the abs value of the diff between position and `myPosition`
  - If the abs diff is < `smallestDiff`:
    - Reassign `smallestDiff` to this abs diff
    - Reassign `largestPosition` to the current opponent position
  - Else if abs diff is equal to `smallestDiff`
    - Reassign `largestPosition` to the max of `largestPosition` or the current position
- Return `largestPosition`

Main algorithm:
- If the object is empty (if there are no properties), return null
- Get the positions of the opponents, place them in array `oppPositions`
- Filter out null values from `oppPositions`
- Return the largest position
  - Use `getClosestPosition`
*/

function getClosestPosition(oppPositions, myPosition) {
  let smallestDiff = Infinity;
  let largestPosition = null;
  oppPositions.forEach(position => {
    let diff = Math.abs(position - myPosition);
    if (diff < smallestDiff) {
      smallestDiff = diff;
      largestPosition = position;
    } else if (diff === smallestDiff) {
      largestPosition = Math.max(largestPosition, position);
    }
  });

  return largestPosition;
}

function findClosestOpponent(positions, position) {
  if (Object.keys(positions).length === 0) {
    return null;
  }

  let oppPositions = Object.values(positions).filter(position => position !== null);

  return getClosestPosition(oppPositions, position);
}

console.log(findClosestOpponent({
  "Opponent 1" : 1,
  "Opponent 2" : 15,
  "Opponent 3" : 37
}, 10) === 15); // 15

console.log(findClosestOpponent({
  "Opponent 1a" : 1,
  "Opponent 1b" : 5
}, 3) === 5); // 5

console.log(findClosestOpponent({
  "Opponent 1a" : 1, "Opponent 1b" : 5,
  "Opponent 1c" : 50, "Opponent 1d" : 100, "Opponent 1e" : null
}, 150) === 100); // 100

console.log(findClosestOpponent({}, 1) === null);
console.log(findClosestOpponent({
  'Opponent 1': 2
}, 1) === 2);

console.log(findClosestOpponent({
  'Opponent 1': 2,
  'Opponent 2': null,
}, 1) === 2);



/*
oppPositions = [1, 5]
position = 3

smallestDiff = 2
largestPosition = 5
*/

/*
oppPositions = [2]
position = 1

smallestDiff = 1
largestPosition = 2
*/