/*
Write a function that logs the integers from 1 to 100 (inclusive) that are multiples of either 3 or 5.
If the number is divisible by both 3 and 5, append an "!" to the number.

multiplesOfThreeAndFive();

// output on console
'3'
'5'
'6'
'9'
'10'
'12'
'15!'
// … remainder of output omitted for brevity

*/

function multiplesOfThreeAndFive() {
  for (let i = 1; i <= 100; i += 1) {
    divisibleByThree = i % 3 === 0;
    divisibleByFive = i % 5 === 0;
    if (divisibleByThree && divisibleByFive) {
      console.log(String(i) + '!');
    } else if (divisibleByThree || divisibleByFive) {
      console.log(String(i));
    }
  }
}

multiplesOfThreeAndFive();

/*
For additional practice, how would you change your function so it takes, as arguments,
the range of numbers it should check?
*/

function multiplesOfThreeAndFive(minNumber, maxNumber) {
  for (let i = minNumber; i <= maxNumber; i += 1) {
    divisibleByThree = i % 3 === 0;
    divisibleByFive = i % 5 === 0;
    if (divisibleByThree && divisibleByFive) {
      console.log(String(i) + '!');
    } else if (divisibleByThree || divisibleByFive) {
      console.log(String(i));
    }
  }
}

multiplesOfThreeAndFive(70, 80);