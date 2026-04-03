/*
Write a program that solicits six numbers from the user and logs a message that describes whether the
sixth number appears among the first five numbers.
*/

const rlSync = require('readline-sync');

function getSuffix(num) {
  switch (num) {
    case 1:
      return 'st'
    case 2:
      return 'nd'
    case 3:
      return 'rd'
    default:
      return 'th'
  }
}

function getNumbers() {
  let numbers = [];
  for (let i = 1; i <= 5; i += 1) {
    let number = parseInt(rlSync.question(`Enter the ${i}${getSuffix(i)} number: `), 10);
    numbers.push(number);
  }
  return numbers;
}

function getSearchNumber() {
  return parseInt(rlSync.question(`Enter the last number: `), 10);
}

let numbers = getNumbers();
let searchNumber = getSearchNumber();
if (numbers.includes(searchNumber)) {
  console.log(`The number ${searchNumber} appears in [${numbers.join(', ')}].`)
} else {
  console.log(`The number ${searchNumber} does not appear in [${numbers.join(', ')}].`)
}