/*
A user wrote a function that takes an array as an argument and returns its average.
Given the code below, the user expects the average function to return 5.
Is the user's expectation correct? Why or why not?
*/

const myArray = [5, 5];
myArray[-1] = 5;
myArray[-2] = 5;

function average(array) {
  let sum = 0;

  for (let i = -2; i < array.length; i += 1) {
    sum += array[i];
  }

  return sum / array.length;
}

console.log(average(myArray));


/*
No, this will return 10.

array.length is only 2. The length property for arrays only takes into account non-negative integer indices.
In this case that would only be 0 and 1, so the length is 2.
The for loop  iterates over the properties with keys -2, -1, 0, and 1, as we are starting at -2 and incrementing
upward until we get to 2 (exclusive).

The issue lies with dividing that resulting sum, which will be 20, by 2, which only yields 10.
*/

/*
Refactor the average function so that it returns the result that the user expected, 5.
*/

function averageV2(array) {
  let sum = 0;

  for (let i = -2; i < array.length; i += 1) {
    sum += array[i];
  }

  return sum / Object.keys(array).length;
}

console.log(averageV2(myArray));
