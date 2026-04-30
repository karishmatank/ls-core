/*

My questions:
- Might the array contain other data types besides numbers and strings? If so, how should we sort those?
- Will all elements in an array be of the same data type?
- Confirming that if two elements in a pair have the same value, we just keep the order of that pair as is?
- What happens if we receive more than one input? No input at all?
- Do we have to worry about sparse arrays or arrays with custom properties?


Input: Array
Output: Array (same array, sorted using bubble sort)
Rules:
- Bubble sort works by making multiple passes through the argument
  - Choose a pair of two consecutive numbers
  - If the left is <= the right, move to next pair
  - Otherwise, swap them such that the left is now on the right and the original right is now on the left
  - Keep iterating from left to right through the array until we don't make any swaps for one full "cycle"
- We should mutate the input array
- Assume the array contains at least 2 elements
- Assume that we'll only see arrays with numbers or strings
- Assume that a given array will only include elements of one data type
- Assume we'll always get one input only
- Don't worry about sparse arrays or arrays with custom properties


Data structures:



Algorithm:

Main:
- Set `swaps` to 0
- Iterate through each pair of the array (index of 1 to the end of the array)
  - For each pair, check if left element is <= right element
    - If not
      - reassign left index to the right element and reassign right index to the left element
      - Increment `swaps` by 1
- If `swaps` is 0, we're done
- Else, repeat the prior steps again

*/


function bubbleSort(array) {
  while (true) {
    let swaps = 0;

    for (let idx = 1; idx < array.length; idx += 1) {
      let [ left, right ] = [array[idx - 1], array[idx]];
      if (left > right) {
        array[idx - 1] = right;
        array[idx] = left;
        swaps += 1;
      }
    }

    if (swaps === 0) {
      break;
    }
  }
}


const array1 = [5, 3];
bubbleSort(array1);
console.log(array1);    // [3, 5]

const array2 = [6, 2, 7, 1, 4];
bubbleSort(array2);
console.log(array2);    // [1, 2, 4, 6, 7]

const array3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie'];
bubbleSort(array3);
console.log(array3);    // ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]