/*
Write a program that asks the user to enter an integer greater than 0,
then asks if the user wants to determine the sum or the product of all numbers between 1 and the entered integer,
inclusive.
*/

const rlSync = require('readline-sync');

function getInteger() {
  let int;
  while (true) {
    int = parseInt(rlSync.question('Please enter an integer greater than 0: '), 10);
    if (int > 0) break;
    console.log("Invalid integer. Please try again.");
  }
  return int;
}

function getOperation() {
  let operation;
  while (true) {
    operation = rlSync.question('Enter "s" to compute the sum, or "p" to compute the product. ').toLowerCase().trim();
    if (operation === 's' || operation === 'p') break;
    console.log('Unsupported operation. Please try again.');
  }
  return operation;
}

function calculateSum(endInt) {
  let total = 0;
  for (let num = 1; num <= endInt; num += 1) {
    total += num;
  }
  return total;
}

function calculateProduct(endInt) {
  let total = 1;
  for (let num = 1; num <= endInt; num += 1) {
    total *= num;
  }
  return total;
}

let int = getInteger();
let operation = getOperation();
let total;
if (operation === 's') {
  total = calculateSum(int);
} else {
  total = calculateProduct(int);
}

console.log(`The ${operation === 's' ? 'sum' : 'product'} of the integers between 1 and ${int} is ${total}.`)

/*
What if the input was an array of integers instead of just a single integer?
How would your computeSum and computeProduct functions change?
Given that the input is an array, how might you make use of the Array.prototype.reduce() method?
*/

function calculateSum(intArray) {
  return intArray.reduce((accumulator, number) => accumulator + number, 0);
}

function calculateProduct(intArray) {
  return intArray.reduce((accumulator, number) => accumulator * number, 1);
}