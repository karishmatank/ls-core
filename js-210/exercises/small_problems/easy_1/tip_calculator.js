/*
Create a simple tip calculator. The program should prompt for a bill amount and a tip rate.
The program must compute the tip, and then log both the tip and the total amount of the bill to the console.
You can ignore input validation and assume that the user will put in numbers.
*/

const rlSync = require('readline-sync');

let bill = parseFloat(rlSync.question('What is the bill? '));
let tipPercentage = parseFloat(rlSync.question('What is the tip percentage? '));

let tip = bill * tipPercentage / 100;
let total = bill + tip;

console.log(`The tip is $${tip.toFixed(2)}\nThe total is $${total.toFixed(2)}`);