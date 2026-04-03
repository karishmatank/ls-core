/*
Build a program that randomly generates Teddy's age, and logs it to the console.
Have the age be a random number between 20 and 200 (inclusive).

Example Output:

Teddy is 69 years old!

*/

function generateRandomNumber(minimum, maximum) {
  let multiplier = Math.random();
  let age = Math.round(multiplier * (maximum - minimum) + minimum);
  return age;
}

console.log(`Teddy is ${generateRandomNumber(20, 200)} years old!`);