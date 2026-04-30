/*
THIS PROBLEM MATCHES THE LEVEL OF DIFFICULTY OF THE LS216 EXAM.

You have a bank of switches before you, numbered from 1 to n. Every switch is connected to exactly one light that is initially off. You walk down the row of switches and toggle every one of them. You walk back to the beginning of the row and start another pass. On this second pass, you toggle switches 2, 4, 6, and so on. On the third pass, you go back to the beginning again, this time toggling switches 3, 6, 9, and so on. You continue to repeat this process until you have gone through n repetitions.

Write a program that takes one argument—the total number of switches—and returns an array of the lights that are on after n repetitions.


My questions:
- Will the input always be a number? What about if it is another data type?
- What happens if we don't receive any arguemnt? What about if we receive more than one?
- Will the input always be a positive integer? What if it is 0, or a negative int, or a decimal / non integer?
- How should we represent the output? Should it always be an array of the lights that are on?
- Within the output, when we reference lights that are on, is it 1-indexed, or 0-indexed? i.e. if the first light is on, do we reference it using 0 or 1?
- If no lights are on, do we just return an empty array?



P:
Input: Number
Output: Array of integers

Rules:
- The output includes the indices of the lights that are on:
  - Indices are **1-indexed**, NOT 0-indexed
  - I.e. if the first light is on, it should be represented at 1, not 0 in the output
- All n lights start as off. We flip a switch on based on the number of the pass we are making:
  - First pass: Every 1 switch is flipped from the beginning (every switch)
  - Second pass: Every 2nd switch is flipped from the beginning (if we start at 1, then 2, 4, 6, ... are flipped)
  - Etc
  - We make n passes, same as number of switches we have
- Input will be a numeric value, not any other data type.
- Only concerned with first argument. Don't worry about receiving no arguments or multiple arguments
- Don't need to support 0, negative integers, or non-integers. Input will be a valid positive integer, not NaN or Infinity
- If no lights are on, we just return an empty array

P ~10.5 min

E ~13 min


Data structures:
- Input: number
- Output: Array of numbers

- Lights: Array of boolean -> boolean of whether light is on (true) or off (false)


Algorithm:

High-level:
- Initialize an array `switchOnStatus` to ['X'] (will be used to align indices correctly)
- Create an array, total # of elements is the input, elements should all have value false -> `switchOnStatus`
  - For a number starting at 0 until the input `n` - 1:
    - Add an element `false` to the array
- For a `runNumber` starting from 1 and ending at `n` inclusive (`n` is the input):
  - Iterate through `switchOnStatus` from indices 1 to the end:
     - If the index of the element of `switchOnStatus` is evenly divisible by `runNumber`, toggle the boolean to be the opposite of whatever value it is
- Filter `switchOnStatus` for indices of elements that are boolean true
  - Create an array `onIndices`
  - If `switchOnStatus` is true for a given index, push the index to `onIndices`
- Return the filtered list


A ~24 min or so

Total time ~31 min
*/


function lightsOn(switches) {
  let switchOnStatus = ['X'];
  for (let idx = 0; idx < switches; idx += 1) {
    switchOnStatus.push(false);
  }

  for (let runNumber = 1; runNumber <= switches; runNumber += 1) {
    for (let switchIdx = 1; switchIdx < switchOnStatus.length; switchIdx += 1) {
      if (switchIdx % runNumber === 0) {
        switchOnStatus[switchIdx] = !switchOnStatus[switchIdx];
      }
    }
  }

  let onIndices = [];
  switchOnStatus.forEach((status, idx) => {
    if (status === true) {
      onIndices.push(idx);
    }
  });

  return onIndices;
}

console.log(lightsOn(5));        // [1, 4]
// Detailed result of each round for `5` lights
// Round 1: all lights are on
// Round 2: lights 2 and 4 are now off;     1, 3, and 5 are on
// Round 3: lights 2, 3, and 4 are now off; 1 and 5 are on
// Round 4: lights 2 and 3 are now off;     1, 4, and 5 are on
// Round 5: lights 2, 3, and 5 are now off; 1 and 4 are on


/*
['x', true, false, false, true, false]

runNumber = 5
[1, 4]
*/

console.log(lightsOn(100));      // [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

console.log(lightsOn(1)); // [1]
console.log(lightsOn(2)); // [1]


/* I only realized at the end of this that I could have saved time by only filtering for numbers from 1 to the input that are perfect squares....
*/

/* Could have also used reduce at the end:
return switchOnStatus.reduce((acc, status, idx) => {
  if (status === true) {
    acc.push(idx);
  }
  return acc;
}, []);
*/