/*
Q1:
Modify the age.js program you wrote in the exercises for the Input/Output chapter.
The updated code should use a for loop to display the future ages.
*/

/* Already used a loop there */

/*
Q2:
Write a function that computes and returns the factorial of a number by using a for loop.
The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:

n!	Expansion	         Result
1!	1	                 1
2!	1 * 2	             2
3!	1 * 2 * 3	         6
4!	1 * 2 * 3 * 4	     24
5!	1 * 2 * 3 * 4 * 5	 120

You may assume that the argument is always a positive integer.

*/

function factorial(num) {
  let answer = 1;
  for (let i = num; i > 1; i--) {
    answer *= i;
  }
  return answer;
}

console.log(factorial(1));     // => 1
console.log(factorial(2));     // => 2
console.log(factorial(3));     // => 6
console.log(factorial(4));     // => 24
console.log(factorial(5));     // => 120
console.log(factorial(6));     // => 720
console.log(factorial(7));     // => 5040
console.log(factorial(8));     // => 40320

/*
Q3:
The following code causes an infinite loop (a loop that never stops iterating). Why?


let counter = 0;

while (counter = 1) {
  console.log(counter);
  counter += 1;

  if (counter > 2) {
    break;
  }
}


This is because we're using a single equals in the while condition.
This sets a global variable `counter` to the value 1. The value 1 is always truthy, so the while loop never stops.
`counter` is reset to the value 1 each time the condition is checked, so even though counter gets incremented by 1
within the loop, counter is never > 2, so it never breaks.

*/

/*
Q4:
Does the following code produce an error? Why or why not? What output does this code send to the console?
*/

for (let i = 0; i < 5;) {
  console.log(i += 1);
}

/*
We're missing the increment part of the for loop, so I do think this will raise an error.

EDIT: Actually, no error.
*/

/*
Q5:
The following code uses a randomNumberBetween function to generate a number between its first and second arguments.
It uses a while loop to try to generate a number greater than 2.
Refactor the code so that you don't need to call randomNumberBetween from two different locations, lines 6 and 10.
Do not change the arguments you pass to randomNumberBetween.
*/

function randomNumberBetween(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

let tries = 0;
// let result = randomNumberBetween(1, 6);
// tries += 1;

// while (result <= 2) {
//   result = randomNumberBetween(1, 6);
//   tries += 1;
// }

let result;
do {
  result = randomNumberBetween(1, 6);
  tries += 1;
} while (result <= 2);


console.log('It took ' + String(tries) + ' tries to get a number greater than 2');


/*
Q6:
Reimplement the factorial function from exercise 2 using recursion.
Once again, you may assume that the argument is always a positive integer.
*/

function factorial(num) {
  if (num === 1) return num;
  return num * factorial(num - 1);
}

console.log(factorial(1));     // => 1
console.log(factorial(2));     // => 2
console.log(factorial(3));     // => 6
console.log(factorial(4));     // => 24
console.log(factorial(5));     // => 120
console.log(factorial(6));     // => 720
console.log(factorial(7));     // => 5040
console.log(factorial(8));     // => 40320