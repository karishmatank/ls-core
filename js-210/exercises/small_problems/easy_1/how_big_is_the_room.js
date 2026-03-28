/*
Build a program that asks the user to enter the length and width of a room in meters,
and then logs the area of the room to the console in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet

Do not worry about validating the input at this time. Use the readlineSync.prompt method to collect user input.
*/

const rlSync = require('readline-sync');
const SQUARE_FEET_PER_SQUARE_METER = 10.7639;

let length = parseFloat(rlSync.question('Enter the length of the room in meters:\n'));
let width = parseFloat(rlSync.question('Enter the width of the room in meters:\n'));

let squareMeters = length * width;
let squareFeet = squareMeters * SQUARE_FEET_PER_SQUARE_METER;

console.log(`The area of the room is ${squareMeters.toFixed(2)} square meters (${squareFeet.toFixed(2)} square feet).`)

/*
Modify the program so that it asks the user for the input type (meters or feet).
Compute for the area accordingly, and log it and its conversion in parentheses.
*/

let units;

while (true) {
  units = rlSync.question('What units will you be reporting measurements in? (meters or feet):\n').toLowerCase().trim();
  if (units === 'meters' || units === 'feet') {
    break;
  }
  console.log('Please specify either meters or feet.');
}

length = parseFloat(rlSync.question('Enter the length of the room:\n'));
width = parseFloat(rlSync.question('Enter the width of the room:\n'));

let squared = length * width;
if (units === 'meters') {
  squareMeters = squared;
  squareFeet = squareMeters * SQUARE_FEET_PER_SQUARE_METER;
} else {
  squareFeet = squared;
  squareMeters = squareFeet / SQUARE_FEET_PER_SQUARE_METER;
}

console.log(`The area of the room is ${squareMeters.toFixed(2)} square meters (${squareFeet.toFixed(2)} square feet).`)