/*
Q1:
We need a piece of reusable code that returns the average of three numbers.
Define a function named average that takes three parameters, a, b, and c, and returns their average.
Call the function with three numbers and log the result.
*/

function average(a, b, c) {
  return (a + b + c) / 3;
}

console.log(average(1, 3, 5));

/*
Q2:
We now need a function that calculates the sum of the same three values.
Create a function named sum that takes the same three arguments as average, and returns the sum of the three arguments.
 Now modify average to call the sum function with those three arguments and use the return value to calculate the average.
*/

function sum(a, b, c) {
  return a + b + c;
}

function average(a, b, c) {
  return sum(a, b, c) / 3;
}

console.log(average(1, 3, 5));

/*
Q3:
Suppose we have a bunch of values for which we want to calculate an average.
Our current average function only takes three numbers; we might need to write additional functions
if we want to work with different numbers of data points.
A better solution, though, is to change the function to accept an array of arbitrary length.
We can calculate the average by looping over the array elements to calculate the total, then divide by the array length.

Create a variable named total with an initial value of 0 at the start of the average function.
Use a for loop to iterate over all the elements in the array. With each iteration, add the element's value to the total.
When the loop finishes, return the total divided by the array's length.
Call average with an array of five numbers and log the result.
*/

// function sum(a, b, c) {
//   return a + b + c;
// }

function average(numArray) {
  let total = 0;

  // // Option 1
  // for (let idx = 0; idx < numArray.length; idx += 1) {
  //   total += numArray[idx];
  // }

  // // Option 2
  // for (let num in numArray) {
  //   total += numArray[num];
  // }
  // // Note that option 2 is not recommended for arrays, as it will also iterate over any other properties
  // // that exist within the array, not just the properties with integer keys.

  // Option 3
  numArray.forEach((num) => total += num);

  return total / numArray.length;
}

console.log(average([1, 3, 5, 6, 8]));

/*
Q4:
We should make the same changes to the sum function so we can continue to use it from the average function.
Since we've already written that functionality in average, we can just move it from there to sum.
Move everything from average into sum, except for the final return statement.
The sum function should return the total, and average should call the sum function with the same values,
then divide the return value by the array length, and return it.

As before, call average with an array of five numbers and log the result.
*/

function sum(numArray) {
  let total = 0;
  numArray.forEach((num) => total += num);
  return total;
}

function average(numArray) {
  return sum(numArray) / numArray.length;
}

console.log(average([1, 3, 5, 6, 8]));

/*
With the refactors done for question 3 and 4, we can now use our functions to determine the average of all
the numbers in an arbitrary array of numbers.
Create an array named temperatures and store five temperature values in it.
Find the average temperature by passing the array to the average function and log the result.
*/

let temperatures = [70, 80, 79, 82, 90];
console.log(average(temperatures));