/*
Write a function logMultiples that takes one argument number.
It should log all multiples of the argument between 0 and 100 (inclusive) that are also odd numbers.
Log the values in descending order.

You may assume that number is an integer between 0 and 100.

logMultiples(17);
// output (5x, 3x and 1x)
85
51
17

logMultiples(21);
// output (3x and 1x)
63
21
*/

function logMultiples(number) {
  let oddMultiples = [];

  for (let multiplier = 1; ; multiplier += 1) {
    let result = multiplier * number;
    if (result > 100) {
      break;
    }
    if (result % 2 !== 0) {
      oddMultiples.push(result);
    }
  }

  oddMultiples.reverse();
  oddMultiples.forEach(multiple => console.log(multiple));
}

logMultiples(21);


/*
The official solution iterates through every number between 100 and 0.
Alternatively, you can determine the number's largest multiple that is less than 100,
then start the loop with that multiple.
With each iteration of the loop, you can decrement the number by the argument;
when the result is negative, you can quit.

As above, we must check each multiple to determine whether it is odd. If it is odd, we log it.

Math.floor(100 / number) * number returns the largest multiple of number that is between 0 and 100.
If you're not familiar with the floor method, see the documentation.
*/

function logMultiples(number) {
  let largestMultiple = Math.floor(100 / number) * number;
  for (let multiple = largestMultiple; multiple >= number; multiple -= number) {
    if (multiple % 2 !== 0) {
      console.log(multiple);
    }
  }
}