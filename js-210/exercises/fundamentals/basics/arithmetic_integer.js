/*
Write a program that prompts the user for two positive integers,
and then prints the results of the following operations on those two numbers:
addition, subtraction, product, quotient, remainder, and power. Do not worry about validating the input.
*/

// Example
// ==> Enter the first number:
// 23
// ==> Enter the second number:
// 17
// ==> 23 + 17 = 40
// ==> 23 - 17 = 6
// ==> 23 * 17 = 391
// ==> 23 / 17 = 1
// ==> 23 % 17 = 6
// ==> 23 ** 17 = 1.4105003956066297e+23


let rlSync = require('readline-sync');
let firstNum = parseInt(rlSync.question("Enter the first number:\n"));
let secondNum = parseInt(rlSync.question("Enter the second number:\n"));

console.log(`${firstNum} + ${secondNum} = ${firstNum + secondNum}`);
console.log(`${firstNum} - ${secondNum} = ${firstNum - secondNum}`);
console.log(`${firstNum} * ${secondNum} = ${firstNum * secondNum}`);
console.log(`${firstNum} / ${secondNum} = ${parseInt(firstNum / secondNum)}`);
console.log(`${firstNum} % ${secondNum} = ${firstNum % secondNum}`);
console.log(`${firstNum} ** ${secondNum} = ${firstNum ** secondNum}`);