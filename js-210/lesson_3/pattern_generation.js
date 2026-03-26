/*
Write a function that takes a number of rows as the argument nStars and logs a square of numbers and asterisks.
For example, if nStars is 7, log the following pattern:

generatePattern(7);

// console output
1******
12*****
123****
1234***
12345**
123456*
1234567

You may assume that nStars is greater than 1 and less than 10.
*/

function generatePattern(nStars) {
  let numericString = '';
  let asteriskString = '*'.repeat(nStars);

  for (let rowNumber = 1; rowNumber <= nStars; rowNumber += 1) {
    numericString += String(rowNumber); // Add the current number to the numericString
    asteriskString = asteriskString.slice(1); // Remove 1 asterisk, we'll remove it from the front as that is easiest
    console.log(numericString + asteriskString);
  }
}

generatePattern(7);

/*
Have you tried supplying generatePattern with a number greater than 9? What did you observe? Can you fix the current implementation so that it still renders as a rectangle?

generatePattern(20);

// console output
1******************************
12*****************************
123****************************
1234***************************
12345**************************
123456*************************
1234567************************
12345678***********************
123456789**********************
12345678910********************
1234567891011******************
123456789101112****************
12345678910111213**************
1234567891011121314************
123456789101112131415**********
12345678910111213141516********
1234567891011121314151617******
123456789101112131415161718****
12345678910111213141516171819**
1234567891011121314151617181920

*/

function generatePattern(nStars) {
  for (let rowNumber = 1; rowNumber <= nStars; rowNumber += 1) {
    let fullString = '';
    
    for (let num = 1; num <= rowNumber; num += 1) {
      fullString += String(num);
    }
    for (let num = rowNumber + 1; num <= nStars; num += 1) {
      fullString += '*'.repeat(String(num).length);
    }

    console.log(fullString);
  }
}

generatePattern(20);